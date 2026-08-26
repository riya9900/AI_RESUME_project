"""
UI Custom Styling Injector
"""
import streamlit as st
from src.app.config import ThemeColors


def inject_custom_styles():
    """
    Injects responsive, glassmorphism dark-mode CSS styles into Streamlit.
    """
    css = f"""
    <style>
        .stApp {{
            background-color: {ThemeColors.BACKGROUND};
            color: {ThemeColors.TEXT_PRIMARY};
        }}
        
        .main-header {{
            background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
            border: 1px solid {ThemeColors.BORDER_COLOR};
            border-radius: 16px;
            padding: 24px 32px;
            margin-bottom: 24px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        }}
        .main-title {{
            font-size: 2.1rem;
            font-weight: 800;
            background: linear-gradient(90deg, {ThemeColors.ACCENT_INDIGO} 0%, {ThemeColors.ACCENT_PURPLE} 50%, {ThemeColors.ACCENT_PINK} 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 6px;
        }}
        .sub-title {{
            color: {ThemeColors.TEXT_MUTED};
            font-size: 1.02rem;
            font-weight: 400;
        }}
        
        .metric-card {{
            background: {ThemeColors.CARD_BG};
            border: 1px solid {ThemeColors.BORDER_COLOR};
            border-radius: 12px;
            padding: 16px 18px;
            text-align: center;
            transition: transform 0.2s ease, border-color 0.2s ease;
        }}
        .metric-card:hover {{
            transform: translateY(-2px);
            border-color: {ThemeColors.ACCENT_INDIGO};
        }}
        .metric-value {{
            font-size: 1.75rem;
            font-weight: 700;
            color: {ThemeColors.ACCENT_CYAN};
        }}
        .metric-label {{
            font-size: 0.82rem;
            color: {ThemeColors.TEXT_MUTED};
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}

        .feature-tag {{
            display: inline-block;
            background: rgba(99, 102, 241, 0.15);
            color: #818CF8;
            border: 1px solid rgba(99, 102, 241, 0.3);
            border-radius: 20px;
            padding: 4px 14px;
            font-size: 0.8rem;
            font-weight: 600;
            margin-bottom: 10px;
        }}

        /* Skill Pills Styling */
        .skill-badge {{
            display: inline-flex;
            align-items: center;
            background: rgba(30, 41, 59, 0.9);
            border: 1px solid rgba(99, 102, 241, 0.4);
            border-radius: 8px;
            padding: 6px 14px;
            margin: 4px;
            font-size: 0.88rem;
            font-weight: 600;
            color: #F1F5F9;
            box-shadow: 0 2px 6px rgba(0,0,0,0.2);
            transition: all 0.2s ease;
        }}
        .skill-badge:hover {{
            border-color: #A855F7;
            background: rgba(99, 102, 241, 0.25);
            transform: scale(1.03);
        }}
        .skill-count {{
            background: #6366F1;
            color: #FFFFFF;
            border-radius: 12px;
            padding: 2px 8px;
            font-size: 0.72rem;
            margin-left: 8px;
            font-weight: 700;
        }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
