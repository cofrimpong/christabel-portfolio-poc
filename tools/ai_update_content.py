import json
import os
import sys
import requests

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "").strip()
ISSUE_TITLE = (os.environ.get("ISSUE_TITLE") or "").strip()
ISSUE_BODY = (os.environ.get("ISSUE_BODY") or "").strip()

if not OPENAI_API_KEY:
    print("Missing OPENAI_API_KEY (GitHub Secret).")
    sys.exit(1)

# Load current content.json
with open("content.json", "r", encoding="utf-8") as f:
    current = f.read()

instruction = f"""You are updating a GitHub Pages portfolio site.
Rules:
- ONLY output valid JSON.
- Output must match the existing top-level keys and structure of the current content.json.
- Do not add new top-level keys.
- Do not remove required fields; if unsure, keep original values.
- Do not include markdown fences or commentary.

Issue title: {ISSUE_TITLE}

User request:
{ISSUE_BODY}

Current content.json:
{current}

Return the updated content.json as raw JSON only.
"""

# Call OpenAI Responses API
resp = requests.post(
    "https://api.openai.com/v1/responses",
    headers={
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    },
    json={
        "model": "gpt-4o-mini",
        "input": instruction,
    },
    timeout=60,
)

if resp.status_code >= 300:
    print("OpenAI API error:", resp.status_code, resp.text)
    sys.exit(1)

data = resp.json()

# The response text is typically in output[0].content[0].text
try:
    text = data["output"][0]["content"][0]["text"]
except Exception:
    print("Unexpected OpenAI response shape:", json.dumps(data)[:1000])
    sys.exit(1)

text = text.strip()

# Validate JSON
try:
    updated_obj = json.loads(text)
except json.JSONDecodeError:
    print("AI did not return valid JSON. Output was:\n", text[:1500])
    sys.exit(1)

# Write pretty JSON back
with open("content.json", "w", encoding="utf-8") as f:
    json.dump(updated_obj, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("content.json updated successfully.")
