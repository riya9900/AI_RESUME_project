"""
Reusable UI Component Widgets
"""
import streamlit as st
from src.app.config import FEATURE_LIST
from src.app.core.metrics import DocumentMetrics


def render_sidebar():
    """
    Renders sidebar status navigation panel.
    """
    with st.sidebar:
        st.markdown("### 🧭 Navigation & Status")
        for icon, title, is_active in FEATURE_LIST:
            active_badge = " (Active)" if is_active else ""
            st.markdown(f"- {icon} **{title}**{active_badge}")
        
        st.divider()
        st.markdown("### ⚙️ System Architecture")
        st.caption("Backend: `Python 3.14` + `pypdf`")
        st.caption("UI Framework: `Streamlit 1.62`")
        st.caption("Package Manager: `uv`")


def render_header(title: str, subtitle: str, feature_badge: str):
    """
    Renders styled header section.
    """
    st.markdown(f"""
    <div class="main-header">
        <div class="feature-tag">{feature_badge}</div>
        <div class="main-title">{title}</div>
        <div class="sub-title">{subtitle}</div>
    </div>
    """, unsafe_allow_html=True)


def render_metrics_grid(metrics: DocumentMetrics):
    """
    Renders responsive grid of document metrics cards.
    """
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{metrics.page_count}</div>
            <div class="metric-label">Pages</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{metrics.word_count}</div>
            <div class="metric-label">Words</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{metrics.line_count}</div>
            <div class="metric-label">Lines</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{metrics.char_count}</div>
            <div class="metric-label">Characters</div>
        </div>
        """, unsafe_allow_html=True)
    with col5:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{metrics.estimated_reading_time_min}m</div>
            <div class="metric-label">Read Time</div>
        </div>
        """, unsafe_allow_html=True)
