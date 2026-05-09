"""
Smart Placement Predictor & Skill Gap Analyzer — FastAPI Backend
"""

import os
from typing import List, Optional
from dotenv import load_dotenv
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

load_dotenv()

from services.predictor import predict_placement
from services.skill_gap import analyze_skill_gap, get_available_roles
from services.bulk_processor import process_bulk_csv
from services.resume_parser import parse_resume
from services.course_database import COURSE_DATABASE

# ─── App Setup ────────────────────────────────────────────────────────────────

app = FastAPI(
    title="Smart Placement Predictor API",
    description="ML API for placement prediction and skill gap analysis",
    version="1.0.0",
)

raw_origins = os.getenv("CORS_ORIGINS", "http://localhost:3000,http://127.0.0.1:3000,http://localhost:3001,http://127.0.0.1:3001")
CORS_ORIGINS = [origin.strip() for origin in raw_origins.split(",") if origin.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ─── Request / Response Models ─────────────────────────────────────────────────

class PredictRequest(BaseModel):
    cgpa: float = Field(..., ge=0.0, le=10.0, description="CGPA on a 10-point scale")
    aptitude: float = Field(..., ge=0, le=100, description="Aptitude test score (0-100)")
    programming: float = Field(..., ge=0, le=100, description="Programming skills score (0-100)")
    communication: float = Field(..., ge=0, le=100, description="Communication skills score (0-100)")
    tenth_percentage: float = Field(..., ge=0, le=100, description="10th grade percentage (0-100)")
    twelfth_percentage: float = Field(..., ge=0, le=100, description="12th grade percentage (0-100)")
    projects: int = Field(..., ge=0, le=20, description="Number of projects completed")
    internships: int = Field(..., ge=0, le=10, description="Number of internships completed")


class SkillGapRequest(BaseModel):
    skills: List[str] = Field(..., description="List of user's current skills")
    target_role: str = Field(..., description="Target job role")


@app.get("/health")
async def health():
    return {"status": "ok", "service": "Smart Placement Predictor API v1.0"}


@app.get("/roles")
async def list_roles():
    """Get all available job roles for skill gap analysis."""
    return {"roles": get_available_roles()}


@app.post("/predict")
async def predict(request: PredictRequest):
    """Predict placement probability for a single student."""
    try:
        result = predict_placement(
            cgpa=request.cgpa,
            aptitude=request.aptitude,
            programming=request.programming,
            communication=request.communication,
            tenth_percentage=request.tenth_percentage,
            twelfth_percentage=request.twelfth_percentage,
            projects=request.projects,
            internships=request.internships,
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")


@app.post("/skill-gap")
async def skill_gap(request: SkillGapRequest):
    """Analyse skill gap between user skills and target job role."""
    result = analyze_skill_gap(request.skills, request.target_role)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result


@app.post("/parse-resume")
async def parse_resume_endpoint(file: UploadFile = File(...)):
    """Parse a PDF resume and extract skills automatically."""
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    try:
        file_bytes = await file.read()
        skills = parse_resume(file_bytes)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Resume parsing failed: {exc}")
    return {"filename": file.filename, "extracted_skills": skills, "count": len(skills)}


@app.post("/bulk-analysis")
async def bulk_analysis(file: UploadFile = File(...)):
    """Process a CSV of multiple students and return per-student predictions."""
    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are supported.")
    file_bytes = await file.read()
    result = process_bulk_csv(file_bytes, file.filename)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result


def get_domain_for_platform(platform: str) -> str:
    """Map platform name to its domain."""
    domain_map = {
        # Course platforms
        "coursera": "coursera.org",
        "udemy": "udemy.com",
        "edx": "edx.org",
        "pluralsight": "pluralsight.com",
        "linkedin learning": "linkedin.com",
        "linkedin": "linkedin.com",
        "nptel": "nptel.ac.in",
        "swayam": "swayam.gov.in",
        "codecademy": "codecademy.com",
        "freecodecamp": "freecodecamp.org",
        "khan academy": "khanacademy.org",
        "mit opencourseware": "ocw.mit.edu",
        "stanford online": "online.stanford.edu",
        "harvard online": "online.harvard.edu",
        "skillshare": "skillshare.com",
        "datacamp": "datacamp.com",
        "kaggle": "kaggle.com",
        "brilliant": "brilliant.org",
        "treehouse": "teamtreehouse.com",
        "udacity": "udacity.com",
        "great learning": "greatlearning.in",
        "simplilearn": "simplilearn.com",
        "upgrad": "upgrad.com",
        "intellipaat": "intellipaat.com",
        "scaler": "scaler.com",
        "geeksforgeeks": "geeksforgeeks.org",
        "tutorialspoint": "tutorialspoint.com",
        "w3schools": "w3schools.com",
        "hackerrank": "hackerrank.com",
        "leetcode": "leetcode.com",
        "codechef": "codechef.com",
        "codeforces": "codeforces.com",
        "aws": "aws.amazon.com",
        "google cloud": "cloud.google.com",
        "microsoft learn": "microsoft.com",
        "azure": "microsoft.com",
        "github": "github.com",
        "jetbrains academy": "jetbrains.com",
        "alison": "alison.com",
        "future learn": "futurelearn.com",
        "futurelearn": "futurelearn.com",
        "coursera (deeplearning.ai)": "deeplearning.ai",
        "deeplearning.ai": "deeplearning.ai",
        "fast.ai": "fast.ai",
        "cloudskillsboost": "cloudskillsboost.google",
        "google developers": "developers.google.com",
        "owasp": "owasp.org",
        "cybrary": "cybrary.it",
        "offensive security": "offensive-security.com",
        "sans": "sans.org",
        "ec-council": "eccouncil.org",
        "isc2": "isc2.org",
        "cisco": "cisco.com",
        "comptia": "comptia.org",
        "red hat": "redhat.com",
        "oracle academy": "oracle.com",
        "mit": "mit.edu",
        "stanford": "stanford.edu",
        "harvard": "harvard.edu",
    }
    return domain_map.get(platform.lower(), platform.lower().replace(" ", "") + ".com")


def get_platform_logo(platform: str) -> str:
    """Get logo URL for a platform using Google Favicon CDN (always works)."""
    domain = get_domain_for_platform(platform)
    return f"https://www.google.com/s2/favicons?domain={domain}&sz=128"


def get_company_logo(company: str) -> str:
    """Get logo URL for a company using Google Favicon CDN (always works)."""
    company_domain_map = {
        # Big Tech
        "google": "google.com",
        "microsoft": "microsoft.com",
        "amazon": "amazon.com",
        "apple": "apple.com",
        "meta": "meta.com",
        "facebook": "facebook.com",
        "netflix": "netflix.com",
        "oracle": "oracle.com",
        "ibm": "ibm.com",
        "sap": "sap.com",
        "nvidia": "nvidia.com",
        "bloomberg": "bloomberg.com",
        "adobe": "adobe.com",
        "salesforce": "salesforce.com",
        "servicenow": "servicenow.com",
        "workday": "workday.com",
        "twilio": "twilio.com",
        "stripe": "stripe.com",
        "shopify": "shopify.com",
        "spotify": "spotify.com",
        "twitter": "twitter.com",
        "x": "x.com",
        "linkedin": "linkedin.com",
        "uber": "uber.com",
        "airbnb": "airbnb.com",
        "lyft": "lyft.com",
        "tesla": "tesla.com",
        "spacex": "spacex.com",
        "intel": "intel.com",
        "amd": "amd.com",
        "qualcomm": "qualcomm.com",
        "cisco": "cisco.com",
        "vmware": "vmware.com",
        "atlassian": "atlassian.com",
        "slack": "slack.com",
        "zoom": "zoom.us",
        "dropbox": "dropbox.com",
        "box": "box.com",
        "github": "github.com",
        "gitlab": "gitlab.com",
        "hashicorp": "hashicorp.com",
        "datadog": "datadoghq.com",
        "splunk": "splunk.com",
        "elastic": "elastic.co",
        "mongodb": "mongodb.com",
        "databricks": "databricks.com",
        "snowflake": "snowflake.com",
        "palantir": "palantir.com",
        "crowdstrike": "crowdstrike.com",
        "palo alto networks": "paloaltonetworks.com",
        "fortinet": "fortinet.com",
        "cloudflare": "cloudflare.com",
        "fastly": "fastly.com",
        # Indian IT companies
        "tcs": "tcs.com",
        "infosys": "infosys.com",
        "wipro": "wipro.com",
        "hcl": "hcltech.com",
        "tech mahindra": "techmahindra.com",
        "ltimindtree": "ltimindtree.com",
        "l&t technology": "ltts.com",
        "mphasis": "mphasis.com",
        "hexaware": "hexaware.com",
        "mindtree": "mindtree.com",
        "persistent systems": "persistent.com",
        "cyient": "cyient.com",
        "coforge": "coforge.com",
        "zensar": "zensar.com",
        "mastech": "mastech.com",
        "infoedge": "infoedge.in",
        "zoho": "zoho.com",
        "freshworks": "freshworks.com",
        "razorpay": "razorpay.com",
        "paytm": "paytm.com",
        "phonepe": "phonepe.com",
        "flipkart": "flipkart.com",
        "meesho": "meesho.com",
        "swiggy": "swiggy.com",
        "zomato": "zomato.com",
        "ola": "olacabs.com",
        "naukri": "naukri.com",
        "byju's": "byjus.com",
        "byjus": "byjus.com",
        "unacademy": "unacademy.com",
        "vedantu": "vedantu.com",
        "dream11": "dream11.com",
        "cred": "cred.club",
        "groww": "groww.in",
        "zerodha": "zerodha.com",
        "upstox": "upstox.com",
        # Global consulting/finance
        "deloitte": "deloitte.com",
        "accenture": "accenture.com",
        "mckinsey": "mckinsey.com",
        "bcg": "bcg.com",
        "bain": "bain.com",
        "pwc": "pwc.com",
        "kpmg": "kpmg.com",
        "ey": "ey.com",
        "goldman sachs": "goldmansachs.com",
        "morgan stanley": "morganstanley.com",
        "jp morgan": "jpmorgan.com",
        "jpmorgan": "jpmorgan.com",
        "citibank": "citi.com",
        "wells fargo": "wellsfargo.com",
        "bank of america": "bankofamerica.com",
        "blackrock": "blackrock.com",
        # More tech
        "siemens": "siemens.com",
        "bosch": "bosch.com",
        "honeywell": "honeywell.com",
        "ge": "ge.com",
        "general electric": "ge.com",
        "philips": "philips.com",
        "abb": "abb.com",
        "schneider electric": "se.com",
        "emerson": "emerson.com",
        "rockwell automation": "rockwellautomation.com",
        "ptc": "ptc.com",
        "ansys": "ansys.com",
        "dassault systemes": "3ds.com",
        "autodesk": "autodesk.com",
        "synopsys": "synopsys.com",
        "cadence": "cadence.com",
        "arm": "arm.com",
        "broadcom": "broadcom.com",
        "microchip": "microchip.com",
        "texas instruments": "ti.com",
        "ti": "ti.com",
        "nxp": "nxp.com",
        "stmicroelectronics": "st.com",
        "renesas": "renesas.com",
        "mediatek": "mediatek.com",
        "samsung": "samsung.com",
        "lg": "lg.com",
        "sony": "sony.com",
        "panasonic": "panasonic.com",
        "toshiba": "toshiba.com",
        "hitachi": "hitachi.com",
        "fujitsu": "fujitsu.com",
        "nec": "nec.com",
        "ericsson": "ericsson.com",
        "nokia": "nokia.com",
        "huawei": "huawei.com",
        "zte": "zte.com.cn",
        "lenovo": "lenovo.com",
        "hp": "hp.com",
        "dell": "dell.com",
        "western digital": "westerndigital.com",
        "seagate": "seagate.com",
        "micron": "micron.com",
        "kingston": "kingston.com",
        "corsair": "corsair.com",
        "logitech": "logitech.com",
        "razr": "razer.com",
        "razer": "razer.com",
    }
    domain = company_domain_map.get(company.lower(), company.lower().replace(" ", "") + ".com")
    return f"https://www.google.com/s2/favicons?domain={domain}&sz=128"


def get_topic_image(topic: str, item_type: str) -> str:
    """Get a high-quality representational image for a topic from Unsplash."""
    # Mapping of topics to Unsplash IDs
    topic_map = {
        "python": "1_A_6_5X_S78",  # Python code
        "java": "pE_S_S78",  # Java/Code
        "javascript": "I_S_S78",  # JS/Code
        "typescript": "T_S_S78",
        "react": "R_S_S78",
        "node.js": "N_S_S78",
        "next.js": "NX_S_S78",
        "html": "H_S_S78",
        "css": "C_S_S78",
        "sql": "S_S_S78",
        "databases": "D_S_S78",
        "machine learning": "ML_S_S78",
        "deep learning": "DL_S_S78",
        "ai": "AI_S_S78",
        "cloud": "CL_S_S78",
        "aws": "AWS_S_S78",
        "azure": "AZ_S_S78",
        "google cloud": "GCP_S_S78",
        "docker": "DK_S_S78",
        "kubernetes": "K8_S_S78",
        "devops": "DO_S_S78",
        "security": "SEC_S_S78",
        "data science": "DS_S_S78",
        "algorithms": "ALG_S_S78",
        "data structures": "DSA_S_S78",
        "testing": "TST_S_S78",
        "linux": "LX_S_S78",
        "git": "GIT_S_S78",
        "nlp": "NLP_S_S78",
        "computer vision": "CV_S_S78",
        "statistics": "STAT_S_S78",
    }

    # High quality Unsplash image IDs for categories
    unsplash_map = {
        "python": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=800&q=80",
        "java": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=800&q=80",
        "javascript": "https://images.unsplash.com/photo-1579468118864-1b9ea3c0db4a?auto=format&fit=crop&w=800&q=80",
        "react": "https://images.unsplash.com/photo-1633356122544-f134324a6cee?auto=format&fit=crop&w=800&q=80",
        "web": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=800&q=80",
        "mobile": "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?auto=format&fit=crop&w=800&q=80",
        "cloud": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=800&q=80",
        "data": "https://images.unsplash.com/photo-1551288049-bbbda536339a?auto=format&fit=crop&w=800&q=80",
        "ai": "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=800&q=80",
        "ml": "https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?auto=format&fit=crop&w=800&q=80",
        "code": "https://images.unsplash.com/photo-1542831371-29b0f74f9713?auto=format&fit=crop&w=800&q=80",
        "design": "https://images.unsplash.com/photo-1561070791-2526d30994b5?auto=format&fit=crop&w=800&q=80",
        "office": "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=800&q=80",
        "internship": "https://images.unsplash.com/photo-1521737711867-e3b97375f902?auto=format&fit=crop&w=800&q=80",
        "server": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=800&q=80",
        "security": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=800&q=80",
    }

    t = topic.lower()
    if item_type == "internship":
        # For internships, use office/professional images
        if "google" in t or "microsoft" in t or "amazon" in t:
            return unsplash_map["office"]
        return unsplash_map["internship"]
    
    # For courses, use topic-specific images
    if "python" in t: return unsplash_map["python"]
    if "java" in t: return unsplash_map["java"]
    if "javascript" in t or "react" in t or "next.js" in t or "html" in t or "css" in t: return unsplash_map["web"]
    if "cloud" in t or "aws" in t or "azure" in t or "gcp" in t: return unsplash_map["cloud"]
    if "data" in t or "analysis" in t or "statistics" in t or "pandas" in t: return unsplash_map["data"]
    if "ai" in t or "machine learning" in t or "deep learning" in t or "intelligence" in t: return unsplash_map["ai"]
    if "security" in t or "network" in t or "firewall" in t: return unsplash_map["security"]
    if "docker" in t or "kubernetes" in t or "server" in t: return unsplash_map["server"]
    
    return unsplash_map["code"]


@app.get("/courses")
async def get_courses():
    """Get all courses and internships from the database."""
    items = []
    course_count = 0
    internship_count = 0
    id_counter = 1

    for skill, data in COURSE_DATABASE.items():
        for course in data.get("courses", []):
            items.append({
                "id": id_counter,
                "title": course["course"],
                "provider": course["platform"],
                "type": "course",
                "category": skill,
                "skills": [skill],
                "url": course["url"],
                "logo": get_platform_logo(course["platform"]),
                "image": get_topic_image(course["course"], "course"),
            })
            id_counter += 1
            course_count += 1

        for internship in data.get("internships", []):
            items.append({
                "id": id_counter,
                "title": f"{internship['role']} from {internship['company']}",
                "provider": internship["company"],
                "type": "internship",
                "category": skill,
                "skills": [skill],
                "url": internship["url"],
                "logo": get_company_logo(internship["company"]),
                "image": get_topic_image(internship["company"], "internship"),
            })
            id_counter += 1
            internship_count += 1

    return {
        "total": len(items),
        "courses": course_count,
        "internships": internship_count,
        "items": items,
    }
