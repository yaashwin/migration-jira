from flask import Flask, jsonify, request

app = Flask(__name__)

# =============================================================================
# PROJECTS (10 projects with custom fields needing mapping)
# =============================================================================
projects = [
    {"id": 1, "key": "BANK", "name": "Banking Application", "lead": "rahul", "category": "Finance", "project_type": "software", "description": "Core banking platform"},
    {"id": 2, "key": "ECOM", "name": "E-Commerce Platform", "lead": "john", "category": "Retail", "project_type": "software", "description": "Online shopping platform"},
    {"id": 3, "key": "HRM", "name": "HR Management System", "lead": "priya", "category": "Internal Tools", "project_type": "business", "description": "Employee management"},
    {"id": 4, "key": "CRM", "name": "Customer Relationship Mgmt", "lead": "alex", "category": "Sales", "project_type": "software", "description": "Customer tracking system"},
    {"id": 5, "key": "DEVOPS", "name": "DevOps Pipeline", "lead": "mike", "category": "Infrastructure", "project_type": "ops", "description": "CI/CD automation"},
    {"id": 6, "key": "MOB", "name": "Mobile App", "lead": "sarah", "category": "Mobile", "project_type": "software", "description": "iOS and Android app"},
    {"id": 7, "key": "DATA", "name": "Data Analytics Engine", "lead": "chen", "category": "Data", "project_type": "research", "description": "Big data processing"},
    {"id": 8, "key": "SEC", "name": "Security Audit Tool", "lead": "fatima", "category": "Security", "project_type": "compliance", "description": "Vulnerability scanning"},
    {"id": 9, "key": "QA", "name": "QA Automation Framework", "lead": "james", "category": "Quality", "project_type": "testing", "description": "Test automation suite"},
    {"id": 10, "key": "CLOUD", "name": "Cloud Migration Project", "lead": "anita", "category": "Infrastructure", "project_type": "ops", "description": "On-prem to cloud migration"},
]

# =============================================================================
# USERS (15 users with custom roles needing mapping)
# =============================================================================
users = [
    {"id": 1, "username": "rahul", "full_name": "Rahul Sharma", "email": "rahul@company.com", "role": "tech_lead", "department": "Engineering", "active": True},
    {"id": 2, "username": "john", "full_name": "John Smith", "email": "john@company.com", "role": "senior_dev", "department": "Engineering", "active": True},
    {"id": 3, "username": "priya", "full_name": "Priya Patel", "email": "priya@company.com", "role": "project_manager", "department": "Management", "active": True},
    {"id": 4, "username": "alex", "full_name": "Alex Johnson", "email": "alex@company.com", "role": "business_analyst", "department": "Product", "active": True},
    {"id": 5, "username": "mike", "full_name": "Mike Brown", "email": "mike@company.com", "role": "devops_engineer", "department": "Infrastructure", "active": True},
    {"id": 6, "username": "sarah", "full_name": "Sarah Wilson", "email": "sarah@company.com", "role": "junior_dev", "department": "Engineering", "active": True},
    {"id": 7, "username": "chen", "full_name": "Chen Wei", "email": "chen@company.com", "role": "data_engineer", "department": "Data", "active": True},
    {"id": 8, "username": "fatima", "full_name": "Fatima Al-Hassan", "email": "fatima@company.com", "role": "security_analyst", "department": "Security", "active": True},
    {"id": 9, "username": "james", "full_name": "James Taylor", "email": "james@company.com", "role": "qa_lead", "department": "Quality", "active": True},
    {"id": 10, "username": "anita", "full_name": "Anita Desai", "email": "anita@company.com", "role": "architect", "department": "Engineering", "active": True},
    {"id": 11, "username": "bob", "full_name": "Bob Garcia", "email": "bob@company.com", "role": "senior_dev", "department": "Engineering", "active": False},
    {"id": 12, "username": "lisa", "full_name": "Lisa Anderson", "email": "lisa@company.com", "role": "ux_designer", "department": "Design", "active": True},
    {"id": 13, "username": "kumar", "full_name": "Kumar Rajan", "email": "kumar@company.com", "role": "junior_dev", "department": "Engineering", "active": True},
    {"id": 14, "username": "emma", "full_name": "Emma Davis", "email": "emma@company.com", "role": "scrum_master", "department": "Management", "active": True},
    {"id": 15, "username": "david", "full_name": "David Kim", "email": "david@company.com", "role": "dba", "department": "Data", "active": True},
]

# =============================================================================
# CUSTOM ROLES (need mapping to Jira roles)
# =============================================================================
roles = [
    {"id": 1, "name": "tech_lead", "description": "Technical Lead"},
    {"id": 2, "name": "senior_dev", "description": "Senior Developer"},
    {"id": 3, "name": "junior_dev", "description": "Junior Developer"},
    {"id": 4, "name": "project_manager", "description": "Project Manager"},
    {"id": 5, "name": "business_analyst", "description": "Business Analyst"},
    {"id": 6, "name": "devops_engineer", "description": "DevOps Engineer"},
    {"id": 7, "name": "data_engineer", "description": "Data Engineer"},
    {"id": 8, "name": "security_analyst", "description": "Security Analyst"},
    {"id": 9, "name": "qa_lead", "description": "QA Lead"},
    {"id": 10, "name": "architect", "description": "Solution Architect"},
    {"id": 11, "name": "ux_designer", "description": "UX Designer"},
    {"id": 12, "name": "scrum_master", "description": "Scrum Master"},
    {"id": 13, "name": "dba", "description": "Database Administrator"},
]

# =============================================================================
# ISSUE TYPES (custom types needing mapping to Jira issue types)
# =============================================================================
issue_types = [
    {"id": 1, "name": "Epic", "description": "Large body of work", "icon": "epic.png", "subtask": False},
    {"id": 2, "name": "Story", "description": "User story", "icon": "story.png", "subtask": False},
    {"id": 3, "name": "Task", "description": "General task", "icon": "task.png", "subtask": False},
    {"id": 4, "name": "Bug", "description": "Software defect", "icon": "bug.png", "subtask": False},
    {"id": 5, "name": "Sub-task", "description": "Child task", "icon": "subtask.png", "subtask": True},
    {"id": 6, "name": "Spike", "description": "Research/investigation", "icon": "spike.png", "subtask": False},
    {"id": 7, "name": "Change_Request", "description": "Change request from client", "icon": "cr.png", "subtask": False},
    {"id": 8, "name": "Improvement", "description": "Enhancement to existing feature", "icon": "improve.png", "subtask": False},
    {"id": 9, "name": "Tech_Debt", "description": "Technical debt item", "icon": "debt.png", "subtask": False},
    {"id": 10, "name": "Incident", "description": "Production incident", "icon": "incident.png", "subtask": False},
    {"id": 11, "name": "Service_Request", "description": "Internal service request", "icon": "sr.png", "subtask": False},
    {"id": 12, "name": "Test_Case", "description": "Test case definition", "icon": "test.png", "subtask": False},
]

# =============================================================================
# CUSTOM STATUSES (need mapping to Jira workflow statuses)
# =============================================================================
statuses = [
    {"id": 1, "name": "New", "category": "new", "description": "Newly created"},
    {"id": 2, "name": "Open", "category": "open", "description": "Acknowledged and open"},
    {"id": 3, "name": "In_Analysis", "category": "in_progress", "description": "Being analyzed"},
    {"id": 4, "name": "Ready_For_Dev", "category": "ready", "description": "Ready to be picked up"},
    {"id": 5, "name": "In_Development", "category": "in_progress", "description": "Actively being developed"},
    {"id": 6, "name": "Code_Review", "category": "in_progress", "description": "Under code review"},
    {"id": 7, "name": "Ready_For_QA", "category": "ready", "description": "Ready for testing"},
    {"id": 8, "name": "In_QA", "category": "in_progress", "description": "Being tested"},
    {"id": 9, "name": "QA_Failed", "category": "blocked", "description": "Testing failed"},
    {"id": 10, "name": "Ready_For_UAT", "category": "ready", "description": "Ready for user acceptance"},
    {"id": 11, "name": "In_UAT", "category": "in_progress", "description": "User acceptance testing"},
    {"id": 12, "name": "Approved", "category": "done", "description": "Approved by stakeholder"},
    {"id": 13, "name": "Done", "category": "done", "description": "Completed"},
    {"id": 14, "name": "Closed", "category": "closed", "description": "Closed and archived"},
    {"id": 15, "name": "On_Hold", "category": "blocked", "description": "Paused"},
    {"id": 16, "name": "Cancelled", "category": "closed", "description": "Will not be done"},
]

# =============================================================================
# CUSTOM PRIORITIES (need mapping to Jira priorities)
# =============================================================================
priorities = [
    {"id": 1, "name": "Showstopper", "color": "#FF0000", "order": 1},
    {"id": 2, "name": "Urgent", "color": "#FF4500", "order": 2},
    {"id": 3, "name": "High_Priority", "color": "#FF8C00", "order": 3},
    {"id": 4, "name": "Medium_Priority", "color": "#FFD700", "order": 4},
    {"id": 5, "name": "Normal", "color": "#32CD32", "order": 5},
    {"id": 6, "name": "Low_Priority", "color": "#4169E1", "order": 6},
    {"id": 7, "name": "Nice_To_Have", "color": "#808080", "order": 7},
    {"id": 8, "name": "Backlog_Priority", "color": "#D3D3D3", "order": 8},
    {"id": 9, "name": "Deferred", "color": "#A9A9A9", "order": 9},
    {"id": 10, "name": "Unprioritized", "color": "#FFFFFF", "order": 10},
]

# =============================================================================
# RESOLUTIONS (need mapping to Jira resolutions)
# =============================================================================
resolutions = [
    {"id": 1, "name": "Fixed", "description": "Issue was fixed"},
    {"id": 2, "name": "Wont_Fix", "description": "Decision not to fix"},
    {"id": 3, "name": "Duplicate_Issue", "description": "Duplicate of another issue"},
    {"id": 4, "name": "Cannot_Reproduce", "description": "Cannot replicate the issue"},
    {"id": 5, "name": "Not_A_Bug", "description": "Working as designed"},
    {"id": 6, "name": "Done_Complete", "description": "Work completed successfully"},
    {"id": 7, "name": "Incomplete_Info", "description": "Not enough information provided"},
    {"id": 8, "name": "Out_Of_Scope", "description": "Outside project scope"},
    {"id": 9, "name": "Workaround_Applied", "description": "Temporary workaround in place"},
    {"id": 10, "name": "Third_Party_Issue", "description": "Issue with external dependency"},
]

# =============================================================================
# COMPONENTS (12 components across projects)
# =============================================================================
components = [
    {"id": 1, "name": "Authentication", "project_key": "BANK", "lead": "rahul", "description": "Login and auth module"},
    {"id": 2, "name": "Payments", "project_key": "BANK", "lead": "john", "description": "Payment processing"},
    {"id": 3, "name": "Account_Mgmt", "project_key": "BANK", "lead": "anita", "description": "Account management"},
    {"id": 4, "name": "Shopping_Cart", "project_key": "ECOM", "lead": "sarah", "description": "Cart functionality"},
    {"id": 5, "name": "Product_Catalog", "project_key": "ECOM", "lead": "alex", "description": "Product listing"},
    {"id": 6, "name": "Order_Processing", "project_key": "ECOM", "lead": "john", "description": "Order management"},
    {"id": 7, "name": "Employee_Portal", "project_key": "HRM", "lead": "priya", "description": "Employee self-service"},
    {"id": 8, "name": "Payroll", "project_key": "HRM", "lead": "kumar", "description": "Salary processing"},
    {"id": 9, "name": "CI_Pipeline", "project_key": "DEVOPS", "lead": "mike", "description": "Continuous integration"},
    {"id": 10, "name": "Monitoring", "project_key": "DEVOPS", "lead": "mike", "description": "System monitoring"},
    {"id": 11, "name": "Push_Notifications", "project_key": "MOB", "lead": "sarah", "description": "Mobile push notifications"},
    {"id": 12, "name": "Data_Pipeline", "project_key": "DATA", "lead": "chen", "description": "ETL pipelines"},
]

# =============================================================================
# VERSIONS / RELEASES (15 versions across projects)
# =============================================================================
versions = [
    {"id": 1, "name": "Release 1.0", "project_key": "BANK", "status": "released", "release_date": "2024-01-15", "description": "Initial release"},
    {"id": 2, "name": "Release 2.0", "project_key": "BANK", "status": "released", "release_date": "2024-04-01", "description": "Major update"},
    {"id": 3, "name": "Release 2.1-hotfix", "project_key": "BANK", "status": "released", "release_date": "2024-04-15", "description": "Hotfix for 2.0"},
    {"id": 4, "name": "Release 3.0", "project_key": "BANK", "status": "in_progress", "release_date": "2024-09-01", "description": "Next major version"},
    {"id": 5, "name": "v1.0-beta", "project_key": "ECOM", "status": "released", "release_date": "2024-02-01", "description": "Beta launch"},
    {"id": 6, "name": "v1.0-GA", "project_key": "ECOM", "status": "released", "release_date": "2024-03-15", "description": "General availability"},
    {"id": 7, "name": "v2.0-planned", "project_key": "ECOM", "status": "planned", "release_date": "2024-10-01", "description": "Version 2 planning"},
    {"id": 8, "name": "HRM-Phase1", "project_key": "HRM", "status": "released", "release_date": "2024-05-01", "description": "Phase 1 delivery"},
    {"id": 9, "name": "HRM-Phase2", "project_key": "HRM", "status": "in_progress", "release_date": "2024-08-01", "description": "Phase 2 delivery"},
    {"id": 10, "name": "DevOps-v1", "project_key": "DEVOPS", "status": "released", "release_date": "2024-01-01", "description": "Initial pipeline"},
    {"id": 11, "name": "MOB-1.0", "project_key": "MOB", "status": "released", "release_date": "2024-06-01", "description": "App store release"},
    {"id": 12, "name": "MOB-1.1", "project_key": "MOB", "status": "in_progress", "release_date": "2024-07-15", "description": "Bug fixes"},
    {"id": 13, "name": "DATA-alpha", "project_key": "DATA", "status": "in_progress", "release_date": "2024-09-01", "description": "Alpha release"},
    {"id": 14, "name": "SEC-audit-v1", "project_key": "SEC", "status": "released", "release_date": "2024-03-01", "description": "First audit cycle"},
    {"id": 15, "name": "CLOUD-wave1", "project_key": "CLOUD", "status": "in_progress", "release_date": "2024-12-01", "description": "First migration wave"},
]

# =============================================================================
# SPRINTS (15 sprints across projects with custom fields)
# =============================================================================
sprints = [
    {"id": 1, "name": "BANK Sprint 1", "project_key": "BANK", "state": "completed", "start_date": "2024-01-01", "end_date": "2024-01-14", "goal": "Core login system"},
    {"id": 2, "name": "BANK Sprint 2", "project_key": "BANK", "state": "completed", "start_date": "2024-01-15", "end_date": "2024-01-28", "goal": "Payment integration"},
    {"id": 3, "name": "BANK Sprint 3", "project_key": "BANK", "state": "active", "start_date": "2024-01-29", "end_date": "2024-02-11", "goal": "Account management"},
    {"id": 4, "name": "BANK Sprint 4", "project_key": "BANK", "state": "planned", "start_date": "2024-02-12", "end_date": "2024-02-25", "goal": "Reporting module"},
    {"id": 5, "name": "ECOM Sprint 1", "project_key": "ECOM", "state": "completed", "start_date": "2024-02-01", "end_date": "2024-02-14", "goal": "Product catalog"},
    {"id": 6, "name": "ECOM Sprint 2", "project_key": "ECOM", "state": "completed", "start_date": "2024-02-15", "end_date": "2024-02-28", "goal": "Shopping cart"},
    {"id": 7, "name": "ECOM Sprint 3", "project_key": "ECOM", "state": "active", "start_date": "2024-03-01", "end_date": "2024-03-14", "goal": "Checkout flow"},
    {"id": 8, "name": "HRM Sprint 1", "project_key": "HRM", "state": "completed", "start_date": "2024-03-01", "end_date": "2024-03-14", "goal": "Employee onboarding"},
    {"id": 9, "name": "HRM Sprint 2", "project_key": "HRM", "state": "active", "start_date": "2024-03-15", "end_date": "2024-03-28", "goal": "Payroll processing"},
    {"id": 10, "name": "MOB Sprint 1", "project_key": "MOB", "state": "completed", "start_date": "2024-04-01", "end_date": "2024-04-14", "goal": "App skeleton"},
    {"id": 11, "name": "MOB Sprint 2", "project_key": "MOB", "state": "active", "start_date": "2024-04-15", "end_date": "2024-04-28", "goal": "Push notifications"},
    {"id": 12, "name": "DEVOPS Sprint 1", "project_key": "DEVOPS", "state": "completed", "start_date": "2024-01-01", "end_date": "2024-01-14", "goal": "Jenkins setup"},
    {"id": 13, "name": "DATA Sprint 1", "project_key": "DATA", "state": "active", "start_date": "2024-05-01", "end_date": "2024-05-14", "goal": "Spark pipeline"},
    {"id": 14, "name": "SEC Sprint 1", "project_key": "SEC", "state": "completed", "start_date": "2024-02-01", "end_date": "2024-02-14", "goal": "Vulnerability scan"},
    {"id": 15, "name": "CLOUD Sprint 1", "project_key": "CLOUD", "state": "planned", "start_date": "2024-06-01", "end_date": "2024-06-14", "goal": "AWS setup"},
]

# =============================================================================
# LABELS (custom labels needing mapping)
# =============================================================================
labels = [
    {"id": 1, "name": "frontend"},
    {"id": 2, "name": "backend"},
    {"id": 3, "name": "api"},
    {"id": 4, "name": "database"},
    {"id": 5, "name": "security"},
    {"id": 6, "name": "performance"},
    {"id": 7, "name": "ui-ux"},
    {"id": 8, "name": "critical-path"},
    {"id": 9, "name": "tech-debt"},
    {"id": 10, "name": "customer-reported"},
    {"id": 11, "name": "regression"},
    {"id": 12, "name": "documentation"},
]

# =============================================================================
# CUSTOM FIELDS DEFINITIONS (need mapping to Jira custom fields)
# =============================================================================
custom_field_definitions = [
    {"id": "cf_001", "name": "Business_Value", "type": "number", "description": "Business value score 1-100"},
    {"id": "cf_002", "name": "Risk_Level", "type": "select", "options": ["Low", "Medium", "High", "Critical"], "description": "Risk assessment"},
    {"id": "cf_003", "name": "Story_Points_Custom", "type": "number", "description": "Story point estimate"},
    {"id": "cf_004", "name": "Environment_Found", "type": "select", "options": ["DEV", "QA", "STAGING", "PROD"], "description": "Environment where issue found"},
    {"id": "cf_005", "name": "Customer_Impact", "type": "select", "options": ["None", "Low", "Medium", "High", "Severe"], "description": "Impact on customers"},
    {"id": "cf_006", "name": "Target_Release", "type": "text", "description": "Target release version"},
    {"id": "cf_007", "name": "External_Reference", "type": "text", "description": "External ticket/reference ID"},
    {"id": "cf_008", "name": "Team_Name", "type": "select", "options": ["Alpha", "Beta", "Gamma", "Delta", "Platform"], "description": "Owning team"},
    {"id": "cf_009", "name": "Estimated_Days", "type": "number", "description": "Estimated days to complete"},
    {"id": "cf_010", "name": "Regression_Flag", "type": "boolean", "description": "Is this a regression"},
]

# =============================================================================
# ISSUES (50 issues with rich data, hierarchy, custom fields)
# =============================================================================
issues = [
    # ======================== BANK PROJECT ========================
    # EPIC 1: Login System
    {
        "id": 1001, "key": "BANK-1", "title": "Build login system",
        "type": "Epic", "status": "In_Development", "priority": "High_Priority",
        "assignee": "rahul", "reporter": "priya",
        "project_key": "BANK", "component": "Authentication",
        "version_fixed": "Release 2.0", "version_affected": None,
        "sprint": "BANK Sprint 1", "labels": ["backend", "security"],
        "created_date": "2024-01-02", "updated_date": "2024-01-20",
        "due_date": "2024-02-28", "resolution": None, "parent": None,
        "description": "Implement complete authentication system with OAuth2 and MFA support",
        "custom_fields": {"cf_001": 95, "cf_002": "High", "cf_003": 40, "cf_008": "Alpha", "cf_009": 30}
    },
    # Stories under Epic 1
    {
        "id": 1002, "key": "BANK-2", "title": "Create login page UI",
        "type": "Story", "status": "Done", "priority": "High_Priority",
        "assignee": "sarah", "reporter": "alex",
        "project_key": "BANK", "component": "Authentication",
        "version_fixed": "Release 1.0", "version_affected": None,
        "sprint": "BANK Sprint 1", "labels": ["frontend", "ui-ux"],
        "created_date": "2024-01-03", "updated_date": "2024-01-12",
        "due_date": "2024-01-14", "resolution": "Done_Complete", "parent": 1001,
        "description": "Design and implement responsive login page",
        "custom_fields": {"cf_001": 80, "cf_002": "Medium", "cf_003": 8, "cf_008": "Alpha", "cf_009": 5}
    },
    {
        "id": 1003, "key": "BANK-3", "title": "Implement JWT token service",
        "type": "Story", "status": "Code_Review", "priority": "High_Priority",
        "assignee": "john", "reporter": "rahul",
        "project_key": "BANK", "component": "Authentication",
        "version_fixed": "Release 2.0", "version_affected": None,
        "sprint": "BANK Sprint 2", "labels": ["backend", "api", "security"],
        "created_date": "2024-01-05", "updated_date": "2024-01-25",
        "due_date": "2024-01-28", "resolution": None, "parent": 1001,
        "description": "Build JWT-based token issuance, refresh, and validation",
        "custom_fields": {"cf_001": 90, "cf_002": "High", "cf_003": 13, "cf_008": "Alpha", "cf_009": 8}
    },
    {
        "id": 1004, "key": "BANK-4", "title": "Add multi-factor authentication",
        "type": "Story", "status": "Ready_For_Dev", "priority": "Urgent",
        "assignee": "john", "reporter": "priya",
        "project_key": "BANK", "component": "Authentication",
        "version_fixed": "Release 3.0", "version_affected": None,
        "sprint": "BANK Sprint 3", "labels": ["backend", "security"],
        "created_date": "2024-01-10", "updated_date": "2024-01-29",
        "due_date": "2024-02-11", "resolution": None, "parent": 1001,
        "description": "Implement TOTP and SMS-based MFA",
        "custom_fields": {"cf_001": 85, "cf_002": "Critical", "cf_003": 21, "cf_008": "Alpha", "cf_009": 12}
    },
    # Sub-tasks under BANK-2
    {
        "id": 1005, "key": "BANK-5", "title": "Design login mockup in Figma",
        "type": "Sub-task", "status": "Done", "priority": "Medium_Priority",
        "assignee": "lisa", "reporter": "sarah",
        "project_key": "BANK", "component": "Authentication",
        "version_fixed": "Release 1.0", "version_affected": None,
        "sprint": "BANK Sprint 1", "labels": ["ui-ux"],
        "created_date": "2024-01-03", "updated_date": "2024-01-05",
        "due_date": "2024-01-06", "resolution": "Done_Complete", "parent": 1002,
        "description": "Create Figma mockup for login, registration, forgot password",
        "custom_fields": {"cf_001": 60, "cf_003": 3, "cf_008": "Alpha", "cf_009": 2}
    },
    {
        "id": 1006, "key": "BANK-6", "title": "Implement login form HTML/CSS",
        "type": "Sub-task", "status": "Done", "priority": "Medium_Priority",
        "assignee": "sarah", "reporter": "sarah",
        "project_key": "BANK", "component": "Authentication",
        "version_fixed": "Release 1.0", "version_affected": None,
        "sprint": "BANK Sprint 1", "labels": ["frontend"],
        "created_date": "2024-01-06", "updated_date": "2024-01-10",
        "due_date": "2024-01-10", "resolution": "Done_Complete", "parent": 1002,
        "description": "Code the login form with validation",
        "custom_fields": {"cf_001": 70, "cf_003": 5, "cf_008": "Alpha", "cf_009": 3}
    },
    # Bugs in BANK
    {
        "id": 1007, "key": "BANK-7", "title": "Login fails with special chars in password",
        "type": "Bug", "status": "In_QA", "priority": "Showstopper",
        "assignee": "john", "reporter": "james",
        "project_key": "BANK", "component": "Authentication",
        "version_fixed": "Release 2.1-hotfix", "version_affected": "Release 2.0",
        "sprint": "BANK Sprint 3", "labels": ["security", "regression", "customer-reported"],
        "created_date": "2024-01-28", "updated_date": "2024-02-01",
        "due_date": "2024-02-03", "resolution": None, "parent": None,
        "description": "Users with passwords containing &, <, > cannot login. SQL injection vector possible.",
        "custom_fields": {"cf_001": 100, "cf_002": "Critical", "cf_004": "PROD", "cf_005": "Severe", "cf_008": "Alpha", "cf_010": True}
    },
    {
        "id": 1008, "key": "BANK-8", "title": "Session timeout not working correctly",
        "type": "Bug", "status": "Open", "priority": "High_Priority",
        "assignee": "rahul", "reporter": "fatima",
        "project_key": "BANK", "component": "Authentication",
        "version_fixed": None, "version_affected": "Release 2.0",
        "sprint": "BANK Sprint 3", "labels": ["backend", "security"],
        "created_date": "2024-01-30", "updated_date": "2024-01-30",
        "due_date": "2024-02-05", "resolution": None, "parent": None,
        "description": "Session stays alive beyond 30 min timeout, security risk",
        "custom_fields": {"cf_001": 85, "cf_002": "High", "cf_004": "QA", "cf_005": "High", "cf_008": "Alpha", "cf_010": False}
    },
    # EPIC 2: Payments
    {
        "id": 1009, "key": "BANK-9", "title": "Build payment processing engine",
        "type": "Epic", "status": "In_Analysis", "priority": "Urgent",
        "assignee": "anita", "reporter": "priya",
        "project_key": "BANK", "component": "Payments",
        "version_fixed": "Release 3.0", "version_affected": None,
        "sprint": None, "labels": ["backend", "critical-path"],
        "created_date": "2024-01-15", "updated_date": "2024-01-29",
        "due_date": "2024-06-30", "resolution": None, "parent": None,
        "description": "Complete payment processing with multiple gateway support",
        "custom_fields": {"cf_001": 100, "cf_002": "Critical", "cf_003": 100, "cf_008": "Beta", "cf_009": 60}
    },
    {
        "id": 1010, "key": "BANK-10", "title": "Integrate Stripe payment gateway",
        "type": "Story", "status": "In_Analysis", "priority": "High_Priority",
        "assignee": "kumar", "reporter": "anita",
        "project_key": "BANK", "component": "Payments",
        "version_fixed": "Release 3.0", "version_affected": None,
        "sprint": "BANK Sprint 4", "labels": ["backend", "api"],
        "created_date": "2024-01-20", "updated_date": "2024-01-29",
        "due_date": "2024-03-15", "resolution": None, "parent": 1009,
        "description": "Integrate Stripe API for card payments",
        "custom_fields": {"cf_001": 90, "cf_002": "High", "cf_003": 21, "cf_007": "STRIPE-INT-2024", "cf_008": "Beta", "cf_009": 15}
    },

    # ======================== ECOM PROJECT ========================
    # EPIC: Product Catalog
    {
        "id": 2001, "key": "ECOM-1", "title": "Build product catalog system",
        "type": "Epic", "status": "In_Development", "priority": "High_Priority",
        "assignee": "john", "reporter": "alex",
        "project_key": "ECOM", "component": "Product_Catalog",
        "version_fixed": "v1.0-GA", "version_affected": None,
        "sprint": "ECOM Sprint 1", "labels": ["backend", "frontend"],
        "created_date": "2024-02-01", "updated_date": "2024-02-20",
        "due_date": "2024-03-15", "resolution": None, "parent": None,
        "description": "Full product catalog with categories, search, and filtering",
        "custom_fields": {"cf_001": 95, "cf_002": "High", "cf_003": 55, "cf_008": "Beta", "cf_009": 40}
    },
    {
        "id": 2002, "key": "ECOM-2", "title": "Product listing page with filters",
        "type": "Story", "status": "Done", "priority": "High_Priority",
        "assignee": "sarah", "reporter": "alex",
        "project_key": "ECOM", "component": "Product_Catalog",
        "version_fixed": "v1.0-beta", "version_affected": None,
        "sprint": "ECOM Sprint 1", "labels": ["frontend", "ui-ux"],
        "created_date": "2024-02-02", "updated_date": "2024-02-13",
        "due_date": "2024-02-14", "resolution": "Done_Complete", "parent": 2001,
        "description": "Create product listing page with category and price filters",
        "custom_fields": {"cf_001": 85, "cf_002": "Medium", "cf_003": 13, "cf_008": "Beta", "cf_009": 8}
    },
    {
        "id": 2003, "key": "ECOM-3", "title": "Product search API with Elasticsearch",
        "type": "Story", "status": "In_Development", "priority": "High_Priority",
        "assignee": "chen", "reporter": "john",
        "project_key": "ECOM", "component": "Product_Catalog",
        "version_fixed": "v1.0-GA", "version_affected": None,
        "sprint": "ECOM Sprint 2", "labels": ["backend", "api", "performance"],
        "created_date": "2024-02-10", "updated_date": "2024-02-25",
        "due_date": "2024-02-28", "resolution": None, "parent": 2001,
        "description": "Build product search using Elasticsearch with autocomplete",
        "custom_fields": {"cf_001": 80, "cf_002": "Medium", "cf_003": 13, "cf_008": "Beta", "cf_009": 10}
    },
    # Shopping Cart
    {
        "id": 2004, "key": "ECOM-4", "title": "Shopping cart functionality",
        "type": "Epic", "status": "In_Development", "priority": "Urgent",
        "assignee": "sarah", "reporter": "alex",
        "project_key": "ECOM", "component": "Shopping_Cart",
        "version_fixed": "v1.0-GA", "version_affected": None,
        "sprint": "ECOM Sprint 2", "labels": ["frontend", "backend"],
        "created_date": "2024-02-05", "updated_date": "2024-02-28",
        "due_date": "2024-03-14", "resolution": None, "parent": None,
        "description": "Complete shopping cart with add, remove, quantity update, save for later",
        "custom_fields": {"cf_001": 95, "cf_002": "High", "cf_003": 34, "cf_008": "Beta", "cf_009": 20}
    },
    {
        "id": 2005, "key": "ECOM-5", "title": "Add to cart button not responsive on mobile",
        "type": "Bug", "status": "In_Development", "priority": "High_Priority",
        "assignee": "sarah", "reporter": "james",
        "project_key": "ECOM", "component": "Shopping_Cart",
        "version_fixed": "v1.0-GA", "version_affected": "v1.0-beta",
        "sprint": "ECOM Sprint 3", "labels": ["frontend", "customer-reported"],
        "created_date": "2024-02-20", "updated_date": "2024-03-01",
        "due_date": "2024-03-05", "resolution": None, "parent": None,
        "description": "Add to cart button overlaps with product image on iPhone SE",
        "custom_fields": {"cf_001": 70, "cf_002": "Medium", "cf_004": "PROD", "cf_005": "Medium", "cf_008": "Beta", "cf_010": False}
    },
    # Spike and Tech Debt
    {
        "id": 2006, "key": "ECOM-6", "title": "Investigate CDN options for product images",
        "type": "Spike", "status": "Done", "priority": "Normal",
        "assignee": "mike", "reporter": "anita",
        "project_key": "ECOM", "component": "Product_Catalog",
        "version_fixed": None, "version_affected": None,
        "sprint": "ECOM Sprint 1", "labels": ["performance"],
        "created_date": "2024-02-03", "updated_date": "2024-02-10",
        "due_date": "2024-02-10", "resolution": "Done_Complete", "parent": None,
        "description": "Research CloudFront vs Cloudflare for image delivery",
        "custom_fields": {"cf_001": 50, "cf_002": "Low", "cf_003": 5, "cf_008": "Platform", "cf_009": 3}
    },
    {
        "id": 2007, "key": "ECOM-7", "title": "Refactor product service to use repository pattern",
        "type": "Tech_Debt", "status": "Ready_For_Dev", "priority": "Low_Priority",
        "assignee": "john", "reporter": "rahul",
        "project_key": "ECOM", "component": "Product_Catalog",
        "version_fixed": "v2.0-planned", "version_affected": None,
        "sprint": None, "labels": ["backend", "tech-debt"],
        "created_date": "2024-02-15", "updated_date": "2024-02-15",
        "due_date": None, "resolution": None, "parent": None,
        "description": "Current service layer is tightly coupled to ORM. Needs abstraction.",
        "custom_fields": {"cf_001": 30, "cf_002": "Low", "cf_003": 8, "cf_008": "Beta", "cf_009": 5}
    },

    # ======================== HRM PROJECT ========================
    {
        "id": 3001, "key": "HRM-1", "title": "Employee onboarding workflow",
        "type": "Epic", "status": "Done", "priority": "High_Priority",
        "assignee": "priya", "reporter": "priya",
        "project_key": "HRM", "component": "Employee_Portal",
        "version_fixed": "HRM-Phase1", "version_affected": None,
        "sprint": "HRM Sprint 1", "labels": ["backend", "frontend"],
        "created_date": "2024-03-01", "updated_date": "2024-03-14",
        "due_date": "2024-03-14", "resolution": "Done_Complete", "parent": None,
        "description": "Complete new employee onboarding workflow",
        "custom_fields": {"cf_001": 85, "cf_002": "Medium", "cf_003": 34, "cf_008": "Gamma", "cf_009": 20}
    },
    {
        "id": 3002, "key": "HRM-2", "title": "Build employee profile page",
        "type": "Story", "status": "Done", "priority": "Medium_Priority",
        "assignee": "kumar", "reporter": "priya",
        "project_key": "HRM", "component": "Employee_Portal",
        "version_fixed": "HRM-Phase1", "version_affected": None,
        "sprint": "HRM Sprint 1", "labels": ["frontend"],
        "created_date": "2024-03-02", "updated_date": "2024-03-10",
        "due_date": "2024-03-10", "resolution": "Done_Complete", "parent": 3001,
        "description": "Employee profile page with photo, details, department info",
        "custom_fields": {"cf_001": 70, "cf_002": "Low", "cf_003": 8, "cf_008": "Gamma", "cf_009": 5}
    },
    {
        "id": 3003, "key": "HRM-3", "title": "Payroll calculation engine",
        "type": "Story", "status": "In_Development", "priority": "Urgent",
        "assignee": "kumar", "reporter": "priya",
        "project_key": "HRM", "component": "Payroll",
        "version_fixed": "HRM-Phase2", "version_affected": None,
        "sprint": "HRM Sprint 2", "labels": ["backend", "critical-path"],
        "created_date": "2024-03-15", "updated_date": "2024-03-25",
        "due_date": "2024-03-28", "resolution": None, "parent": None,
        "description": "Build payroll engine with tax calculations, deductions, and compliance",
        "custom_fields": {"cf_001": 95, "cf_002": "High", "cf_003": 21, "cf_008": "Gamma", "cf_009": 15}
    },
    {
        "id": 3004, "key": "HRM-4", "title": "Leave management module",
        "type": "Story", "status": "In_Analysis", "priority": "Medium_Priority",
        "assignee": "sarah", "reporter": "priya",
        "project_key": "HRM", "component": "Employee_Portal",
        "version_fixed": "HRM-Phase2", "version_affected": None,
        "sprint": "HRM Sprint 2", "labels": ["backend", "frontend"],
        "created_date": "2024-03-16", "updated_date": "2024-03-20",
        "due_date": "2024-04-01", "resolution": None, "parent": None,
        "description": "Leave request, approval workflow, balance tracking",
        "custom_fields": {"cf_001": 75, "cf_002": "Medium", "cf_003": 13, "cf_008": "Gamma", "cf_009": 10}
    },
    {
        "id": 3005, "key": "HRM-5", "title": "Payslip PDF generation broken",
        "type": "Bug", "status": "QA_Failed", "priority": "Showstopper",
        "assignee": "kumar", "reporter": "emma",
        "project_key": "HRM", "component": "Payroll",
        "version_fixed": "HRM-Phase2", "version_affected": "HRM-Phase1",
        "sprint": "HRM Sprint 2", "labels": ["backend", "customer-reported", "regression"],
        "created_date": "2024-03-22", "updated_date": "2024-03-26",
        "due_date": "2024-03-28", "resolution": None, "parent": None,
        "description": "PDF generation throws NPE when employee has no bank details on file",
        "custom_fields": {"cf_001": 90, "cf_002": "Critical", "cf_004": "PROD", "cf_005": "Severe", "cf_008": "Gamma", "cf_010": True}
    },

    # ======================== DEVOPS PROJECT ========================
    {
        "id": 4001, "key": "DEVOPS-1", "title": "Set up Jenkins CI/CD pipeline",
        "type": "Epic", "status": "Done", "priority": "High_Priority",
        "assignee": "mike", "reporter": "mike",
        "project_key": "DEVOPS", "component": "CI_Pipeline",
        "version_fixed": "DevOps-v1", "version_affected": None,
        "sprint": "DEVOPS Sprint 1", "labels": ["backend"],
        "created_date": "2024-01-01", "updated_date": "2024-01-14",
        "due_date": "2024-01-14", "resolution": "Done_Complete", "parent": None,
        "description": "Set up complete CI/CD with Jenkins, SonarQube, and Artifactory",
        "custom_fields": {"cf_001": 90, "cf_002": "High", "cf_003": 21, "cf_008": "Platform", "cf_009": 14}
    },
    {
        "id": 4002, "key": "DEVOPS-2", "title": "Configure SonarQube quality gates",
        "type": "Task", "status": "Done", "priority": "Medium_Priority",
        "assignee": "mike", "reporter": "mike",
        "project_key": "DEVOPS", "component": "CI_Pipeline",
        "version_fixed": "DevOps-v1", "version_affected": None,
        "sprint": "DEVOPS Sprint 1", "labels": ["backend"],
        "created_date": "2024-01-05", "updated_date": "2024-01-10",
        "due_date": "2024-01-10", "resolution": "Done_Complete", "parent": 4001,
        "description": "Set up quality gates for code coverage, duplication, and vulnerabilities",
        "custom_fields": {"cf_001": 75, "cf_002": "Medium", "cf_003": 5, "cf_008": "Platform", "cf_009": 3}
    },
    {
        "id": 4003, "key": "DEVOPS-3", "title": "Set up Prometheus + Grafana monitoring",
        "type": "Story", "status": "In_Development", "priority": "High_Priority",
        "assignee": "mike", "reporter": "anita",
        "project_key": "DEVOPS", "component": "Monitoring",
        "version_fixed": None, "version_affected": None,
        "sprint": None, "labels": ["backend", "performance"],
        "created_date": "2024-02-01", "updated_date": "2024-02-15",
        "due_date": "2024-03-01", "resolution": None, "parent": None,
        "description": "Deploy Prometheus for metrics collection and Grafana dashboards",
        "custom_fields": {"cf_001": 80, "cf_002": "Medium", "cf_003": 13, "cf_008": "Platform", "cf_009": 10}
    },
    {
        "id": 4004, "key": "DEVOPS-4", "title": "Jenkins pipeline fails on Node 18 projects",
        "type": "Incident", "status": "In_Development", "priority": "Showstopper",
        "assignee": "mike", "reporter": "john",
        "project_key": "DEVOPS", "component": "CI_Pipeline",
        "version_fixed": None, "version_affected": "DevOps-v1",
        "sprint": None, "labels": ["critical-path", "regression"],
        "created_date": "2024-02-10", "updated_date": "2024-02-12",
        "due_date": "2024-02-12", "resolution": None, "parent": None,
        "description": "All builds using Node 18 fail with heap out of memory error",
        "custom_fields": {"cf_001": 100, "cf_002": "Critical", "cf_004": "DEV", "cf_005": "Severe", "cf_008": "Platform", "cf_010": True}
    },

    # ======================== MOB PROJECT ========================
    {
        "id": 5001, "key": "MOB-1", "title": "Mobile app skeleton and navigation",
        "type": "Epic", "status": "Done", "priority": "High_Priority",
        "assignee": "sarah", "reporter": "sarah",
        "project_key": "MOB", "component": "Push_Notifications",
        "version_fixed": "MOB-1.0", "version_affected": None,
        "sprint": "MOB Sprint 1", "labels": ["frontend"],
        "created_date": "2024-04-01", "updated_date": "2024-04-14",
        "due_date": "2024-04-14", "resolution": "Done_Complete", "parent": None,
        "description": "React Native app with tab navigation and authentication flow",
        "custom_fields": {"cf_001": 90, "cf_002": "High", "cf_003": 34, "cf_008": "Delta", "cf_009": 14}
    },
    {
        "id": 5002, "key": "MOB-2", "title": "Implement push notification service",
        "type": "Story", "status": "In_Development", "priority": "High_Priority",
        "assignee": "sarah", "reporter": "sarah",
        "project_key": "MOB", "component": "Push_Notifications",
        "version_fixed": "MOB-1.1", "version_affected": None,
        "sprint": "MOB Sprint 2", "labels": ["backend", "frontend"],
        "created_date": "2024-04-15", "updated_date": "2024-04-20",
        "due_date": "2024-04-28", "resolution": None, "parent": None,
        "description": "FCM integration for Android, APNS for iOS",
        "custom_fields": {"cf_001": 80, "cf_002": "Medium", "cf_003": 13, "cf_008": "Delta", "cf_009": 8}
    },
    {
        "id": 5003, "key": "MOB-3", "title": "App crashes on Android 12 during login",
        "type": "Bug", "status": "Open", "priority": "Showstopper",
        "assignee": "sarah", "reporter": "james",
        "project_key": "MOB", "component": "Push_Notifications",
        "version_fixed": "MOB-1.1", "version_affected": "MOB-1.0",
        "sprint": "MOB Sprint 2", "labels": ["frontend", "customer-reported"],
        "created_date": "2024-04-18", "updated_date": "2024-04-18",
        "due_date": "2024-04-22", "resolution": None, "parent": None,
        "description": "App crashes with FATAL EXCEPTION on Samsung devices running Android 12",
        "custom_fields": {"cf_001": 100, "cf_002": "Critical", "cf_004": "PROD", "cf_005": "Severe", "cf_008": "Delta", "cf_010": False}
    },

    # ======================== DATA PROJECT ========================
    {
        "id": 6001, "key": "DATA-1", "title": "Build real-time data pipeline",
        "type": "Epic", "status": "In_Development", "priority": "High_Priority",
        "assignee": "chen", "reporter": "chen",
        "project_key": "DATA", "component": "Data_Pipeline",
        "version_fixed": "DATA-alpha", "version_affected": None,
        "sprint": "DATA Sprint 1", "labels": ["backend", "performance"],
        "created_date": "2024-05-01", "updated_date": "2024-05-10",
        "due_date": "2024-09-01", "resolution": None, "parent": None,
        "description": "Kafka + Spark streaming pipeline for real-time analytics",
        "custom_fields": {"cf_001": 90, "cf_002": "High", "cf_003": 55, "cf_008": "Platform", "cf_009": 45}
    },
    {
        "id": 6002, "key": "DATA-2", "title": "Set up Kafka cluster",
        "type": "Task", "status": "Done", "priority": "High_Priority",
        "assignee": "chen", "reporter": "chen",
        "project_key": "DATA", "component": "Data_Pipeline",
        "version_fixed": "DATA-alpha", "version_affected": None,
        "sprint": "DATA Sprint 1", "labels": ["backend"],
        "created_date": "2024-05-02", "updated_date": "2024-05-08",
        "due_date": "2024-05-08", "resolution": "Done_Complete", "parent": 6001,
        "description": "Deploy 3-node Kafka cluster with Zookeeper",
        "custom_fields": {"cf_001": 85, "cf_002": "High", "cf_003": 8, "cf_008": "Platform", "cf_009": 5}
    },
    {
        "id": 6003, "key": "DATA-3", "title": "Spark job OOM on large datasets",
        "type": "Bug", "status": "In_Analysis", "priority": "Urgent",
        "assignee": "chen", "reporter": "david",
        "project_key": "DATA", "component": "Data_Pipeline",
        "version_fixed": None, "version_affected": "DATA-alpha",
        "sprint": "DATA Sprint 1", "labels": ["backend", "performance"],
        "created_date": "2024-05-10", "updated_date": "2024-05-12",
        "due_date": "2024-05-14", "resolution": None, "parent": None,
        "description": "Spark streaming job runs out of memory when processing >1M events/sec",
        "custom_fields": {"cf_001": 85, "cf_002": "High", "cf_004": "STAGING", "cf_005": "High", "cf_008": "Platform", "cf_010": False}
    },

    # ======================== SEC PROJECT ========================
    {
        "id": 7001, "key": "SEC-1", "title": "OWASP Top 10 vulnerability scan",
        "type": "Task", "status": "Done", "priority": "Urgent",
        "assignee": "fatima", "reporter": "fatima",
        "project_key": "SEC", "component": None,
        "version_fixed": "SEC-audit-v1", "version_affected": None,
        "sprint": "SEC Sprint 1", "labels": ["security"],
        "created_date": "2024-02-01", "updated_date": "2024-02-10",
        "due_date": "2024-02-10", "resolution": "Done_Complete", "parent": None,
        "description": "Run OWASP ZAP scan against all applications",
        "custom_fields": {"cf_001": 95, "cf_002": "Critical", "cf_003": 8, "cf_008": "Platform", "cf_009": 5}
    },
    {
        "id": 7002, "key": "SEC-2", "title": "SQL injection found in BANK search API",
        "type": "Incident", "status": "Done", "priority": "Showstopper",
        "assignee": "john", "reporter": "fatima",
        "project_key": "SEC", "component": None,
        "version_fixed": "Release 2.1-hotfix", "version_affected": "Release 2.0",
        "sprint": "SEC Sprint 1", "labels": ["security", "critical-path"],
        "created_date": "2024-02-05", "updated_date": "2024-02-08",
        "due_date": "2024-02-06", "resolution": "Fixed", "parent": None,
        "description": "Parameterized queries not used in account search endpoint",
        "custom_fields": {"cf_001": 100, "cf_002": "Critical", "cf_004": "STAGING", "cf_005": "Severe", "cf_008": "Alpha", "cf_010": False}
    },
    {
        "id": 7003, "key": "SEC-3", "title": "Implement SAST in CI pipeline",
        "type": "Change_Request", "status": "In_Development", "priority": "High_Priority",
        "assignee": "mike", "reporter": "fatima",
        "project_key": "SEC", "component": None,
        "version_fixed": None, "version_affected": None,
        "sprint": None, "labels": ["security", "backend"],
        "created_date": "2024-02-12", "updated_date": "2024-02-20",
        "due_date": "2024-04-01", "resolution": None, "parent": None,
        "description": "Add static application security testing to all Jenkins pipelines",
        "custom_fields": {"cf_001": 80, "cf_002": "High", "cf_003": 13, "cf_007": "SEC-POLICY-2024-001", "cf_008": "Platform", "cf_009": 10}
    },

    # ======================== QA PROJECT ========================
    {
        "id": 8001, "key": "QA-1", "title": "Build Selenium test framework",
        "type": "Epic", "status": "In_Development", "priority": "High_Priority",
        "assignee": "james", "reporter": "james",
        "project_key": "QA", "component": None,
        "version_fixed": None, "version_affected": None,
        "sprint": None, "labels": ["backend", "frontend"],
        "created_date": "2024-03-01", "updated_date": "2024-03-20",
        "due_date": "2024-05-01", "resolution": None, "parent": None,
        "description": "Page Object Model based Selenium framework with reporting",
        "custom_fields": {"cf_001": 75, "cf_002": "Medium", "cf_003": 34, "cf_008": "Gamma", "cf_009": 25}
    },
    {
        "id": 8002, "key": "QA-2", "title": "Write test cases for BANK login module",
        "type": "Test_Case", "status": "Done", "priority": "Medium_Priority",
        "assignee": "james", "reporter": "james",
        "project_key": "QA", "component": None,
        "version_fixed": None, "version_affected": None,
        "sprint": None, "labels": ["documentation"],
        "created_date": "2024-03-05", "updated_date": "2024-03-08",
        "due_date": "2024-03-08", "resolution": "Done_Complete", "parent": 8001,
        "description": "50 test cases covering login, forgot password, MFA, session management",
        "custom_fields": {"cf_001": 60, "cf_003": 5, "cf_008": "Gamma", "cf_009": 3}
    },

    # ======================== CLOUD PROJECT ========================
    {
        "id": 9001, "key": "CLOUD-1", "title": "AWS infrastructure setup",
        "type": "Epic", "status": "New", "priority": "High_Priority",
        "assignee": "anita", "reporter": "anita",
        "project_key": "CLOUD", "component": None,
        "version_fixed": "CLOUD-wave1", "version_affected": None,
        "sprint": "CLOUD Sprint 1", "labels": ["backend", "critical-path"],
        "created_date": "2024-05-15", "updated_date": "2024-05-15",
        "due_date": "2024-12-01", "resolution": None, "parent": None,
        "description": "Set up VPC, subnets, EKS cluster, RDS, ElastiCache",
        "custom_fields": {"cf_001": 100, "cf_002": "Critical", "cf_003": 89, "cf_008": "Platform", "cf_009": 60}
    },
    {
        "id": 9002, "key": "CLOUD-2", "title": "Terraform modules for VPC setup",
        "type": "Task", "status": "New", "priority": "High_Priority",
        "assignee": "mike", "reporter": "anita",
        "project_key": "CLOUD", "component": None,
        "version_fixed": "CLOUD-wave1", "version_affected": None,
        "sprint": "CLOUD Sprint 1", "labels": ["backend"],
        "created_date": "2024-05-16", "updated_date": "2024-05-16",
        "due_date": "2024-06-14", "resolution": None, "parent": 9001,
        "description": "Create reusable Terraform modules for multi-AZ VPC",
        "custom_fields": {"cf_001": 85, "cf_002": "High", "cf_003": 13, "cf_008": "Platform", "cf_009": 8}
    },
    {
        "id": 9003, "key": "CLOUD-3", "title": "Database migration strategy document",
        "type": "Spike", "status": "New", "priority": "Urgent",
        "assignee": "david", "reporter": "anita",
        "project_key": "CLOUD", "component": None,
        "version_fixed": "CLOUD-wave1", "version_affected": None,
        "sprint": "CLOUD Sprint 1", "labels": ["database", "documentation"],
        "created_date": "2024-05-17", "updated_date": "2024-05-17",
        "due_date": "2024-06-01", "resolution": None, "parent": 9001,
        "description": "Evaluate DMS vs custom scripts for Oracle to PostgreSQL migration",
        "custom_fields": {"cf_001": 90, "cf_002": "High", "cf_003": 8, "cf_008": "Platform", "cf_009": 5}
    },

    # ======================== CRM PROJECT ========================
    {
        "id": 10001, "key": "CRM-1", "title": "Customer 360 dashboard",
        "type": "Epic", "status": "In_Analysis", "priority": "High_Priority",
        "assignee": "alex", "reporter": "alex",
        "project_key": "CRM", "component": None,
        "version_fixed": None, "version_affected": None,
        "sprint": None, "labels": ["frontend", "backend", "critical-path"],
        "created_date": "2024-04-01", "updated_date": "2024-04-10",
        "due_date": "2024-08-01", "resolution": None, "parent": None,
        "description": "Unified customer view with interaction history, purchases, support tickets",
        "custom_fields": {"cf_001": 95, "cf_002": "High", "cf_003": 55, "cf_008": "Delta", "cf_009": 40}
    },
    {
        "id": 10002, "key": "CRM-2", "title": "Import legacy customer data",
        "type": "Task", "status": "On_Hold", "priority": "Medium_Priority",
        "assignee": "david", "reporter": "alex",
        "project_key": "CRM", "component": None,
        "version_fixed": None, "version_affected": None,
        "sprint": None, "labels": ["database", "backend"],
        "created_date": "2024-04-05", "updated_date": "2024-04-15",
        "due_date": "2024-06-01", "resolution": None, "parent": 10001,
        "description": "Migrate 2M customer records from legacy Oracle DB to new PostgreSQL",
        "custom_fields": {"cf_001": 80, "cf_002": "Medium", "cf_003": 13, "cf_007": "LEGACY-MIG-001", "cf_008": "Delta", "cf_009": 10}
    },
    {
        "id": 10003, "key": "CRM-3", "title": "Service request form improvement",
        "type": "Improvement", "status": "New", "priority": "Normal",
        "assignee": "lisa", "reporter": "alex",
        "project_key": "CRM", "component": None,
        "version_fixed": None, "version_affected": None,
        "sprint": None, "labels": ["frontend", "ui-ux"],
        "created_date": "2024-04-10", "updated_date": "2024-04-10",
        "due_date": None, "resolution": None, "parent": None,
        "description": "Improve service request form with auto-fill and template support",
        "custom_fields": {"cf_001": 40, "cf_002": "Low", "cf_003": 5, "cf_008": "Delta", "cf_009": 3}
    },
    {
        "id": 10004, "key": "CRM-4", "title": "Internal tool access request form",
        "type": "Service_Request", "status": "Cancelled", "priority": "Low_Priority",
        "assignee": "mike", "reporter": "bob",
        "project_key": "CRM", "component": None,
        "version_fixed": None, "version_affected": None,
        "sprint": None, "labels": [],
        "created_date": "2024-04-12", "updated_date": "2024-04-14",
        "due_date": "2024-04-20", "resolution": "Out_Of_Scope", "parent": None,
        "description": "Request for admin access to CRM staging environment",
        "custom_fields": {"cf_001": 10, "cf_002": "Low", "cf_008": "Delta"}
    },
]

# =============================================================================
# COMMENTS (25+ comments across issues)
# =============================================================================
comments = [
    {"id": 1, "issue_id": 1007, "issue_key": "BANK-7", "author": "james", "text": "Reproduced on Chrome and Firefox. Password with & symbol fails consistently.", "created_date": "2024-01-28T10:30:00", "updated_date": None},
    {"id": 2, "issue_id": 1007, "issue_key": "BANK-7", "author": "john", "text": "Root cause identified: input not being sanitized before DB query. Fixing now.", "created_date": "2024-01-28T14:00:00", "updated_date": None},
    {"id": 3, "issue_id": 1007, "issue_key": "BANK-7", "author": "fatima", "text": "This could be a security vulnerability. Escalating priority to Showstopper.", "created_date": "2024-01-28T15:30:00", "updated_date": None},
    {"id": 4, "issue_id": 1007, "issue_key": "BANK-7", "author": "john", "text": "Fix deployed to QA. Used parameterized queries to prevent injection.", "created_date": "2024-01-30T09:00:00", "updated_date": None},
    {"id": 5, "issue_id": 1007, "issue_key": "BANK-7", "author": "james", "text": "QA verified fix. All special characters now work correctly in passwords.", "created_date": "2024-02-01T11:00:00", "updated_date": None},
    {"id": 6, "issue_id": 1003, "issue_key": "BANK-3", "author": "john", "text": "JWT implementation using RS256 algorithm. PR ready for review.", "created_date": "2024-01-22T16:00:00", "updated_date": None},
    {"id": 7, "issue_id": 1003, "issue_key": "BANK-3", "author": "rahul", "text": "Code review comments added. Need to handle token refresh edge case.", "created_date": "2024-01-23T10:00:00", "updated_date": None},
    {"id": 8, "issue_id": 1008, "issue_key": "BANK-8", "author": "fatima", "text": "Security scan flagged this. Sessions remaining active for 2+ hours.", "created_date": "2024-01-30T09:30:00", "updated_date": None},
    {"id": 9, "issue_id": 2003, "issue_key": "ECOM-3", "author": "chen", "text": "Elasticsearch cluster set up. Working on autocomplete mapping now.", "created_date": "2024-02-18T14:00:00", "updated_date": None},
    {"id": 10, "issue_id": 2005, "issue_key": "ECOM-5", "author": "sarah", "text": "Confirmed on iPhone SE and iPhone 12 mini. Button z-index issue.", "created_date": "2024-02-22T11:00:00", "updated_date": None},
    {"id": 11, "issue_id": 2005, "issue_key": "ECOM-5", "author": "lisa", "text": "Updated CSS. Added proper media query breakpoints for small screens.", "created_date": "2024-02-25T09:00:00", "updated_date": None},
    {"id": 12, "issue_id": 3005, "issue_key": "HRM-5", "author": "emma", "text": "Multiple employees reported blank payslips. 15 tickets raised by HR.", "created_date": "2024-03-22T08:00:00", "updated_date": None},
    {"id": 13, "issue_id": 3005, "issue_key": "HRM-5", "author": "kumar", "text": "NPE in PayslipGenerator.java line 142. BankDetails can be null.", "created_date": "2024-03-23T10:00:00", "updated_date": None},
    {"id": 14, "issue_id": 3005, "issue_key": "HRM-5", "author": "kumar", "text": "Fix applied. Added null check and placeholder text for missing bank info.", "created_date": "2024-03-24T15:00:00", "updated_date": None},
    {"id": 15, "issue_id": 3005, "issue_key": "HRM-5", "author": "james", "text": "QA failed: Fix resolves NPE but now shows 'N/A' for bank name which confuses users.", "created_date": "2024-03-26T09:00:00", "updated_date": None},
    {"id": 16, "issue_id": 4004, "issue_key": "DEVOPS-4", "author": "john", "text": "All our ECOM builds have been failing since yesterday morning.", "created_date": "2024-02-10T10:00:00", "updated_date": None},
    {"id": 17, "issue_id": 4004, "issue_key": "DEVOPS-4", "author": "mike", "text": "Jenkins agent has 4GB heap for Node builds. Node 18 needs at least 8GB. Increasing now.", "created_date": "2024-02-10T14:00:00", "updated_date": None},
    {"id": 18, "issue_id": 5003, "issue_key": "MOB-3", "author": "james", "text": "Crash report from Firebase Crashlytics attached. 450 users affected.", "created_date": "2024-04-18T09:00:00", "updated_date": None},
    {"id": 19, "issue_id": 6003, "issue_key": "DATA-3", "author": "chen", "text": "Need to tune Spark executor memory. Currently 2GB per executor.", "created_date": "2024-05-10T16:00:00", "updated_date": None},
    {"id": 20, "issue_id": 6003, "issue_key": "DATA-3", "author": "david", "text": "Also consider partitioning strategy. Current partition count is too low.", "created_date": "2024-05-11T10:00:00", "updated_date": None},
    {"id": 21, "issue_id": 7002, "issue_key": "SEC-2", "author": "fatima", "text": "CRITICAL: Able to extract user table via UNION-based SQL injection on /api/accounts/search", "created_date": "2024-02-05T11:00:00", "updated_date": None},
    {"id": 22, "issue_id": 7002, "issue_key": "SEC-2", "author": "john", "text": "Emergency fix deployed. All queries now use PreparedStatement.", "created_date": "2024-02-06T08:00:00", "updated_date": None},
    {"id": 23, "issue_id": 7002, "issue_key": "SEC-2", "author": "fatima", "text": "Verified fix. Injection no longer possible. Closing.", "created_date": "2024-02-08T10:00:00", "updated_date": None},
    {"id": 24, "issue_id": 9003, "issue_key": "CLOUD-3", "author": "david", "text": "Initial analysis: 500 tables, 2TB data. DMS can handle but needs careful testing.", "created_date": "2024-05-18T14:00:00", "updated_date": None},
    {"id": 25, "issue_id": 10002, "issue_key": "CRM-2", "author": "david", "text": "On hold waiting for legacy DB access credentials from IT.", "created_date": "2024-04-15T09:00:00", "updated_date": None},
]

# =============================================================================
# ISSUE LINKS (15 links with custom link types needing mapping)
# =============================================================================
links = [
    {"id": 1, "source": 1002, "source_key": "BANK-2", "target": 1003, "target_key": "BANK-3", "type": "depends_on", "description": "Login UI depends on JWT service"},
    {"id": 2, "source": 1003, "source_key": "BANK-3", "target": 1004, "target_key": "BANK-4", "type": "is_prerequisite_for", "description": "JWT needed before MFA"},
    {"id": 3, "source": 1007, "source_key": "BANK-7", "target": 7002, "target_key": "SEC-2", "type": "is_related_to", "description": "Both are input sanitization issues"},
    {"id": 4, "source": 1007, "source_key": "BANK-7", "target": 1003, "target_key": "BANK-3", "type": "blocks", "description": "Bug blocks JWT deployment"},
    {"id": 5, "source": 2002, "source_key": "ECOM-2", "target": 2003, "target_key": "ECOM-3", "type": "is_prerequisite_for", "description": "Listing page needs search API"},
    {"id": 6, "source": 2004, "source_key": "ECOM-4", "target": 2001, "target_key": "ECOM-1", "type": "depends_on", "description": "Cart needs product catalog"},
    {"id": 7, "source": 2005, "source_key": "ECOM-5", "target": 2004, "target_key": "ECOM-4", "type": "is_caused_by", "description": "Bug caused by cart epic changes"},
    {"id": 8, "source": 3003, "source_key": "HRM-3", "target": 3005, "target_key": "HRM-5", "type": "blocks", "description": "Payroll engine blocked by payslip bug"},
    {"id": 9, "source": 4003, "source_key": "DEVOPS-3", "target": 4004, "target_key": "DEVOPS-4", "type": "is_related_to", "description": "Monitoring would help detect such issues"},
    {"id": 10, "source": 5002, "source_key": "MOB-2", "target": 5003, "target_key": "MOB-3", "type": "blocks", "description": "Crash must be fixed before notifications"},
    {"id": 11, "source": 7002, "source_key": "SEC-2", "target": 7003, "target_key": "SEC-3", "type": "is_prerequisite_for", "description": "SAST would have caught SQL injection"},
    {"id": 12, "source": 9001, "source_key": "CLOUD-1", "target": 9003, "target_key": "CLOUD-3", "type": "contains", "description": "DB migration is part of cloud setup"},
    {"id": 13, "source": 1009, "source_key": "BANK-9", "target": 1001, "target_key": "BANK-1", "type": "depends_on", "description": "Payments depend on auth system"},
    {"id": 14, "source": 4001, "source_key": "DEVOPS-1", "target": 7003, "target_key": "SEC-3", "type": "is_related_to", "description": "SAST integrates into CI pipeline"},
    {"id": 15, "source": 10002, "source_key": "CRM-2", "target": 9003, "target_key": "CLOUD-3", "type": "is_related_to", "description": "Both involve database migration"},
]

# =============================================================================
# WORKLOGS (20 worklogs with custom time tracking fields)
# =============================================================================
worklogs = [
    {"id": 1, "issue_id": 1002, "issue_key": "BANK-2", "user": "sarah", "hours": 6, "date": "2024-01-04", "description": "Login page initial implementation"},
    {"id": 2, "issue_id": 1002, "issue_key": "BANK-2", "user": "sarah", "hours": 4, "date": "2024-01-05", "description": "Responsive design adjustments"},
    {"id": 3, "issue_id": 1002, "issue_key": "BANK-2", "user": "lisa", "hours": 8, "date": "2024-01-03", "description": "Figma mockup creation"},
    {"id": 4, "issue_id": 1003, "issue_key": "BANK-3", "user": "john", "hours": 8, "date": "2024-01-15", "description": "JWT service scaffolding"},
    {"id": 5, "issue_id": 1003, "issue_key": "BANK-3", "user": "john", "hours": 6, "date": "2024-01-16", "description": "Token generation and validation"},
    {"id": 6, "issue_id": 1003, "issue_key": "BANK-3", "user": "john", "hours": 8, "date": "2024-01-17", "description": "Refresh token logic"},
    {"id": 7, "issue_id": 1003, "issue_key": "BANK-3", "user": "john", "hours": 4, "date": "2024-01-22", "description": "Code review fixes"},
    {"id": 8, "issue_id": 1007, "issue_key": "BANK-7", "user": "john", "hours": 3, "date": "2024-01-29", "description": "Root cause analysis"},
    {"id": 9, "issue_id": 1007, "issue_key": "BANK-7", "user": "john", "hours": 5, "date": "2024-01-30", "description": "Fix implementation and testing"},
    {"id": 10, "issue_id": 2002, "issue_key": "ECOM-2", "user": "sarah", "hours": 8, "date": "2024-02-05", "description": "Product listing grid layout"},
    {"id": 11, "issue_id": 2002, "issue_key": "ECOM-2", "user": "sarah", "hours": 6, "date": "2024-02-06", "description": "Filter sidebar implementation"},
    {"id": 12, "issue_id": 2003, "issue_key": "ECOM-3", "user": "chen", "hours": 8, "date": "2024-02-18", "description": "Elasticsearch index setup"},
    {"id": 13, "issue_id": 2003, "issue_key": "ECOM-3", "user": "chen", "hours": 6, "date": "2024-02-19", "description": "Search query builder"},
    {"id": 14, "issue_id": 3002, "issue_key": "HRM-2", "user": "kumar", "hours": 7, "date": "2024-03-03", "description": "Profile page layout and API integration"},
    {"id": 15, "issue_id": 3003, "issue_key": "HRM-3", "user": "kumar", "hours": 8, "date": "2024-03-18", "description": "Tax calculation module"},
    {"id": 16, "issue_id": 3003, "issue_key": "HRM-3", "user": "kumar", "hours": 8, "date": "2024-03-19", "description": "Deduction rules engine"},
    {"id": 17, "issue_id": 4002, "issue_key": "DEVOPS-2", "user": "mike", "hours": 6, "date": "2024-01-06", "description": "SonarQube installation and config"},
    {"id": 18, "issue_id": 5001, "issue_key": "MOB-1", "user": "sarah", "hours": 8, "date": "2024-04-02", "description": "React Native project setup"},
    {"id": 19, "issue_id": 6002, "issue_key": "DATA-2", "user": "chen", "hours": 8, "date": "2024-05-03", "description": "Kafka cluster deployment"},
    {"id": 20, "issue_id": 7001, "issue_key": "SEC-1", "user": "fatima", "hours": 8, "date": "2024-02-03", "description": "OWASP ZAP scan execution"},
]

# =============================================================================
# ATTACHMENTS (metadata only, need mapping)
# =============================================================================
attachments = [
    {"id": 1, "issue_id": 1007, "issue_key": "BANK-7", "filename": "login_error_screenshot.png", "size_kb": 245, "uploader": "james", "upload_date": "2024-01-28", "mime_type": "image/png"},
    {"id": 2, "issue_id": 1007, "issue_key": "BANK-7", "filename": "browser_console_log.txt", "size_kb": 12, "uploader": "james", "upload_date": "2024-01-28", "mime_type": "text/plain"},
    {"id": 3, "issue_id": 1005, "issue_key": "BANK-5", "filename": "login_mockup_v2.fig", "size_kb": 3400, "uploader": "lisa", "upload_date": "2024-01-05", "mime_type": "application/octet-stream"},
    {"id": 4, "issue_id": 2005, "issue_key": "ECOM-5", "filename": "iphone_se_screenshot.jpg", "size_kb": 180, "uploader": "james", "upload_date": "2024-02-20", "mime_type": "image/jpeg"},
    {"id": 5, "issue_id": 2006, "issue_key": "ECOM-6", "filename": "cdn_comparison_report.pdf", "size_kb": 890, "uploader": "mike", "upload_date": "2024-02-10", "mime_type": "application/pdf"},
    {"id": 6, "issue_id": 3005, "issue_key": "HRM-5", "filename": "payslip_error_stacktrace.log", "size_kb": 8, "uploader": "kumar", "upload_date": "2024-03-23", "mime_type": "text/plain"},
    {"id": 7, "issue_id": 5003, "issue_key": "MOB-3", "filename": "crashlytics_report.pdf", "size_kb": 1200, "uploader": "james", "upload_date": "2024-04-18", "mime_type": "application/pdf"},
    {"id": 8, "issue_id": 5003, "issue_key": "MOB-3", "filename": "android12_crash_video.mp4", "size_kb": 15000, "uploader": "james", "upload_date": "2024-04-18", "mime_type": "video/mp4"},
    {"id": 9, "issue_id": 7002, "issue_key": "SEC-2", "filename": "sql_injection_poc.py", "size_kb": 3, "uploader": "fatima", "upload_date": "2024-02-05", "mime_type": "text/x-python"},
    {"id": 10, "issue_id": 9003, "issue_key": "CLOUD-3", "filename": "db_migration_analysis.xlsx", "size_kb": 560, "uploader": "david", "upload_date": "2024-05-18", "mime_type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"},
]

# =============================================================================
# BOARDS (Kanban/Scrum boards needing mapping)
# =============================================================================
boards = [
    {"id": 1, "name": "BANK Scrum Board", "type": "scrum", "project_key": "BANK", "admin": "rahul"},
    {"id": 2, "name": "ECOM Scrum Board", "type": "scrum", "project_key": "ECOM", "admin": "john"},
    {"id": 3, "name": "HRM Scrum Board", "type": "scrum", "project_key": "HRM", "admin": "priya"},
    {"id": 4, "name": "DevOps Kanban", "type": "kanban", "project_key": "DEVOPS", "admin": "mike"},
    {"id": 5, "name": "MOB Scrum Board", "type": "scrum", "project_key": "MOB", "admin": "sarah"},
    {"id": 6, "name": "DATA Kanban", "type": "kanban", "project_key": "DATA", "admin": "chen"},
    {"id": 7, "name": "Security Board", "type": "kanban", "project_key": "SEC", "admin": "fatima"},
    {"id": 8, "name": "QA Kanban", "type": "kanban", "project_key": "QA", "admin": "james"},
    {"id": 9, "name": "Cloud Migration Board", "type": "scrum", "project_key": "CLOUD", "admin": "anita"},
    {"id": 10, "name": "CRM Scrum Board", "type": "scrum", "project_key": "CRM", "admin": "alex"},
]

# =============================================================================
# WORKFLOWS (custom workflows needing mapping to Jira workflows)
# =============================================================================
workflows = [
    {
        "id": 1, "name": "Software Development Workflow",
        "project_keys": ["BANK", "ECOM", "HRM", "MOB", "CRM"],
        "transitions": [
            {"from": "New", "to": "Open", "trigger": "acknowledge"},
            {"from": "Open", "to": "In_Analysis", "trigger": "start_analysis"},
            {"from": "In_Analysis", "to": "Ready_For_Dev", "trigger": "analysis_complete"},
            {"from": "Ready_For_Dev", "to": "In_Development", "trigger": "start_dev"},
            {"from": "In_Development", "to": "Code_Review", "trigger": "submit_pr"},
            {"from": "Code_Review", "to": "In_Development", "trigger": "changes_requested"},
            {"from": "Code_Review", "to": "Ready_For_QA", "trigger": "pr_approved"},
            {"from": "Ready_For_QA", "to": "In_QA", "trigger": "start_testing"},
            {"from": "In_QA", "to": "QA_Failed", "trigger": "test_failed"},
            {"from": "QA_Failed", "to": "In_Development", "trigger": "reopen"},
            {"from": "In_QA", "to": "Ready_For_UAT", "trigger": "qa_passed"},
            {"from": "Ready_For_UAT", "to": "In_UAT", "trigger": "start_uat"},
            {"from": "In_UAT", "to": "Approved", "trigger": "uat_passed"},
            {"from": "In_UAT", "to": "In_Development", "trigger": "uat_failed"},
            {"from": "Approved", "to": "Done", "trigger": "deploy"},
            {"from": "Done", "to": "Closed", "trigger": "close"},
            {"from": "*", "to": "On_Hold", "trigger": "put_on_hold"},
            {"from": "On_Hold", "to": "Open", "trigger": "resume"},
            {"from": "*", "to": "Cancelled", "trigger": "cancel"},
        ]
    },
    {
        "id": 2, "name": "Bug Workflow",
        "project_keys": ["BANK", "ECOM", "HRM", "MOB", "SEC"],
        "transitions": [
            {"from": "New", "to": "Open", "trigger": "triage"},
            {"from": "Open", "to": "In_Development", "trigger": "start_fix"},
            {"from": "In_Development", "to": "Ready_For_QA", "trigger": "fix_ready"},
            {"from": "Ready_For_QA", "to": "In_QA", "trigger": "start_verification"},
            {"from": "In_QA", "to": "QA_Failed", "trigger": "verification_failed"},
            {"from": "QA_Failed", "to": "In_Development", "trigger": "reopen"},
            {"from": "In_QA", "to": "Done", "trigger": "verified"},
            {"from": "Done", "to": "Closed", "trigger": "close"},
        ]
    },
    {
        "id": 3, "name": "Ops Kanban Workflow",
        "project_keys": ["DEVOPS", "DATA", "QA", "CLOUD"],
        "transitions": [
            {"from": "New", "to": "Open", "trigger": "accept"},
            {"from": "Open", "to": "In_Development", "trigger": "start_work"},
            {"from": "In_Development", "to": "Done", "trigger": "complete"},
            {"from": "Done", "to": "Closed", "trigger": "close"},
        ]
    },
]

# =============================================================================
# HISTORY / CHANGELOG (issue history for migration auditing)
# =============================================================================
changelogs = [
    {"id": 1, "issue_id": 1007, "issue_key": "BANK-7", "author": "fatima", "field": "priority", "old_value": "High_Priority", "new_value": "Showstopper", "changed_date": "2024-01-28T15:30:00"},
    {"id": 2, "issue_id": 1007, "issue_key": "BANK-7", "author": "john", "field": "status", "old_value": "Open", "new_value": "In_Development", "changed_date": "2024-01-29T09:00:00"},
    {"id": 3, "issue_id": 1007, "issue_key": "BANK-7", "author": "john", "field": "status", "old_value": "In_Development", "new_value": "Ready_For_QA", "changed_date": "2024-01-30T17:00:00"},
    {"id": 4, "issue_id": 1007, "issue_key": "BANK-7", "author": "james", "field": "status", "old_value": "Ready_For_QA", "new_value": "In_QA", "changed_date": "2024-01-31T09:00:00"},
    {"id": 5, "issue_id": 1002, "issue_key": "BANK-2", "author": "sarah", "field": "status", "old_value": "In_Development", "new_value": "Code_Review", "changed_date": "2024-01-10T16:00:00"},
    {"id": 6, "issue_id": 1002, "issue_key": "BANK-2", "author": "rahul", "field": "status", "old_value": "Code_Review", "new_value": "Ready_For_QA", "changed_date": "2024-01-11T10:00:00"},
    {"id": 7, "issue_id": 1002, "issue_key": "BANK-2", "author": "james", "field": "status", "old_value": "Ready_For_QA", "new_value": "Done", "changed_date": "2024-01-12T15:00:00"},
    {"id": 8, "issue_id": 3005, "issue_key": "HRM-5", "author": "kumar", "field": "status", "old_value": "Open", "new_value": "In_Development", "changed_date": "2024-03-23T09:00:00"},
    {"id": 9, "issue_id": 3005, "issue_key": "HRM-5", "author": "kumar", "field": "status", "old_value": "In_Development", "new_value": "Ready_For_QA", "changed_date": "2024-03-24T16:00:00"},
    {"id": 10, "issue_id": 3005, "issue_key": "HRM-5", "author": "james", "field": "status", "old_value": "Ready_For_QA", "new_value": "QA_Failed", "changed_date": "2024-03-26T09:30:00"},
    {"id": 11, "issue_id": 2005, "issue_key": "ECOM-5", "author": "sarah", "field": "assignee", "old_value": None, "new_value": "sarah", "changed_date": "2024-02-21T09:00:00"},
    {"id": 12, "issue_id": 10004, "issue_key": "CRM-4", "author": "alex", "field": "status", "old_value": "New", "new_value": "Cancelled", "changed_date": "2024-04-14T10:00:00"},
    {"id": 13, "issue_id": 10004, "issue_key": "CRM-4", "author": "alex", "field": "resolution", "old_value": None, "new_value": "Out_Of_Scope", "changed_date": "2024-04-14T10:00:00"},
    {"id": 14, "issue_id": 7002, "issue_key": "SEC-2", "author": "john", "field": "status", "old_value": "Open", "new_value": "In_Development", "changed_date": "2024-02-05T16:00:00"},
    {"id": 15, "issue_id": 7002, "issue_key": "SEC-2", "author": "fatima", "field": "status", "old_value": "In_Development", "new_value": "Done", "changed_date": "2024-02-08T10:00:00"},
]


# =============================================================================
# API ROUTES
# =============================================================================

@app.route("/")
def index():
    """API documentation listing all available endpoints."""
    endpoints = {
        "message": "Jira Migration Test API - Source System",
        "note": "All field names and values use CUSTOM naming that must be MAPPED to Jira equivalents during migration",
        "endpoints": {
            "/projects": "GET - All projects (project_type needs mapping)",
            "/projects/<key>": "GET - Single project by key",
            "/users": "GET - All users (role field needs mapping to Jira roles)",
            "/roles": "GET - Custom roles (map to Jira project roles)",
            "/issue-types": "GET - Issue types (custom types need mapping)",
            "/statuses": "GET - Custom statuses (map to Jira workflow statuses)",
            "/priorities": "GET - Custom priorities (map to Jira priorities)",
            "/resolutions": "GET - Custom resolutions (map to Jira resolutions)",
            "/components": "GET - Components per project",
            "/versions": "GET - Versions/releases per project",
            "/sprints": "GET - Sprints per project",
            "/labels": "GET - Custom labels",
            "/custom-fields": "GET - Custom field definitions (map to Jira custom fields)",
            "/issues": "GET - All issues with custom fields (supports ?project_key= filter)",
            "/issues/<id>": "GET - Single issue by ID",
            "/comments": "GET - All comments (supports ?issue_id= filter)",
            "/links": "GET - Issue links (link types need mapping)",
            "/worklogs": "GET - Time tracking entries",
            "/attachments": "GET - Attachment metadata",
            "/boards": "GET - Boards (type needs mapping)",
            "/workflows": "GET - Custom workflows (map to Jira workflows)",
            "/changelogs": "GET - Issue history/changelog",
            "/migration-summary": "GET - Summary stats for migration planning",
        },
        "mapping_required": {
            "issue_types": "Epic, Story, Task, Bug, Sub-task map directly; Spike, Change_Request, Improvement, Tech_Debt, Incident, Service_Request, Test_Case need custom mapping",
            "statuses": "16 custom statuses need mapping to Jira workflow (e.g., In_Analysis -> In Progress, Code_Review -> In Review, etc.)",
            "priorities": "10 custom priorities need mapping to Jira's 5 (Showstopper->Highest, Urgent->Highest, High_Priority->High, etc.)",
            "resolutions": "10 custom resolutions need mapping (Wont_Fix->Won't Fix, Duplicate_Issue->Duplicate, etc.)",
            "users": "Custom roles (tech_lead, senior_dev, etc.) need mapping to Jira project roles",
            "custom_fields": "10 custom fields need mapping to Jira custom fields",
            "link_types": "Custom link types (depends_on, is_prerequisite_for, is_caused_by, contains) need mapping",
        }
    }
    return jsonify(endpoints)


@app.route("/projects")
def get_projects():
    return jsonify(projects)


@app.route("/projects/<key>")
def get_project(key):
    project = next((p for p in projects if p["key"] == key.upper()), None)
    if project:
        return jsonify(project)
    return jsonify({"error": "Project not found"}), 404


@app.route("/users")
def get_users():
    active_only = request.args.get("active")
    if active_only and active_only.lower() == "true":
        return jsonify([u for u in users if u["active"]])
    return jsonify(users)


@app.route("/roles")
def get_roles():
    return jsonify(roles)


@app.route("/issue-types")
def get_issue_types():
    return jsonify(issue_types)


@app.route("/statuses")
def get_statuses():
    return jsonify(statuses)


@app.route("/priorities")
def get_priorities():
    return jsonify(priorities)


@app.route("/resolutions")
def get_resolutions():
    return jsonify(resolutions)


@app.route("/components")
def get_components():
    project_key = request.args.get("project_key")
    if project_key:
        filtered = [c for c in components if c["project_key"] == project_key.upper()]
        return jsonify(filtered)
    return jsonify(components)


@app.route("/versions")
def get_versions():
    project_key = request.args.get("project_key")
    if project_key:
        filtered = [v for v in versions if v["project_key"] == project_key.upper()]
        return jsonify(filtered)
    return jsonify(versions)


@app.route("/sprints")
def get_sprints():
    project_key = request.args.get("project_key")
    state = request.args.get("state")
    result = sprints
    if project_key:
        result = [s for s in result if s["project_key"] == project_key.upper()]
    if state:
        result = [s for s in result if s["state"] == state.lower()]
    return jsonify(result)


@app.route("/labels")
def get_labels():
    return jsonify(labels)


@app.route("/custom-fields")
def get_custom_fields():
    return jsonify(custom_field_definitions)


@app.route("/issues")
def get_issues():
    project_key = request.args.get("project_key")
    status = request.args.get("status")
    issue_type = request.args.get("type")
    assignee = request.args.get("assignee")
    priority = request.args.get("priority")

    result = issues
    if project_key:
        result = [i for i in result if i["project_key"] == project_key.upper()]
    if status:
        result = [i for i in result if i["status"] == status]
    if issue_type:
        result = [i for i in result if i["type"] == issue_type]
    if assignee:
        result = [i for i in result if i["assignee"] == assignee]
    if priority:
        result = [i for i in result if i["priority"] == priority]
    return jsonify(result)


@app.route("/issues/<int:issue_id>")
def get_issue(issue_id):
    issue = next((i for i in issues if i["id"] == issue_id), None)
    if issue:
        issue_comments = [c for c in comments if c["issue_id"] == issue_id]
        issue_worklogs = [w for w in worklogs if w["issue_id"] == issue_id]
        issue_attachments = [a for a in attachments if a["issue_id"] == issue_id]
        issue_links_out = [l for l in links if l["source"] == issue_id]
        issue_links_in = [l for l in links if l["target"] == issue_id]
        issue_history = [ch for ch in changelogs if ch["issue_id"] == issue_id]

        result = {
            **issue,
            "comments": issue_comments,
            "worklogs": issue_worklogs,
            "attachments": issue_attachments,
            "outward_links": issue_links_out,
            "inward_links": issue_links_in,
            "changelog": issue_history,
        }
        return jsonify(result)
    return jsonify({"error": "Issue not found"}), 404


@app.route("/comments")
def get_comments():
    issue_id = request.args.get("issue_id", type=int)
    if issue_id:
        filtered = [c for c in comments if c["issue_id"] == issue_id]
        return jsonify(filtered)
    return jsonify(comments)


@app.route("/links")
def get_links():
    return jsonify(links)


@app.route("/worklogs")
def get_worklogs():
    issue_id = request.args.get("issue_id", type=int)
    user = request.args.get("user")
    result = worklogs
    if issue_id:
        result = [w for w in result if w["issue_id"] == issue_id]
    if user:
        result = [w for w in result if w["user"] == user]
    return jsonify(result)


@app.route("/attachments")
def get_attachments():
    issue_id = request.args.get("issue_id", type=int)
    if issue_id:
        filtered = [a for a in attachments if a["issue_id"] == issue_id]
        return jsonify(filtered)
    return jsonify(attachments)


@app.route("/boards")
def get_boards():
    return jsonify(boards)


@app.route("/workflows")
def get_workflows():
    return jsonify(workflows)


@app.route("/changelogs")
def get_changelogs():
    issue_id = request.args.get("issue_id", type=int)
    if issue_id:
        filtered = [ch for ch in changelogs if ch["issue_id"] == issue_id]
        return jsonify(filtered)
    return jsonify(changelogs)


@app.route("/migration-summary")
def migration_summary():
    """Summary statistics for migration planning."""
    summary = {
        "total_projects": len(projects),
        "total_users": len(users),
        "active_users": len([u for u in users if u["active"]]),
        "inactive_users": len([u for u in users if not u["active"]]),
        "total_issues": len(issues),
        "issues_by_project": {},
        "issues_by_type": {},
        "issues_by_status": {},
        "issues_by_priority": {},
        "total_comments": len(comments),
        "total_worklogs": len(worklogs),
        "total_worklog_hours": sum(w["hours"] for w in worklogs),
        "total_attachments": len(attachments),
        "total_links": len(links),
        "total_changelog_entries": len(changelogs),
        "total_components": len(components),
        "total_versions": len(versions),
        "total_sprints": len(sprints),
        "total_boards": len(boards),
        "total_workflows": len(workflows),
        "custom_fields_count": len(custom_field_definitions),
        "custom_issue_types_needing_mapping": [
            it["name"] for it in issue_types
            if it["name"] not in ["Epic", "Story", "Task", "Bug", "Sub-task"]
        ],
        "custom_statuses_needing_mapping": [s["name"] for s in statuses],
        "custom_priorities_needing_mapping": [p["name"] for p in priorities],
        "custom_resolutions_needing_mapping": [r["name"] for r in resolutions],
    }

    for issue in issues:
        pk = issue["project_key"]
        summary["issues_by_project"][pk] = summary["issues_by_project"].get(pk, 0) + 1

        it = issue["type"]
        summary["issues_by_type"][it] = summary["issues_by_type"].get(it, 0) + 1

        st = issue["status"]
        summary["issues_by_status"][st] = summary["issues_by_status"].get(st, 0) + 1

        pr = issue["priority"]
        summary["issues_by_priority"][pr] = summary["issues_by_priority"].get(pr, 0) + 1

    return jsonify(summary)


# =============================================================================
# RUN
# =============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("  JIRA MIGRATION TEST API - SOURCE SYSTEM")
    print("  Visit http://localhost:5000/ for endpoint documentation")
    print("=" * 60)
    app.run(port=5000, debug=True)