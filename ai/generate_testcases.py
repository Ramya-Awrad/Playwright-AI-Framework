from ai.ai_helper import generate_test_cases

requirement = """
User should login successfully using valid username and password.
"""

testcases = generate_test_cases(requirement)

print(testcases)

with open("ai/outputs/login_testcases.txt", "w", encoding="utf-8") as f:
    f.write(testcases)

print("\nTest cases saved successfully!")