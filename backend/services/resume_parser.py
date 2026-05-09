"""PDF resume skill extraction service."""

import re
from typing import List

import os
import json
from groq import Groq

# All skills we know about
ALL_SKILLS = [
    "Python", "Java", "JavaScript", "TypeScript", "C", "C++", "C#", "Go", "Rust", "Kotlin", "Swift",
    "HTML", "CSS", "React", "Next.js", "Vue", "Angular", "Node.js", "Express", "Django", "Flask", "FastAPI",
    "SQL", "MySQL", "PostgreSQL", "MongoDB", "SQLite", "Firebase", "Redis",
    "Machine Learning", "Deep Learning", "NLP", "Computer Vision", "TensorFlow", "PyTorch", "Scikit-learn",
    "Pandas", "NumPy", "Matplotlib", "Seaborn", "Data Visualization", "Statistics",
    "Docker", "Kubernetes", "AWS", "Azure", "GCP", "Terraform", "Ansible", "CI/CD", "Jenkins",
    "Git", "GitHub", "Linux", "REST APIs", "GraphQL", "Microservices",
    "Android SDK", "Material Design", "Networking", "Ethical Hacking", "Cryptography",
    "Responsive Design", "MLOps", "Monitoring", "Incident Response", "Firewalls",
    "Vulnerability Assessment", "SIEM", "Scikit-learn", "MLOps",
]


def extract_skills_from_text(text: str) -> List[str]:
    """Extract skills from raw resume text using Groq LLM (with regex fallback)."""
    
    api_key = os.getenv("GROQ_API_KEY")
    if api_key and api_key != "your-groq-api-key":
        try:
            client = Groq(api_key=api_key)
            prompt = (
                "You are an expert technical recruiter."
                "Extract all technical skills, programming languages, and tools from the following resume text. "
                "Return them strictly as a JSON array of strings, with no markdown or extra conversational text.\n\n"
                f"Resume:\n{text[:3000]}"
            )
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama3-8b-8192",
                temperature=0.1,
                response_format={"type": "json_object"}
            )
            
            response_text = chat_completion.choices[0].message.content
            # Try to grab the array itself, assuming the model might wrap it like {"skills": [...]}
            data = json.loads(response_text)
            if isinstance(data, list):
                return data
            elif isinstance(data, dict):
                for v in data.values():
                    if isinstance(v, list):
                        return v
        except Exception as e:
            print(f"Groq extraction failed: {e}. Falling back to Regex.")

    # Fallback logic
    found = set()
    text_lower = text.lower()
    for skill in ALL_SKILLS:
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'
        if re.search(pattern, text_lower):
            found.add(skill)
    return sorted(found)


def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Extract text from PDF using pdfplumber."""
    try:
        import io
        import pdfplumber
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            pages_text = []
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    pages_text.append(page_text)
        return "\n".join(pages_text)
    except Exception as e:
        raise RuntimeError(f"PDF text extraction failed: {e}")


def parse_resume(file_bytes: bytes) -> List[str]:
    """Full pipeline: PDF → text → skills."""
    text = extract_text_from_pdf(file_bytes)
    if not text:
        return []
    return extract_skills_from_text(text)
