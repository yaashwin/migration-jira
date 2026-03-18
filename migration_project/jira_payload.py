# jira_payload.py
import json


def text_to_adf(text):
    """Convert plain text to Atlassian Document Format."""
    if not text or text.strip() == "":
        return {
            "version": 1,
            "type": "doc",
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "No description provided"
                        }
                    ]
                }
            ]
        }

    return {
        "version": 1,
        "type": "doc",
        "content": [
            {
                "type": "paragraph",
                "content": [
                    {
                        "type": "text",
                        "text": text
                    }
                ]
            }
        ]
    }


# Load transformed issues
with open("data/transformed_issues.json") as f:
    issues = json.load(f)

jira_issues = []

for issue in issues:
    jira_issue = {
        "fields": {
            "project": {
                "key": issue.get("project_key", "BANK")
            },
            "summary": issue.get("title", "No title"),
            "description": text_to_adf(issue.get("description", "")),
            "issuetype": {
                "name": issue.get("type", "Task")
            },
            "priority": {
                "name": issue.get("priority", "Medium")
            }
        }
    }

    jira_issues.append(jira_issue)

with open("data/jira_payload.json", "w") as f:
    json.dump(jira_issues, f, indent=4)

print(f"✅ Jira payload ready: {len(jira_issues)} issues")