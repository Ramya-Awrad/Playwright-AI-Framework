from ai.ai_helper import analyze_failure

# Read generated code
with open(
    "ai/outputs/generated_playwright_test.py",
    "r",
    encoding="utf-8"
) as f:
    code = f.read()

# Read execution result
with open(
    "ai/outputs/execution_result.txt",
    "r",
    encoding="utf-8"
) as f:
    error = f.read()

analysis = analyze_failure(code, error)

print(analysis)

with open(
    "ai/outputs/failure_analysis.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(analysis)

print("\nFailure analysis completed!")