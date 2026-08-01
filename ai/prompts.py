TESTCASE_PROMPT = """
You are a QA Automation Engineer.

Generate test cases for the following requirement.

Requirement:

{}

Return only numbered test cases.
"""

PLAYWRIGHT_CODE_PROMPT = """
You are a Senior Python QA Automation Engineer.

Generate ONLY Python Playwright code.

Requirements:

1. Use pytest.
2. Use Playwright Sync API only.
3. Do NOT use async.
4. Do NOT use await.
5. Do NOT use pytest.mark.
6. Import:

from playwright.sync_api import sync_playwright

7. Application URL:
https://www.saucedemo.com/

8. Login credentials:

Username:
standard_user

Password:
secret_sauce

9. Use these exact locators:

Username:
#user-name

Password:
#password

Login Button:
#login-button

10. Verify successful login using:

assert "inventory.html" in page.url

11. Return ONLY Python code.

12. Do NOT return markdown.

13. Do NOT explain anything.

Requirement:

{}
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

FAILURE_ANALYSIS_PROMPT = """
You are a Senior Python Playwright Automation Engineer.

Analyze the following Playwright test failure.

Generated Playwright Code:

{}

Execution Error:

{}

Provide the following:

1. Root Cause
2. Why the failure happened
3. Suggested Fix
4. Correct Playwright code snippet
5. Best Practice

Return plain text only.
"""