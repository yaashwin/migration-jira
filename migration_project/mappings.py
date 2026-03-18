# mappings.py

# PRIORITY MAPPING
PRIORITY_MAP = {
    "Showstopper": "Highest",
    "Urgent": "Highest",
    "High_Priority": "High",
    "Medium_Priority": "Medium",
    "Normal": "Medium",
    "Low_Priority": "Low",
    "Nice_To_Have": "Lowest",
    "Backlog_Priority": "Lowest",
    "Deferred": "Lowest",
    "Unprioritized": "Medium",
}

# STATUS MAPPING
STATUS_MAP = {
    "New": "To Do",
    "Open": "To Do",
    "In_Analysis": "In Progress",
    "Ready_For_Dev": "To Do",
    "In_Development": "In Progress",
    "Code_Review": "In Progress",
    "Ready_For_QA": "To Do",
    "In_QA": "In Progress",
    "QA_Failed": "To Do",
    "Ready_For_UAT": "To Do",
    "In_UAT": "In Progress",
    "Approved": "Done",
    "Done": "Done",
    "Closed": "Done",
    "On_Hold": "To Do",
    "Cancelled": "Done",
}

# ISSUE TYPE MAPPING
# ⚠️ Change these to match YOUR Jira's issue types from check_jira.py output
ISSUE_TYPE_MAP = {
    "Epic": "Epic",
    "Story": "Story",
    "Task": "Task",
    "Bug": "Bug",
    "Sub-task": "Subtask",        # ← Jira Cloud uses "Subtask" not "Sub-task"
    "Spike": "Task",
    "Change_Request": "Story",
    "Tech_Debt": "Task",
    "Improvement": "Story",
    "Incident": "Bug",
    "Service_Request": "Task",
    "Test_Case": "Task",
}

# PROJECT KEY MAPPING
# ⚠️ Map ALL source project keys to ONE project that EXISTS in your Jira
# Replace "BANK" with whatever project key you have in your Jira
PROJECT_MAP = {
    "BANK": "BANK",       # ← change to your actual Jira project key
    "ECOM": "BANK",       # ← all mapped to same project for testing
    "HRM": "BANK",
    "CRM": "BANK",
    "DEVOPS": "BANK",
    "MOB": "BANK",
    "DATA": "BANK",
    "SEC": "BANK",
    "QA": "BANK",
    "CLOUD": "BANK",
}