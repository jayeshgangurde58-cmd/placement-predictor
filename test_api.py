import sys
sys.path.insert(0, '.')

import asyncio
from backend.main import get_courses

result = asyncio.run(get_courses())
print("Total items:", result["total"])
print("Courses:", result["courses"])
print("Internships:", result["internships"])
print("First item:", result["items"][0]["title"], "(", result["items"][0]["provider"], ")")
print("Last item:", result["items"][-1]["title"], "(", result["items"][-1]["provider"], ")")
