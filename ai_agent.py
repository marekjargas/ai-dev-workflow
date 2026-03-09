import os
import requests
from google import genai

# API key
api_key = os.getenv("GEMINI_API_KEY")

# Gemini client
client = genai.Client(api_key=api_key)

# GitHub údaje
issue_title = os.getenv("ISSUE_TITLE")
issue_body = os.getenv("ISSUE_BODY")
issue_number = os.getenv("ISSUE_NUMBER")
repo = os.getenv("GITHUB_REPOSITORY")
token = os.getenv("GITHUB_TOKEN")


def generate_solution():

    prompt = f"""
You are a senior software developer.

Solve this GitHub issue.

TITLE:
{issue_title}

DESCRIPTION:
{issue_body}

Provide:
- implementation plan
- example code
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text


def comment_on_issue(text):

    url = f"https://api.github.com/repos/{repo}/issues/{issue_number}/comments"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    data = {
        "body": text
    }

    requests.post(url, headers=headers, json=data)


solution = generate_solution()

comment_on_issue(solution)
