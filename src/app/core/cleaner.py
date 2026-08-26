"""
Text Normalization & Cleaning Pipeline
"""
import re


class TextCleanerService:
    """
    NLP Text Cleaning Service for resumes and job descriptions.
    """

    @staticmethod
    def clean_text(raw_text: str) -> str:
        """
        Cleans and normalizes text:
        - Removes non-printable control characters.
        - Fixes line-wrapped hyphenated words.
        - Standardizes unicode spaces.
        - Normalizes list bullet formatting.
        - Preserves clean paragraph breaks.
        """
        if not raw_text:
            return ""

        # Remove control characters except newlines/tabs
        cleaned = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]', '', raw_text)

        # Rejoin hyphenated words split across lines (e.g. "micro-\nservices" -> "microservices")
        cleaned = re.sub(r'(\w+)-\s*\n\s*(\w+)', r'\1\2', cleaned)

        # Standardize unicode space variants to standard space
        cleaned = re.sub(r'[\u00A0\u2000-\u200B\u202F\u205F\u3000]', ' ', cleaned)

        # Standardize bullet point formats to clean hyphens
        cleaned = re.sub(r'^[ \t]*[•●▪\*▫\-][ \t]+', '- ', cleaned, flags=re.MULTILINE)

        # Remove multiple inline spaces
        cleaned = re.sub(r'[ \t]+', ' ', cleaned)

        # Remove trailing whitespace per line
        cleaned = re.sub(r' +$', '', cleaned, flags=re.MULTILINE)

        # Collapse 3+ newlines to 2 newlines (preserve paragraphs)
        cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)

        return cleaned.strip()
