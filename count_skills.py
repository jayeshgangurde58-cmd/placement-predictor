import re
with open('backend/services/course_database.py', 'r', encoding='utf-8') as f:
    content = f.read()
keys = re.findall(r'"([A-Za-z][A-Za-z0-9\s/+\-()\.]+)":\s*\{', content)
print(f'Found {len(keys)} skills:')
for k in keys:
    print(k)

