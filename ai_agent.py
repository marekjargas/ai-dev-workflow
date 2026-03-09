import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")


def solve_issue(issue_text):

    prompt = f"""
    You are a senior software developer.

    Implement the following feature:

    {issue_text}

    Steps:
    1 analyze the task
    2 propose implementation
    3 generate code
    """

    response = model.generate_content(prompt)

    return response.text


if __name__ == "__main__":

    issue = "Create REST endpoint POST /login with JWT authentication"

    result = solve_issue(issue)

    print(result)
