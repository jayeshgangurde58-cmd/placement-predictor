import ast

with open('backend/services/course_database.py', 'r', encoding='utf-8') as f:
    content = f.read()

print(f'File length: {len(content)} chars')
print(f'Last 100 chars: {repr(content[-100:])}')
print(f'Count of {{ : {content.count(chr(123))}')
print(f'Count of }} : {content.count(chr(125))}')

try:
    ast.parse(content)
    print('AST parse: OK')
except SyntaxError as e:
    print(f'SyntaxError at line {e.lineno}, col {e.offset}: {e.msg}')
    lines = content.split('\n')
    if e.lineno <= len(lines):
        print(f'Line {e.lineno}: {lines[e.lineno-1]}')

