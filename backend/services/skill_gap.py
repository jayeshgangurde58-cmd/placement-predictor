"""Skill gap analysis service."""

from typing import Dict, List, Any
import urllib.parse

from .course_database import COURSE_DATABASE

JOB_ROLES: Dict[str, List[str]] = {
    "Software Engineer": [
        "Python", "Java", "C++", "Data Structures", "Algorithms", "OOP",
        "Git", "SQL", "Linux", "REST APIs", "Testing", "CI/CD"
    ],
    "Web Developer": [
        "HTML", "CSS", "JavaScript", "React", "Next.js", "Node.js",
        "RESTful APIs", "Git", "Responsive Design", "Deployment", "SEO"
    ],
    "Data Scientist": [
        "Python", "R", "SQL", "Machine Learning", "TensorFlow", "Pandas",
        "NumPy", "Matplotlib", "Statistics", "Data Visualization", "Deep Learning"
    ],
    "DevOps Engineer": [
        "Docker", "Kubernetes", "CI/CD", "AWS", "Linux", "Terraform",
        "Jenkins", "Ansible", "Git", "Monitoring", "Infrastructure as Code"
    ],
    "Machine Learning Engineer": [
        "Python", "TensorFlow", "PyTorch", "Machine Learning", "Deep Learning",
        "NLP", "Computer Vision", "Statistics", "Data Preprocessing", "Model Deployment"
    ],
    "Backend Engineer": [
        "Python", "Java", "Node.js", "REST APIs", "Databases", "SQL",
        "Microservices", "Docker", "Authentication", "Caching", "CI/CD"
    ],
    "Frontend Engineer": [
        "HTML", "CSS", "JavaScript", "React", "TypeScript", "Responsive Design",
        "Accessibility", "Performance Optimization", "Testing", "State Management"
    ],
    "Full Stack Developer": [
        "JavaScript", "React", "Node.js", "Databases", "REST APIs", "SQL",
        "HTML", "CSS", "Deployment", "Git", "Microservices"
    ],
    "Cloud Engineer": [
        "AWS", "Azure", "Google Cloud", "Docker", "Kubernetes", "Networking",
        "Terraform", "Monitoring", "Security", "CI/CD"
    ],
    "Cybersecurity Analyst": [
        "Network Security", "Firewalls", "Encryption", "SIEM", "Vulnerability Assessment",
        "Incident Response", "Risk Management", "Penetration Testing", "Security Policies"
    ],
    "Network Engineer": [
        "TCP/IP", "Routing", "Switching", "Firewalls", "VPN", "Network Monitoring",
        "Troubleshooting", "Wireless Networks", "Subnetting", "OSI Model"
    ],
    "Quality Assurance Engineer": [
        "Test Planning", "Automation", "Selenium", "JUnit", "Performance Testing",
        "Bug Tracking", "API Testing", "Manual Testing", "Regression Testing"
    ],
    "Systems Engineer": [
        "Linux", "Windows Server", "Networking", "Scripting", "Infrastructure",
        "Virtualization", "Monitoring", "Security", "Troubleshooting"
    ],
    "Embedded Systems Engineer": [
        "C", "C++", "Microcontrollers", "RTOS", "Hardware Design",
        "PCB Design", "Signal Processing", "Firmware", "Debugging"
    ],
    "Electrical Engineer": [
        "Circuit Design", "Electronics", "Power Systems", "Signal Processing",
        "Matlab", "Control Systems", "PCB Design", "Instrumentation"
    ],
    "Electronics Engineer": [
        "Digital Electronics", "Analog Circuits", "PCB Layout", "Semiconductors",
        "Microcontrollers", "Signal Processing", "Testing", "Embedded Systems"
    ],
    "Mechanical Engineer": [
        "CAD", "SolidWorks", "Thermodynamics", "Material Science",
        "Manufacturing", "Mechanics", "ANSYS", "Product Design"
    ],
    "Civil Engineer": [
        "Structural Analysis", "AutoCAD", "Building Design", "Material Strength",
        "Construction Management", "Surveying", "Project Planning"
    ],
    "Chemical Engineer": [
        "Process Design", "Heat Transfer", "Fluid Mechanics", "Chemical Thermodynamics",
        "Materials", "Safety", "Reaction Engineering", "Simulation"
    ],
    "Industrial Engineer": [
        "Process Improvement", "Lean Manufacturing", "Six Sigma", "Operations Research",
        "Supply Chain", "Quality Control", "ERP", "Production Planning"
    ],
    "Biomedical Engineer": [
        "Biomaterials", "Medical Imaging", "Signal Processing", "Biomechanics",
        "Regulatory Standards", "CAD", "Data Analysis"
    ],
    "Robotics Engineer": [
        "Robotics", "Control Systems", "C++", "ROS", "Sensors", "Actuators",
        "Automation", "Machine Learning", "Kinematics"
    ],
    "IoT Engineer": [
        "Embedded Systems", "Sensors", "Connectivity", "MQTT", "Cloud Platforms",
        "Security", "Data Analytics", "Firmware", "Networking"
    ],
    "AI Engineer": [
        "Python", "Machine Learning", "Deep Learning", "NLP", "Computer Vision",
        "Model Deployment", "TensorFlow", "PyTorch", "Statistics"
    ]
}


def get_available_roles() -> List[str]:
    """Get list of available job roles."""
    return list(JOB_ROLES.keys())


def _get_skill_recommendations(skill: str) -> Dict[str, List[Dict[str, str]]]:
    """Get real course and internship recommendations from the database."""
    skill_data = COURSE_DATABASE.get(skill)
    if skill_data:
        return {
            "skill": skill,
            "courses": skill_data.get("courses", []),
            "internships": skill_data.get("internships", []),
        }
    # Fallback for skills not in database
    return {
        "skill": skill,
        "courses": [
            {"course": f"Intro to {skill}", "platform": "Coursera", "url": "https://www.coursera.org"},
            {"course": f"Practical {skill}", "platform": "Udemy", "url": "https://www.udemy.com"},
            {"course": f"{skill} Fundamentals", "platform": "Pluralsight", "url": "https://www.pluralsight.com"},
            {"course": f"Advanced {skill}", "platform": "LinkedIn Learning", "url": "https://www.linkedin.com/learning"},
            {"course": f"Hands-On {skill}", "platform": "DataCamp", "url": "https://www.datacamp.com"},
        ],
        "internships": [
            {"company": "Tech Pathways", "role": f"{skill} Intern", "location": "Remote", "url": "https://careers.example.com"},
        ],
    }


def analyze_skill_gap(user_skills: List[str], role: str) -> Dict[str, Any]:
    """Analyze skill gaps for a user applying for a role."""
    if role not in JOB_ROLES:
        return {"error": f"Role '{role}' not found", "available_roles": get_available_roles()}

    required_skills = JOB_ROLES[role]
    user_skills_set = set(skill.strip().lower() for skill in user_skills)

    matching_skills = []
    for skill in required_skills:
        lower_skill = skill.lower()
        if lower_skill in user_skills_set or any(lower_skill in us for us in user_skills_set):
            matching_skills.append(skill)

    missing_skills = [skill for skill in required_skills if skill not in matching_skills]
    total_required = len(required_skills)
    total_matched = len(matching_skills)
    total_missing = len(missing_skills)
    match_rate = round((total_matched / total_required) * 100, 1) if total_required else 0
    skill_gap_index = round((total_missing / total_required), 2) if total_required else 0

    recommendations = [_get_skill_recommendations(skill) for skill in missing_skills]

    radar_data = [
        {"skill": skill, "has": 1 if skill in matching_skills else 0}
        for skill in required_skills
    ]

    return {
        "target_role": role,
        "required_skills": required_skills,
        "matched_skills": matching_skills,
        "missing_skills": missing_skills,
        "match_rate": match_rate,
        "skill_gap_index": skill_gap_index,
        "recommendations": recommendations,
        "radar_data": radar_data,
        "total_required": total_required,
        "total_matched": total_matched,
        "total_missing": total_missing,
    }
