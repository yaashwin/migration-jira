
## Overview

This project simulates a **real-world Jira migration** scenario where:

1. A **source system** (Flask API) holds project management data with **custom field names, statuses, priorities, and issue types**
2. Data is **extracted** from the source system via REST API calls
3. Data is **transformed** by mapping custom values to Jira-compatible values
4. Data is **loaded** into Jira Cloud using the Jira REST API v3

> **Purpose:** Built for Jira migration testing and learning ETL pipeline concepts for project management tool migrations.

---

## Architecture

```
┌─────────────────────┐
│   SOURCE SYSTEM     │
│   (Flask API)       │
│   xyz_api.py        │
│   Port: 5000        │
└────────┬────────────┘
         │
         │  Step 4: HTTP GET requests
         ▼
┌─────────────────────┐
│   EXTRACT           │
│   extract.py        │
│   Saves to data/    │
└────────┬────────────┘
         │
         │  Step 5: Read JSON files
         ▼
┌─────────────────────┐
│   TRANSFORM         │
│   transform.py      │
│   Uses mappings.py  │
└────────┬────────────┘
         │
         │  Step 6: Read transformed data
         ▼
┌─────────────────────┐
│   GENERATE PAYLOAD  │
│   jira_payload.py   │
│   ADF conversion    │
└────────┬────────────┘
         │
         │  Step 7: HTTP POST requests
         ▼
┌─────────────────────┐
│   JIRA CLOUD        │
│   load_to_jira.py   │
│   REST API v3       │
└─────────────────────┘
```

---

## Project Structure

```
project-api/
│
├── xyz_api.py                  # Source system Flask API (simulates legacy tool)
│
└── migration_project/
    │
    ├── check.py                # Checks your Jira instance for valid values
    ├── mappings.py             # All field mapping configurations
    ├── extract.py              # Extracts data from source API
    ├── transform.py            # Transforms data using mappings
    ├── jira_payload.py         # Converts to Jira API v3 format (ADF)
    ├── load_to_jira.py         # Loads data into Jira Cloud
    ├── requirements.txt        # Python dependencies
    ├── README.md               # This file
    │
    └── data/                   # Auto-created directory for JSON files
        ├── projects.json           # Extracted projects
        ├── users.json              # Extracted users
        ├── roles.json              # Extracted roles
        ├── issue-types.json        # Extracted issue types
        ├── issues.json             # Extracted issues
        ├── comments.json           # Extracted comments
        ├── links.json              # Extracted issue links
        ├── worklogs.json           # Extracted work logs
        ├── sprints.json            # Extracted sprints
        ├── versions.json           # Extracted versions
        ├── components.json         # Extracted components
        ├── labels.json             # Extracted labels
        ├── priorities.json         # Extracted priorities
        ├── statuses.json           # Extracted statuses
        ├── resolutions.json        # Extracted resolutions
        ├── custom-fields.json      # Extracted custom field definitions
        ├── boards.json             # Extracted boards
        ├── workflows.json          # Extracted workflows
        ├── attachments.json        # Extracted attachment metadata
        ├── changelogs.json         # Extracted change history
        ├── migration-summary.json  # Migration statistics
        ├── transformed_issues.json # Issues after mapping transformation
        └── jira_payload.json       # Final Jira-ready payload
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Python** | Python 3.6 or higher |
| **pip** | Python package manager |
| **Jira Cloud Account** | Active Jira Cloud instance |
| **Jira API Token** | Generated from Atlassian account settings |
| **Jira Project** | At least one project created in Jira |
| **Network** | Internet access to reach Jira Cloud |

### Generate Jira API Token

1. Go to [https://id.atlassian.com/manage-profile/security/api-tokens](https://id.atlassian.com/manage-profile/security/api-tokens)
2. Click **"Create API token"**
3. Give it a label (e.g., "Migration Tool")
4. Copy the token — **you won't see it again**

---

## Setup

### 1. Clone / Navigate to the project

```bash
cd ~/project-api
```

### 2. Create a virtual environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install flask requests
```

Or create a `requirements.txt`:

```
flask==3.0.0
requests==2.31.0
```

Then install:

```bash
pip install -r requirements.txt
```

### 4. Verify installation

```bash
python3 -c "import flask; import requests; print('All dependencies installed ✅')"
```

---

## Step-by-Step Execution

### Step 1: Start the Source API

Open **Terminal 1**:

```bash
cd ~/project-api
source venv/bin/activate
python3 xyz_api.py
```

**Expected output:**

```
============================================================
  JIRA MIGRATION TEST API - SOURCE SYSTEM
  Visit http://localhost:5000/ for endpoint documentation
============================================================
 * Running on http://127.0.0.1:5000
```

**Verify it works:**

```bash
# In another terminal
curl http://localhost:5000/
curl http://localhost:5000/migration-summary
```

> ⚠️ **Keep this terminal running** throughout the migration process.

---

### Step 2: Check Your Jira Instance

Open **Terminal 2**:

```bash
cd ~/project-api/migration_project
source ../venv/bin/activate
```

**Edit `check.py`** with your Jira credentials:

```python
# check.py
import requests

JIRA_URL = "https://your-domain.atlassian.net"   # ← YOUR Jira URL
EMAIL = "your-email@company.com"                  # ← YOUR email
API_TOKEN = "your-api-token"                      # ← YOUR API token

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
```

**Run it:**

```bash
python3 check.py
```

**Note down:**
- ✅ Which **project keys** exist (e.g., `BANK`, `MOB`)
- ✅ Which **issue types** exist (e.g., `Epic`, `Story`, `Task`, `Bug`, `Sub-task`)
- ✅ Which **priorities** exist (e.g., `Critical`, `Highest`, `High`, `Medium`, `Low`, `Lowest`)

---

### Step 3: Configure Mappings

**Edit `mappings.py`** based on the output from Step 2:

```python
# mappings.py

# =========================================================
# PROJECT KEY MAPPING
# Source project keys → Your actual Jira project keys
# =========================================================
PROJECT_MAP = {
    "BANK": "BANK",       # ← Change to your actual project key
    "ECOM": "BANK",
    "HRM": "BANK",
    "CRM": "BANK",
    "DEVOPS": "BANK",
    "MOB": "MOB",          # ← If MOB exists in your Jira
    "DATA": "BANK",
    "SEC": "BANK",
    "QA": "BANK",
    "CLOUD": "BANK",
}

# =========================================================
# PRIORITY MAPPING
# Source priorities → Jira priorities
# =========================================================
PRIORITY_MAP = {
    "Showstopper": "Critical",
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

# =========================================================
# STATUS MAPPING
# Source statuses → Jira statuses
# =========================================================
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

# =========================================================
# ISSUE TYPE MAPPING
# Source issue types → Jira issue types
# =========================================================
ISSUE_TYPE_MAP = {
    "Epic": "Epic",
    "Story": "Story",
    "Task": "Task",
    "Bug": "Bug",
    "Sub-task": "Sub-task",
    "Spike": "Task",
    "Change_Request": "Story",
    "Tech_Debt": "Task",
    "Improvement": "Story",
    "Incident": "Bug",
    "Service_Request": "Task",
    "Test_Case": "Task",
}
```

---

### Step 4: Extract Data

**File: `extract.py`**

This pulls all data from the source API and saves it as JSON files.

```bash
python3 extract.py
```

**Expected output:**

```
Fetching projects...
Saved projects.json
Fetching users...
Saved users.json
Fetching roles...
Saved roles.json
Fetching issue-types...
Saved issue-types.json
Fetching issues...
Saved issues.json
Fetching comments...
Saved comments.json
Fetching links...
Saved links.json
Fetching worklogs...
Saved worklogs.json
Fetching sprints...
Saved sprints.json
Fetching versions...
Saved versions.json
Fetching components...
Saved components.json
Fetching labels...
Saved labels.json
Fetching priorities...
Saved priorities.json
Fetching statuses...
Saved statuses.json
Fetching resolutions...
Saved resolutions.json
Fetching custom-fields...
Saved custom-fields.json
Fetching boards...
Saved boards.json
Fetching workflows...
Saved workflows.json
Fetching attachments...
Saved attachments.json
Fetching changelogs...
Saved changelogs.json
Fetching migration-summary...
Saved migration-summary.json
✅ Extraction Completed
```

**Verify:**

```bash
ls -la data/
cat data/issues.json | python3 -m json.tool | head -30
```

---

### Step 5: Transform Data

**File: `transform.py`**

This reads extracted issues and applies all mappings from `mappings.py`.

```bash
python3 transform.py
```

**Expected output:**

```
✅ Transformation complete: 50 issues
```

**Verify the transformation worked:**

```bash
# Check a transformed issue
python3 -c "
import json
with open('data/transformed_issues.json') as f:
    issues = json.load(f)
print(json.dumps(issues[0], indent=2))
"
```

**You should see Jira-compatible values:**

```json
{
  "priority": "High",          ← was "High_Priority"
  "status": "In Progress",     ← was "In_Development"
  "type": "Epic",              ← stayed "Epic"
  "project_key": "BANK"        ← mapped correctly
}
```

---

### Step 6: Generate Jira Payload

**File: `jira_payload.py`**

This converts transformed data into **Jira API v3 format**, including converting plain text descriptions to **Atlassian Document Format (ADF)**.

```bash
python3 jira_payload.py
```

**Expected output:**

```
✅ Jira payload ready: 50 issues
```

**Verify the payload format:**

```bash
python3 -c "
import json
with open('data/jira_payload.json') as f:
    issues = json.load(f)
print(json.dumps(issues[0], indent=2))
"
```

**Should look like:**

```json
{
  "fields": {
    "project": {
      "key": "BANK"
    },
    "summary": "Build login system",
    "description": {
      "version": 1,
      "type": "doc",
      "content": [
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "Implement complete authentication system..."
            }
          ]
        }
      ]
    },
    "issuetype": {
      "name": "Epic"
    },
    "priority": {
      "name": "High"
    }
  }
}
```

---

### Step 7: Load to Jira

**File: `load_to_jira.py`**

**Edit the credentials** in `load_to_jira.py`:

```python
JIRA_URL = "https://your-domain.atlassian.net"   # ← YOUR Jira URL
EMAIL = "your-email@company.com"                  # ← YOUR email
API_TOKEN = "your-api-token"                      # ← YOUR API token
```

**Run it:**

```bash
python3 load_to_jira.py
```

**Expected output:**

```
✅ [1/50] Created: BANK-101
✅ [2/50] Created: BANK-102
✅ [3/50] Created: BANK-103
...
==================================================
✅ Success: 50
❌ Failed:  0
📊 Total:   50
```

---

## File Descriptions

### Source System

| File | Purpose | When to Run |
|---|---|---|
| `xyz_api.py` | Flask API simulating a legacy project management tool. Contains 50 issues, 15 users, 10 projects, custom statuses/priorities/types | **First — keep running** |

### Migration Pipeline

| File | Purpose | Input | Output |
|---|---|---|---|
| `check.py` | Connects to your Jira and lists available projects, issue types, priorities | Jira credentials | Terminal output |
| `mappings.py` | Configuration file with all field mappings | Manual configuration | Imported by `transform.py` |
| `extract.py` | Fetches all data from source API via HTTP GET | Source API (port 5000) | `data/*.json` (21 files) |
| `transform.py` | Applies mappings to convert source values to Jira values | `data/issues.json` + `mappings.py` | `data/transformed_issues.json` |
| `jira_payload.py` | Converts transformed data to Jira REST API v3 format with ADF | `data/transformed_issues.json` | `data/jira_payload.json` |
| `load_to_jira.py` | POSTs each issue to Jira Cloud REST API | `data/jira_payload.json` | Issues created in Jira |

### Execution Order

```
1. xyz_api.py        (start and keep running)
2. check.py          (run once to discover Jira config)
3. mappings.py       (edit based on check.py output)
4. extract.py        (run to pull data)
5. transform.py      (run to apply mappings)
6. jira_payload.py   (run to format for Jira)
7. load_to_jira.py   (run to push to Jira)
```

---

## API Endpoints

### Source System Endpoints (xyz_api.py)

| Endpoint | Method | Description | Filter Support |
|---|---|---|---|
| `/` | GET | API documentation | — |
| `/projects` | GET | All projects | — |
| `/projects/<key>` | GET | Single project | — |
| `/users` | GET | All users | `?active=true` |
| `/roles` | GET | Custom roles | — |
| `/issue-types` | GET | Issue type definitions | — |
| `/statuses` | GET | Custom status definitions | — |
| `/priorities` | GET | Custom priority definitions | — |
| `/resolutions` | GET | Resolution definitions | — |
| `/components` | GET | Components | `?project_key=BANK` |
| `/versions` | GET | Versions/releases | `?project_key=BANK` |
| `/sprints` | GET | Sprints | `?project_key=BANK&state=active` |
| `/labels` | GET | Labels | — |
| `/custom-fields` | GET | Custom field definitions | — |
| `/issues` | GET | All issues | `?project_key=&status=&type=&assignee=&priority=` |
| `/issues/<id>` | GET | Single issue with nested data | — |
| `/comments` | GET | All comments | `?issue_id=1007` |
| `/links` | GET | Issue links | — |
| `/worklogs` | GET | Time logs | `?issue_id=&user=` |
| `/attachments` | GET | Attachment metadata | `?issue_id=1007` |
| `/boards` | GET | Boards | — |
| `/workflows` | GET | Workflow definitions | — |
| `/changelogs` | GET | Issue history | `?issue_id=1007` |
| `/migration-summary` | GET | Stats for planning | — |

---

## Mapping Reference

### Priority Mapping

| Source (Custom) | → | Jira |
|---|---|---|
| Showstopper | → | Critical |
| Urgent | → | Highest |
| High_Priority | → | High |
| Medium_Priority | → | Medium |
| Normal | → | Medium |
| Low_Priority | → | Low |
| Nice_To_Have | → | Lowest |
| Backlog_Priority | → | Lowest |
| Deferred | → | Lowest |
| Unprioritized | → | Medium |

### Status Mapping

| Source (Custom) | → | Jira |
|---|---|---|
| New | → | To Do |
| Open | → | To Do |
| In_Analysis | → | In Progress |
| Ready_For_Dev | → | To Do |
| In_Development | → | In Progress |
| Code_Review | → | In Progress |
| Ready_For_QA | → | To Do |
| In_QA | → | In Progress |
| QA_Failed | → | To Do |
| Ready_For_UAT | → | To Do |
| In_UAT | → | In Progress |
| Approved | → | Done |
| Done | → | Done |
| Closed | → | Done |
| On_Hold | → | To Do |
| Cancelled | → | Done |

### Issue Type Mapping

| Source (Custom) | → | Jira |
|---|---|---|
| Epic | → | Epic |
| Story | → | Story |
| Task | → | Task |
| Bug | → | Bug |
| Sub-task | → | Sub-task |
| Spike | → | Task |
| Change_Request | → | Story |
| Tech_Debt | → | Task |
| Improvement | → | Story |
| Incident | → | Bug |
| Service_Request | → | Task |
| Test_Case | → | Task |

### Project Mapping

| Source Key | → | Jira Key |
|---|---|---|
| BANK | → | BANK |
| ECOM | → | BANK |
| HRM | → | BANK |
| CRM | → | BANK |
| DEVOPS | → | BANK |
| MOB | → | MOB |
| DATA | → | BANK |
| SEC | → | BANK |
| QA | → | BANK |
| CLOUD | → | BANK |

---

## Sample Data Overview

| Entity | Count | Details |
|---|---|---|
| **Projects** | 10 | BANK, ECOM, HRM, CRM, DEVOPS, MOB, DATA, SEC, QA, CLOUD |
| **Users** | 15 | 14 active, 1 inactive (bob) |
| **Roles** | 13 | tech_lead, senior_dev, junior_dev, etc. |
| **Issue Types** | 12 | 5 standard + 7 custom needing mapping |
| **Statuses** | 16 | All custom, mapped to To Do / In Progress / Done |
| **Priorities** | 10 | Mapped to Jira's 7 priorities |
| **Resolutions** | 10 | Fixed, Wont_Fix, Duplicate_Issue, etc. |
| **Components** | 12 | Across multiple projects |
| **Versions** | 15 | Released, in-progress, planned |
| **Sprints** | 15 | Completed, active, planned |
| **Issues** | 50 | Epics, stories, bugs, tasks with hierarchy |
| **Comments** | 25 | Across multiple issues |
| **Links** | 15 | blocks, depends_on, is_related_to, etc. |
| **Worklogs** | 20 | Time entries by various users |
| **Attachments** | 10 | Metadata only (screenshots, PDFs, logs) |
| **Boards** | 10 | Scrum and Kanban boards |
| **Workflows** | 3 | Dev workflow, Bug workflow, Ops workflow |
| **Changelogs** | 15 | Status changes, priority changes, reassignments |

---

## Troubleshooting

### Error: `ModuleNotFoundError: No module named 'flask'`

```bash
pip3 install flask requests
# OR if using virtual environment
source venv/bin/activate
pip install flask requests
```

### Error: `Connection refused` during extraction

```
Make sure xyz_api.py is running in another terminal.
```

```bash
# Terminal 1
python3 xyz_api.py

# Terminal 2
python3 extract.py
```

### Error: `description must be Atlassian Document Format`

```
Your jira_payload.py must convert plain text to ADF format.
Make sure the text_to_adf() function is present.
```

### Error: `valid project is required`

```
The project key in your payload doesn't exist in your Jira.
Run check.py to see available projects and update PROJECT_MAP in mappings.py.
```

### Error: `Specify a valid issue type`

```
The issue type name doesn't match your Jira's issue types.
Run check.py to see available types and update ISSUE_TYPE_MAP in mappings.py.
```

### Error: `401 Unauthorized`

```
Check your JIRA_URL, EMAIL, and API_TOKEN in load_to_jira.py.
Make sure the API token is valid and not expired.
```

### How to check what's in Jira

```bash
python3 check.py
```

### How to verify extracted data

```bash
cat data/issues.json | python3 -m json.tool | head -50
```

### How to verify transformed data

```bash
cat data/transformed_issues.json | python3 -m json.tool | head -50
```

### How to verify payload

```bash
cat data/jira_payload.json | python3 -m json.tool | head -50
```

---

## Notes

- **Status is NOT set via issue creation** — Jira creates all issues in the default status (usually "To Do"). To set status, you need to use the **transition API** after creation, which is not covered in this basic pipeline.

- **Sub-tasks require a parent** — Jira requires sub-tasks to have a parent issue ID. The current pipeline creates them as standalone `Task` type to avoid errors.

- **Attachments are metadata only** — The source API stores attachment metadata (filename, size). Actual file upload to Jira requires the attachment upload API.

- **Comments and worklogs are NOT loaded** — The current `load_to_jira.py` only creates issues. Loading comments and worklogs requires separate API calls after issue creation.

- **Rate limiting** — Jira Cloud has API rate limits. For large migrations, add delays between requests:

  ```python
  import time
  time.sleep(1)  # 1 second delay between API calls
  ```

- **Idempotency** — Running `load_to_jira.py` multiple times will create **duplicate issues**. There is no duplicate detection in this basic pipeline.

---

## Quick Start (TL;DR)

```bash
# Terminal 1: Start source API
cd ~/project-api
source venv/bin/activate
python3 xyz_api.py

# Terminal 2: Run migration
cd ~/project-api/migration_project
source ../venv/bin/activate

python3 check.py              # See what's in your Jira
# Edit mappings.py             # Update mappings based on check.py output
python3 extract.py             # Pull data from source
python3 transform.py           # Apply mappings
python3 jira_payload.py        # Convert to Jira format
python3 load_to_jira.py        # Push to Jira
```

---
