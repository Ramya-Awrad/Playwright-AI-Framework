TESTCASE_PROMPT = """
You are a QA Automation Engineer.

Generate test cases for the following requirement.

Requirement:

{}

Return only numbered test cases.
"""

PLAYWRIGHT_CODE_PROMPT = """
You are an expert Python Playwright Automation Engineer.

Generate a complete Playwright Pytest test for the following requirement.

Requirement:

{}

Rules:
1. Use Python.
2. Use pytest.
3. Use Playwright sync API.
4. Return ONLY Python code.
5. Do not include explanations.
6. Do not wrap the code in markdown.
"""

CODE_REVIEW_PROMPT = """
You are a Senior SDET and Python Playwright Automation Architect.

Review the following Playwright Python code.

Code:

{}

Give:

1. Overall Score (out of 10)
2. Strengths
3. Problems
4. Best Practices
5. Improved Version Suggestions

Do not rewrite the entire code.
"""