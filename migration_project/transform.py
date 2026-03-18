# transform.py
import json
from mappings import PRIORITY_MAP, STATUS_MAP, ISSUE_TYPE_MAP, PROJECT_MAP

with open("data/issues.json") as f:
    issues = json.load(f)

transformed_issues = []

for issue in issues:
    new_issue = issue.copy()

    # Map priority
    if issue.get("priority") in PRIORITY_MAP:
        new_issue["priority"] = PRIORITY_MAP[issue["priority"]]
    else:
        new_issue["priority"] = "Medium"  # fallback

    # Map status
    if issue.get("status") in STATUS_MAP:
        new_issue["status"] = STATUS_MAP[issue["status"]]
    else:
        new_issue["status"] = "To Do"  # fallback

    # Map issue type
    if issue.get("type") in ISSUE_TYPE_MAP:
        new_issue["type"] = ISSUE_TYPE_MAP[issue["type"]]
    else:
        new_issue["type"] = "Task"  # fallback

    # Map project key
    if issue.get("project_key") in PROJECT_MAP:
        new_issue["project_key"] = PROJECT_MAP[issue["project_key"]]
    else:
        new_issue["project_key"] = "BANK"  # fallback

    transformed_issues.append(new_issue)

with open("data/transformed_issues.json", "w") as f:
    json.dump(transformed_issues, f, indent=4)

print(f"✅ Transformation complete: {len(transformed_issues)} issues")