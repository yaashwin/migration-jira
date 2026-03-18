# load_to_jira.py
import json
import requests

JIRA_URL = "https://one-atlas-gnbd.atlassian.net/"
EMAIL = "muhammed.yaashwin@cprime.com"
API_TOKEN = ""


headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

auth = (EMAIL, API_TOKEN)

with open("data/jira_payload.json") as f:
    jira_issues = json.load(f)

success = 0
failed = 0

for i, issue in enumerate(jira_issues):
    try:
        response = requests.post(
            f"{JIRA_URL}/rest/api/3/issue",
            json=issue,
            headers=headers,
            auth=auth
        )

        if response.status_code == 201:
            key = response.json()["key"]
            print(f"✅ [{i+1}/{len(jira_issues)}] Created: {key}")
            success += 1
        else:
            summary = issue["fields"].get("summary", "Unknown")
            project = issue["fields"]["project"]["key"]
            itype = issue["fields"]["issuetype"]["name"]
            print(f"❌ [{i+1}/{len(jira_issues)}] Failed: {summary}")
            print(f"   Project: {project} | Type: {itype}")
            print(f"   Error: {response.text}")
            failed += 1

    except Exception as e:
        print(f"❌ [{i+1}/{len(jira_issues)}] Exception: {e}")
        failed += 1

print(f"\n{'='*50}")
print(f"✅ Success: {success}")
print(f"❌ Failed:  {failed}")
print(f"📊 Total:   {len(jira_issues)}")