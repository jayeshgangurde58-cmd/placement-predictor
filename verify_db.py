#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

try:
    from backend.services.course_database import COURSE_DATABASE
    print(f"Skills: {len(COURSE_DATABASE)}")
    total_courses = 0
    total_internships = 0
    for skill, data in COURSE_DATABASE.items():
        courses = len(data.get('courses', []))
        internships = len(data.get('internships', []))
        total_courses += courses
        total_internships += internships
        print(f"{skill}: {courses} courses, {internships} internships")
    print(f"\nTotal courses: {total_courses}")
    print(f"Total internships: {total_internships}")
    print(f"Total items: {total_courses + total_internships}")
except Exception as e:
    print(f"ERROR: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
