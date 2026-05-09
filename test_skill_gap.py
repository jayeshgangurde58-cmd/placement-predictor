import sys
sys.path.insert(0, '.')

from backend.services.skill_gap import analyze_skill_gap

result = analyze_skill_gap([], 'Software Engineer')
print(f"Target role: {result['target_role']}")
print(f"Missing skills: {len(result['missing_skills'])}")
print(f"Recommendations count: {len(result['recommendations'])}")

for rec in result['recommendations']:
    skill = rec['skill']
    courses = rec['courses']
    internships = rec['internships']
    print(f"  {skill}: {len(courses)} courses, {len(internships)} internships")
    if courses:
        print(f"    First course: {courses[0]['course']} ({courses[0]['platform']})")
    if internships:
        print(f"    First internship: {internships[0]['company']} - {internships[0]['role']}")
