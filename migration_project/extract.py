import requests
import os
import json

BASE_URL = "http://127.0.0.1:5000"

ENDPOINTS = [
    "projects",
    "users",
    "roles",             
    "issue-types",
    "issues",
    "comments",
    "links",
    "worklogs",
    "sprints",
    "versions",
    "components",
    "labels",            
    "priorities",
    "statuses",
    "resolutions",
    "custom-fields",
    "boards",
    "workflows",
    "attachments",
    "changelogs",
    "migration-summary"  
]

DATA_DIR = "data"

os.makedirs(DATA_DIR, exist_ok=True)

def fetch_and_save(endpoint):
    url = f"{BASE_URL}/{endpoint}"
    print(f"Fetching {endpoint}...")

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        file_path = os.path.join(DATA_DIR, f"{endpoint}.json")
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

        print(f"Saved {endpoint}.json")

    except Exception as e:
        print(f"Error fetching {endpoint}: {e}")


if __name__ == "__main__":
    for ep in ENDPOINTS:
        fetch_and_save(ep)

    print("✅ Extraction Completed")