import subprocess

result = subprocess.run(
    [
        "pytest",
        "ai/outputs/generated_playwright_test.py",
    ],
    capture_output=True,
    text=True
)

output = result.stdout + "\n" + result.stderr

print(output)

with open(
    "ai/outputs/execution_result.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(output)

if result.returncode == 0:
    print("\n✅ Test Execution Passed")
else:
    print("\n❌ Test Execution Failed")