import json
import ollama


def get_login_credentials():

    prompt = """
Return ONLY valid JSON.

Use these credentials:

Username: standard_user
Password: secret_sauce

Return exactly:

{
    "username":"standard_user",
    "password":"secret_sauce"
}

Do not write explanations.
Do not use markdown.
Do not write any text before or after JSON.
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response["message"]["content"]

    print(content)

    # Find JSON block
    start = content.find("{")
    end = content.rfind("}")

    json_text = content[start:end + 1]

    return json.loads(json_text)