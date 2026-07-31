from ai.ai_helper import generate_playwright_code

requirement = """
User should login successfully using valid username and password.
"""

code = generate_playwright_code(requirement)

# Remove markdown if present
code = code.replace("```python", "")
code = code.replace("```", "")
code = code.strip()

with open(
    "ai/outputs/generated_playwright_test.py",
    "w",
    encoding="utf-8"
) as f:
    f.write(code)

print("\nPlaywright code generated successfully!")