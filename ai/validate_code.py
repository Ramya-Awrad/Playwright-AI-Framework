import ast

file_path = "ai/outputs/generated_playwright_test.py"

with open(file_path, "r", encoding="utf-8") as f:
    code = f.read()

try:
    ast.parse(code)
    print("[PASS] Python syntax is valid.")
except SyntaxError as e:
    print("[FAIL] Syntax Error")
    print(e)

if "async def" in code:
    print("[WARNING] Async function detected.")

if "await " in code:
    print("[WARNING] Await keyword detected.")

if "pytest.mark" in code:
    print("[WARNING] pytest.mark detected.")

if "sync_playwright" not in code:
    print("[WARNING] sync_playwright not found.")