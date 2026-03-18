# check_jira.py
import requests

JIRA_URL = "https://one-atlas-gnbd.atlassian.net/"
EMAIL = "muhammed.yaashwin@cprime.com"
API_TOKEN = ""


auth = (EMAIL, API_TOKEN)
headers = {"Accept": "application/json"}

# Check projects
print("=== YOUR JIRA PROJECTS ===")
r = requests.get(f"{JIRA_URL}/rest/api/3/project", headers=headers, auth=auth)
for p in r.json():
    print(f"  Key: {p['key']}  Name: {p['name']}")

# Check issue types
print("\n=== YOUR JIRA ISSUE TYPES ===")
r = requests.get(f"{JIRA_URL}/rest/api/3/issuetype", headers=headers, auth=auth)
for it in r.json():
    print(f"  Name: {it['name']}  Subtask: {it.get('subtask', False)}")

# Check priorities
print("\n=== YOUR JIRA PRIORITIES ===")
r = requests.get(f"{JIRA_URL}/rest/api/3/priority", headers=headers, auth=auth)
for p in r.json():
    print(f"  Name: {p['name']}")