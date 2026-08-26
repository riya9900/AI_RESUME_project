"""
Document Analytics & Metrics Calculator
"""
import re
from dataclasses import dataclass


@dataclass(frozen=True)
class DocumentMetrics:
    page_count: int
    word_count: int
    line_count: int
    char_count: int
    estimated_reading_time_min: float


class MetricsCalculatorService:
    """
    Computes analytical metrics for document text.
    """

    @staticmethod
    def calculate_metrics(text: str, page_count: int = 1) -> DocumentMetrics:
        """
        Calculates word count, character count, line count, and reading time.
        """
        words = re.findall(r'\b\w+\b', text)
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        word_count = len(words)
        char_count = len(text)
        line_count = len(lines)
        reading_time = round(word_count / 200, 1) if word_count else 0.0

        return DocumentMetrics(
            page_count=page_count,
            word_count=word_count,
            line_count=line_count,
            char_count=char_count,
            estimated_reading_time_min=reading_time
        )
