from ai.ai_helper import review_playwright_code

with open(
    "ai/outputs/generated_playwright_test.py",
    "r",
    encoding="utf-8"
) as f:

    code = f.read()

review = review_playwright_code(code)

print(review)

with open(
    "ai/outputs/code_review.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write(review)

print("Review completed!")