import subprocess
import sys

print("=" * 60)
print("AI PLAYWRIGHT AUTOMATION PIPELINE")
print("=" * 60)


def run_step(title, module):

    print(f"\n{title}")

    result = subprocess.run(
        [sys.executable, "-m", module],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.stderr:
        print(result.stderr)

    return result.returncode


# Step 1
run_step(
    "Step 1 : Generate Playwright Code",
    "ai.generate_playwright_code"
)

# Step 2
run_step(
    "Step 2 : Validate Generated Code",
    "ai.validate_code"
)

# Step 3
status = run_step(
    "Step 3 : Execute Generated Test",
    "ai.run_generated_test"
)

# Step 4

if status == 0:

    run_step(
        "Step 4 : AI Code Review",
        "ai.review_code"
    )

else:

    run_step(
        "Step 4 : AI Failure Analysis",
        "ai.analyze_failure"
    )

print("\nPipeline Completed")