"""
Application Configuration & Theme Settings
"""
from dataclasses import dataclass

APP_TITLE = "AI Resume Matcher & Skill Gap Analyzer"
APP_ICON = "📄"
LAYOUT = "wide"
INITIAL_SIDEBAR_STATE = "expanded"

@dataclass(frozen=True)
class ThemeColors:
    BACKGROUND = "#0E1117"
    CARD_BG = "#1E293B"
    BORDER_COLOR = "#334155"
    TEXT_PRIMARY = "#E0E6ED"
    TEXT_MUTED = "#94A3B8"
    ACCENT_INDIGO = "#6366F1"
    ACCENT_PURPLE = "#A855F7"
    ACCENT_PINK = "#EC4899"
    ACCENT_CYAN = "#38BDF8"

FEATURE_LIST = [
    ("📄", "Feature 1: Resume Upload", True),
    ("🧠", "Feature 2: Skill Extraction", True),
    ("💼", "Feature 3: JD Analysis", False),
    ("🎯", "Feature 4: Job Match Score", False),
    ("❌", "Feature 5: Skill Gap Analysis", False),
    ("📊", "Feature 6: Multi-Score Breakdown", False),
    ("🤖", "Feature 7: AI Recommendations", False),
    ("💼", "Feature 8: Role Recommendation", False),
    ("📋", "Feature 9: Final AI Report", False),
]
