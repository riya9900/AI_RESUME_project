"""
AI Skill Extraction View Component (Feature 2)
"""
import streamlit as st
from src.app.core.skill_extractor import SkillExtractorService, SkillExtractionResult
from src.app.ui.components import render_header


def render_skill_extraction_component(text: str):
    """
    Renders extracted skill badges and analytics directly for the provided text.
    """
    if not text or not text.strip():
        st.info("👈 Upload a resume above to extract skills automatically.")
        return

    skill_result: SkillExtractionResult = SkillExtractorService.extract_skills(text)

    st.markdown("### 🧠 AI Skill Extraction Results")

    if skill_result.total_skills_found == 0:
        st.warning("No technical skills matching taxonomy were detected in the text.")
        return

    # Top level metric summary
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{skill_result.total_skills_found}</div>
            <div class="metric-label">Total Unique Skills Extracted</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        top_cat = max(skill_result.categories.items(), key=lambda item: len(item[1]))[0] if skill_result.categories else "N/A"
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{top_cat.split()[0]}</div>
            <div class="metric-label">Dominant Category ({top_cat})</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Category Tab View
    category_names = list(skill_result.categories.keys())
    tab_all, *cat_tabs = st.tabs(["✨ All Skills"] + category_names)

    with tab_all:
        st.markdown("#### All Identified Skills")
        badge_html = ""
        for cat, skills in skill_result.categories.items():
            for s in skills:
                badge_html += f'<span class="skill-badge">{s.name} <span class="skill-count">{s.frequency}x</span></span>'
        st.markdown(badge_html, unsafe_allow_html=True)

    for tab, cat_name in zip(cat_tabs, category_names):
        with tab:
            st.markdown(f"#### {cat_name}")
            skills = skill_result.categories[cat_name]
            badge_html = ""
            for s in skills:
                badge_html += f'<span class="skill-badge">{s.name} <span class="skill-count">{s.frequency}x</span></span>'
            st.markdown(badge_html, unsafe_allow_html=True)


def render_skill_extraction_standalone_view():
    """
    Renders standalone Feature 2 View with custom text input or session text.
    """
    render_header(
        title="🧠 AI Skill Extraction",
        subtitle="Automatically identify technical skills, frameworks, cloud tools, and domain expertise.",
        feature_badge="🧠 Feature 2 — Skill Extraction"
    )

    resume_text = st.session_state.get("cleaned_resume_text", "")
    
    if not resume_text:
        st.markdown("#### Paste Resume Text for Skill Analysis")
        input_text = st.text_area("Input Text", height=200, placeholder="Paste resume text or skills here...")
        if input_text:
            render_skill_extraction_component(input_text)
    else:
        render_skill_extraction_component(resume_text)
