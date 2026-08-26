"""
AI Skill Extraction Service & Taxonomy Engine
"""
import re
from typing import Dict, List, Set, NamedTuple
from dataclasses import dataclass, field


@dataclass
class ExtractedSkill:
    name: str
    category: str
    frequency: int
    confidence: float  # Scale 0.0 to 1.0


@dataclass
class SkillExtractionResult:
    total_skills_found: int
    categories: Dict[str, List[ExtractedSkill]] = field(default_factory=dict)
    all_skills_flat: List[str] = field(default_factory=list)


# Comprehensive Skill Taxonomy Dictionary
SKILL_TAXONOMY: Dict[str, Dict[str, List[str]]] = {
    "🛠️ Languages & Core": {
        "Python": [r"\bpython\b", r"\bpython3\b"],
        "SQL": [r"\bsql\b", r"\btsql\b", r"\bpostgresql\b", r"\bmysql\b", r"\bsqlite\b"],
        "C++": [r"\bc\+\+\b", r"\bcpp\b"],
        "C#": [r"\bc#\b", r"\bcsharp\b"],
        "Java": [r"\bjava\b"],
        "JavaScript": [r"\bjavascript\b", r"\bjs\b", r"\bes6\b"],
        "TypeScript": [r"\btypescript\b", r"\bts\b"],
        "R": [r"\br\b", r"\brlang\b", r"\br-lang\b"],
        "Go": [r"\bgolang\b", r"\bgo\b"],
        "Rust": [r"\brust\b"],
        "Bash / Shell": [r"\bbash\b", r"\bshell\b", r"\bzsh\b", r"\bpowershell\b"],
        "HTML/CSS": [r"\bhtml\b", r"\bcss\b", r"\bhtml5\b", r"\bcss3\b"]
    },
    "🧠 AI / ML / Data Science": {
        "PyTorch": [r"\bpytorch\b", r"\btorch\b"],
        "TensorFlow": [r"\btensorflow\b", r"\btf\b", r"\bkeras\b"],
        "Scikit-Learn": [r"\bscikit-learn\b", r"\bsklearn\b", r"\bscikit\b"],
        "NLP": [r"\bnlp\b", r"\bnatural language processing\b"],
        "LLMs": [r"\bllm\b", r"\bllms\b", r"\blarge language model\b", r"\blarge language models\b"],
        "LangChain": [r"\blangchain\b"],
        "LlamaIndex": [r"\bllamaindex\b", r"\bllama-index\b"],
        "RAG": [r"\brag\b", r"\bretrieval-augmented generation\b", r"\bretrieval augmented generation\b"],
        "Transformers": [r"\btransformers\b", r"\bhuggingface\b", r"\bhugging face\b", r"\bbert\b", r"\bgpt\b"],
        "Deep Learning": [r"\bdeep learning\b", r"\bdl\b", r"\bneural networks\b", r"\bcnn\b", r"\brnn\b", r"\blstm\b"],
        "Machine Learning": [r"\bmachine learning\b", r"\bml\b"],
        "Computer Vision": [r"\bcomputer vision\b", r"\bcv\b", r"\bopencv\b", r"\byolo\b"],
        "Pandas": [r"\bpandas\b"],
        "NumPy": [r"\bnumpy\b"],
        "SciPy": [r"\bscipy\b"],
        "Matplotlib / Seaborn": [r"\bmatplotlib\b", r"\bseaborn\b"],
        "Vector Databases": [r"\bchroma\b", r"\bchromadb\b", r"\bpinecone\b", r"\bweaviate\b", r"\bqdrant\b", r"\bfaiss\b"],
        "MLflow": [r"\bmlflow\b"],
        "Feature Engineering": [r"\bfeature engineering\b"]
    },
    "☁️ Cloud & DevOps": {
        "AWS": [r"\baws\b", r"\bamazon web services\b", r"\bs3\b", r"\bec2\b", r"\blambda\b", r"\bsagemaker\b"],
        "GCP": [r"\bgcp\b", r"\bgoogle cloud\b", r"\bgoogle cloud platform\b", r"\bbigquery\b", r"\bvertex ai\b"],
        "Azure": [r"\bazure\b", r"\bmicrosoft azure\b"],
        "Docker": [r"\bdocker\b", r"\bcontainerization\b", r"\bcontainers\b"],
        "Kubernetes": [r"\bkubernetes\b", r"\bk8s\b"],
        "MLOps": [r"\bmlops\b", r"\bmachine learning operations\b"],
        "CI/CD": [r"\bci/cd\b", r"\bci-cd\b", r"\bgithub actions\b", r"\bjenkins\b", r"\bgitlab ci\b"],
        "Git": [r"\bgit\b", r"\bgithub\b", r"\bgitlab\b"],
        "Terraform": [r"\bterraform\b", r"\biac\b", r"\binfrastructure as code\b"],
        "Linux": [r"\blinux\b", r"\bubuntu\b", r"\bdebian\b"]
    },
    "🌐 Web & Backend": {
        "FastAPI": [r"\bfastapi\b", r"\bfast api\b"],
        "Flask": [r"\bflask\b"],
        "Django": [r"\bdjango\b"],
        "Node.js": [r"\bnode\.js\b", r"\bnodejs\b", r"\bnode\b"],
        "React": [r"\breact\b", r"\breactjs\b", r"\breact\.js\b"],
        "REST APIs": [r"\brest\b", r"\brestful\b", r"\brest api\b", r"\brest apis\b", r"\bapi\b", r"\bapis\b"],
        "GraphQL": [r"\bgraphql\b"],
        "PostgreSQL": [r"\bpostgres\b", r"\bpostgresql\b"],
        "MongoDB": [r"\bmongodb\b", r"\bmongo\b"],
        "Redis": [r"\bredis\b"],
        "Streamlit": [r"\bstreamlit\b"],
        "Microservices": [r"\bmicroservices\b", r"\bmicroservice\b"]
    },
    "🤝 Soft Skills & Practices": {
        "System Design": [r"\bsystem design\b", r"\barchitecture\b", r"\bscalable systems\b"],
        "Agile / Scrum": [r"\bagile\b", r"\bscrum\b", r"\bkanban\b"],
        "Problem Solving": [r"\bproblem solving\b", r"\banalytical skills\b", r"\bcritical thinking\b"],
        "Team Leadership": [r"\bleadership\b", r"\bmentorship\b", r"\bteam lead\b", r"\bmanagement\b"],
        "Communication": [r"\bcommunication\b", r"\bpresentation\b", r"\bstakeholder management\b"],
        "Project Management": [r"\bproject management\b", r"\bjira\b", r"\bconfluence\b"]
    }
}


class SkillExtractorService:
    """
    AI Skill Extraction & Categorization Engine.
    """

    @staticmethod
    def extract_skills(text: str) -> SkillExtractionResult:
        """
        Extracts skills from input text using taxonomy pattern matching.
        """
        if not text:
            return SkillExtractionResult(total_skills_found=0)

        cleaned_text_lower = text.lower()
        extracted_by_category: Dict[str, List[ExtractedSkill]] = {}
        all_skills_flat: Set[str] = set()
        total_found = 0

        for category_name, skills_dict in SKILL_TAXONOMY.items():
            category_skills: List[ExtractedSkill] = []

            for skill_name, patterns in skills_dict.items():
                total_matches = 0
                for pattern in patterns:
                    matches = re.findall(pattern, cleaned_text_lower)
                    total_matches += len(matches)

                if total_matches > 0:
                    confidence = min(1.0, 0.75 + (total_matches * 0.08))
                    category_skills.append(
                        ExtractedSkill(
                            name=skill_name,
                            category=category_name,
                            frequency=total_matches,
                            confidence=round(confidence, 2)
                        )
                    )
                    all_skills_flat.add(skill_name)
                    total_found += 1

            if category_skills:
                # Sort skills by frequency descending
                category_skills.sort(key=lambda s: s.frequency, reverse=True)
                extracted_by_category[category_name] = category_skills

        return SkillExtractionResult(
            total_skills_found=total_found,
            categories=extracted_by_category,
            all_skills_flat=sorted(list(all_skills_flat))
        )
