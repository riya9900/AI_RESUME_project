import re
import io
from typing import Dict, Any, Tuple
from pypdf import PdfReader


def extract_text_from_pdf(pdf_file: io.BytesIO) -> Tuple[str, int]:
    """
    Extracts raw text from a PDF file stream using pypdf.
    Returns a tuple of (raw_text, page_count).
    """
    try:
        reader = PdfReader(pdf_file)
        page_count = len(reader.pages)
        extracted_pages = []

        for page_idx, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                extracted_pages.append(text)
        
        raw_text = "\n\n".join(extracted_pages)
        return raw_text, page_count
    except Exception as e:
        raise ValueError(f"Failed to read PDF file: {str(e)}")


def clean_resume_text(raw_text: str) -> str:
    """
    Cleans and normalizes raw resume text:
    - Normalizes unicode whitespace and control characters.
    - Fixes hyphenated line-breaks (e.g., 'devel-\nopment' -> 'development').
    - Standardizes bullet points and list markers.
    - Removes excessive blank lines while preserving paragraph boundaries.
    """
    if not raw_text:
        return ""

    # Replace null bytes and non-printable control characters
    cleaned = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]', '', raw_text)

    # Fix hyphenated words broken across lines
    cleaned = re.sub(r'(\w+)-\s*\n\s*(\w+)', r'\1\2', cleaned)

    # Replace non-breaking spaces and other whitespace variations with standard space
    cleaned = re.sub(r'[\u00A0\u2000-\u200B\u202F\u205F\u3000]', ' ', cleaned)

    # Standardize bullet markers to standard hyphen list format
    cleaned = re.sub(r'^[ \t]*[•●▪\*▫\-][ \t]+', '- ', cleaned, flags=re.MULTILINE)

    # Replace multiple spaces with a single space
    cleaned = re.sub(r'[ \t]+', ' ', cleaned)

    # Remove trailing spaces on lines
    cleaned = re.sub(r' +$', '', cleaned, flags=re.MULTILINE)

    # Replace 3 or more consecutive newlines with 2 newlines (preserve paragraphs)
    cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)

    return cleaned.strip()


def analyze_text_stats(cleaned_text: str, page_count: int = 1) -> Dict[str, Any]:
    """
    Generates summary statistics for extracted resume text.
    """
    words = re.findall(r'\b\w+\b', cleaned_text)
    lines = [line.strip() for line in cleaned_text.split('\n') if line.strip()]
    
    return {
        "page_count": page_count,
        "word_count": len(words),
        "char_count": len(cleaned_text),
        "line_count": len(lines),
        "estimated_reading_time_min": round(len(words) / 200, 1) if words else 0.0
    }
