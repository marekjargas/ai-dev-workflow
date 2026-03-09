kimport os
import google.generativeai as genai

# načítanie API key z GitHub Secrets
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

# model
model = genai.GenerativeModel("gemini-1.5-flash")


def solve_issue(issue_title, issue_body):

    prompt = f"""
You are a senior software engineer.

Implement the following GitHub issue.

TITLE:
{issue_title}

DESCRIPTION:
{issue_body}

Provide:
1. short implementation plan
2. example code
3. explanation
"""

    response = model.generate_content(prompt)

    return response.text


if __name__ == "__main__":

    # GitHub Actions poskytne tieto premenné
    issue_title = os.getenv("ISSUE_TITLE")
    issue_body = os.getenv("ISSUE_BODY")

    result = solve_issue(issue_title, issue_body)

    print(result)

    # uloženie výstupu
    with open("ai_output.md", "w") as f:
        f.write(result)
