"""
Resume Upload & Skill Extraction View (Features 1 & 2)
"""
import io
import streamlit as st
from src.app.core.pdf_parser import PDFParserService
from src.app.core.cleaner import TextCleanerService
from src.app.core.metrics import MetricsCalculatorService
from src.app.ui.components import render_header, render_metrics_grid
from src.app.ui.views.skill_extraction_view import render_skill_extraction_component


def render_resume_upload_view():
    """
    Renders Feature 1 (Resume Upload & PDF Text Processing) and Feature 2 (AI Skill Extraction).
    """
    render_header(
        title="📄 Resume Upload & 🧠 AI Skill Extraction",
        subtitle="Upload your PDF resume to extract clean text and automatically detect technical & soft skills.",
        feature_badge="📄 Feature 1 & 🧠 Feature 2 — Extraction Engine"
    )

    st.markdown("### 📤 Upload PDF Resume")
    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=["pdf"],
        help="Select a PDF resume file to extract text and analyze skills."
    )

    if uploaded_file is not None:
        try:
            with st.spinner("Processing PDF document and extracting skills..."):
                pdf_bytes = io.BytesIO(uploaded_file.read())
                extraction_result = PDFParserService.extract_text(pdf_bytes)
                cleaned_text = TextCleanerService.clean_text(extraction_result.raw_text)
                metrics = MetricsCalculatorService.calculate_metrics(
                    cleaned_text, page_count=extraction_result.page_count
                )
                st.session_state["cleaned_resume_text"] = cleaned_text

            st.success(f"Successfully processed `{uploaded_file.name}` ({uploaded_file.size / 1024:.1f} KB)")

            # Render Feature 1 Document Metrics
            render_metrics_grid(metrics)
            st.markdown("<br>", unsafe_allow_html=True)

            # Main View Tabs: Feature 2 (Skill Extraction) & Feature 1 (Text Views)
            main_tab_skills, main_tab_text = st.tabs(["🧠 AI Extracted Skills", "📄 Extracted Text & Export"])

            with main_tab_skills:
                render_skill_extraction_component(cleaned_text)

            with main_tab_text:
                tab_clean, tab_raw, tab_download = st.tabs([
                    "✨ Cleaned Text", "🔍 Raw Extracted Text", "📥 Export Cleaned Text"
                ])

                with tab_clean:
                    st.markdown("#### Normalized & Standardized Resume Text")
                    st.text_area(
                        label="Cleaned Resume Text",
                        value=cleaned_text,
                        height=350,
                        help="Cleaned text with normalized spacing, standardized bullet points, and fixed line breaks."
                    )

                with tab_raw:
                    st.markdown("#### Raw Extracted Text")
                    st.text_area(
                        label="Raw Text",
                        value=extraction_result.raw_text,
                        height=350,
                        help="Unfiltered raw text extracted directly from the PDF document."
                    )

                with tab_download:
                    st.markdown("#### Export Cleaned Text File")
                    output_filename = f"cleaned_{uploaded_file.name.replace('.pdf', '')}.txt"
                    st.download_button(
                        label="📥 Download Cleaned Resume (.txt)",
                        data=cleaned_text,
                        file_name=output_filename,
                        mime="text/plain",
                        use_container_width=True
                    )

        except Exception as e:
            st.error(f"Error processing PDF file: {str(e)}")
    else:
        st.info("👈 Upload a PDF resume above to see extracted skills and document statistics.")
