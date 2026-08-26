# AI Resume Matcher & Skill Gap Analyzer - Plan

## Overview
An AI-powered web application that analyzes PDF resumes against job descriptions, calculates semantic similarity scores using vector embeddings, performs detailed skill gap analysis, scores resumes across key dimensions, provides AI-driven recommendations, and suggests target job roles.

---

## Main Features

### 📄 1. Resume Upload
- Support PDF resume file upload.
- Extract raw text from uploaded PDF documents.
- Clean and normalize resume text (remove formatting artifacts, extra spaces, special symbols).

### 🧠 2. AI Skill Extraction
- Automatically identify technical and soft skills from extracted text.
- Skill taxonomy detection (e.g., Python, PyTorch, SQL, NLP, AWS, Docker, Scikit-Learn, FastApi, System Design, etc.).

### 💼 3. Job Description Analysis
- User input field to paste any target Job Description (JD).
- Extract required skills, preferred qualifications, and key experience requirements.

### 🎯 4. Job Match Score
- Calculate semantic similarity between Resume ↔ Job Description using vector embeddings (e.g. `SentenceTransformer` / Cosine similarity).
- Output visual match score percentage (e.g. **82% Match**).

### ❌ 5. Skill Gap Analysis
- Categorized analysis:
  - ✅ **Matching skills**: Skills present in both Resume & Job Description.
  - ❌ **Missing skills**: Required skills missing from Resume.
  - ⚠️ **Partially matching skills**: Domain-adjacent or related skills (e.g. PyTorch vs TensorFlow, AWS vs GCP).

### 📊 6. Resume Score Breakdown (/100)
- Multi-dimensional scoring framework:
  - **Skills Score** (Weight: 35%)
  - **Experience Score** (Weight: 25%)
  - **Projects Score** (Weight: 20%)
  - **Education Score** (Weight: 20%)
  - **Overall Score** out of 100 with visual radar/bar charts.

### 🤖 7. AI Recommendations
- Highlight profile **Strengths**.
- Identify profile **Weaknesses**.
- Actionable **Resume Improvement Suggestions** (bullet rewrites, keyword optimization).

### 💼 8. Job Role Recommendation
- Predict best-fit career roles based on skill profile:
  - AI Engineer
  - ML Engineer
  - Data Scientist
  - NLP Engineer
  - MLOps Engineer
  - Data Engineer / Backend Engineer

### 📋 9. Final AI Report & Dashboard
- Clean, responsive dashboard displaying all results, match gauges, breakdown charts, and exportable report options.

---

## Environment & Tech Stack Setup (using `uv`)

### Tooling
- **Package Manager**: `uv`
- **Backend**: Python 3.10+ with FastAPI & Uvicorn
- **PDF Extraction**: `pypdf`
- **AI & NLP**: `sentence-transformers`, `scikit-learn`, `numpy`
- **Frontend**: Glassmorphism Dark-Mode Web UI (HTML5, Vanilla CSS, JS, Chart.js)

### Commands
```bash
# Initialize Python project
uv init --app

# Add required dependencies
uv add fastapi uvicorn pypdf sentence-transformers scikit-learn numpy python-multipart pydantic

# Run local development server
uv run uvicorn app.main:app --reload --port 8000
```
