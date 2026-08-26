"""
Main Streamlit Application Entrypoint
"""
import streamlit as st
import sys
from pathlib import Path

# Ensure src directory is in Python path for clean module imports
root_path = Path(__file__).resolve().parent.parent.parent
if str(root_path) not in sys.path:
    sys.path.insert(0, str(root_path))

from src.app.config import APP_TITLE, APP_ICON, LAYOUT, INITIAL_SIDEBAR_STATE
from src.app.ui.styles import inject_custom_styles
from src.app.ui.components import render_sidebar
from src.app.ui.views.resume_upload_view import render_resume_upload_view

# Page Config Initialization
st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout=LAYOUT,
    initial_sidebar_state=INITIAL_SIDEBAR_STATE
)


def main():
    # Inject Custom Styling
    inject_custom_styles()

    # Render Sidebar Component
    render_sidebar()

    # Render Active Feature View (Feature 1)
    render_resume_upload_view()


if __name__ == "__main__":
    main()
