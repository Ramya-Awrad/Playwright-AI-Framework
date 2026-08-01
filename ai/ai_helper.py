import ollama

from ai.prompts import TESTCASE_PROMPT, PLAYWRIGHT_CODE_PROMPT, CODE_REVIEW_PROMPT, FAILURE_ANALYSIS_PROMPT


def generate_test_cases(requirement):

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": TESTCASE_PROMPT.format(requirement)
            }
        ]
    )

    return response["message"]["content"]


def generate_playwright_code(requirement):

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": PLAYWRIGHT_CODE_PROMPT.format(requirement)
            }
        ]
    )

    return response["message"]["content"]

def review_playwright_code(code):

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": CODE_REVIEW_PROMPT.format(code)
            }
        ]
    )

    return response["message"]["content"]

def analyze_failure(code, error):

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": FAILURE_ANALYSIS_PROMPT.format(code, error)
            }
        ]
    )

    return response["message"]["content"]