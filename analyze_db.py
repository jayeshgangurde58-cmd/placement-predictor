import re

with open('backend/services/course_database.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Match skill keys more broadly
keys = re.findall(r'"([^"]+)":\s*\{\s*\n\s*"courses"', content)
print(f'Found {len(keys)} skills:')
for k in keys:
    print(k)

# Count courses and internships per skill
for k in keys:
    pattern = rf'"{re.escape(k)}":\s*\{{.*?"courses":\s*\[(.*?)\],\s*"internships":\s*\[(.*?)\]'
    m = re.search(pattern, content, re.DOTALL)
    if m:
        courses = len(re.findall(r'\{\"course\"', m.group(1)))
        internships = len(re.findall(r'\{\"company\"', m.group(2)))
        print(f'{k}: {courses} courses, {internships} internships')
    else:
        print(f'{k}: COULD NOT PARSE')

total_courses = len(re.findall(r'"course":', content))
total_internships = len(re.findall(r'"company":', content))
print(f'\nTotal courses: {total_courses}')
print(f'Total internships: {total_internships}')
print(f'Total items: {total_courses + total_internships}')

