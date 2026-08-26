"""
PDF Extraction Service
"""
import io
from typing import NamedTuple
from pypdf import PdfReader


class PDFExtractionResult(NamedTuple):
    raw_text: str
    page_count: int


class PDFParserService:
    """
    Robust PDF Text Extraction Service built on pypdf.
    """

    @staticmethod
    def extract_text(pdf_file: io.BytesIO) -> PDFExtractionResult:
        """
        Extracts plain text and page metadata from an in-memory PDF stream.
        """
        try:
            reader = PdfReader(pdf_file)
            page_count = len(reader.pages)
            extracted_pages = []

            for page in reader.pages:
                text = page.extract_text()
                if text:
                    extracted_pages.append(text)

            raw_text = "\n\n".join(extracted_pages)
            return PDFExtractionResult(raw_text=raw_text, page_count=page_count)
        except Exception as e:
            raise ValueError(f"Failed to read PDF document: {str(e)}") from e
