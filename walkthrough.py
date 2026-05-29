"""
Day 1 - Python Basics (Guided Walkthrough)

Just RUN this file and READ the output. Nothing to write yet.
Each section teaches one concept with a security example.

Read the Day_01_Guide.txt first for plain-English explanations,
then run this file to see every concept in action.
"""

# ============================================================
# CONCEPT 1: VARIABLES
# A variable stores a value with a name, like a label on a box.
# ============================================================

analyst_name = "Yarranav"          # text (string)
years_experience = 3               # number (integer)
is_learning_python = True          # yes/no (boolean)

print("=" * 50)
print("CONCEPT 1: VARIABLES")
print("=" * 50)
print()
print("I created 3 variables:")
print("  analyst_name       =", analyst_name, "       (type: string)")
print("  years_experience   =", years_experience, "              (type: integer)")
print("  is_learning_python =", is_learning_python, "           (type: boolean)")
print()
print("KEY LESSON: Variables hold values. You choose the name.")
print()


# ============================================================
# CONCEPT 2: LISTS
# A list holds multiple values in order, like a column in Excel.
# ============================================================

suspicious_ips = ["10.0.0.1", "192.168.1.100", "172.16.0.5"]

print("=" * 50)
print("CONCEPT 2: LISTS")
print("=" * 50)
print()
print("I created a list called 'suspicious_ips':")
print("  Full list:", suspicious_ips)
print("  First item (index 0):", suspicious_ips[0])
print("  Second item (index 1):", suspicious_ips[1])
print("  Third item (index 2):", suspicious_ips[2])
print("  How many items?", len(suspicious_ips))
print()
print("KEY LESSON: Lists use [ ]. Counting starts at 0, not 1.")
print()


# ============================================================
# CONCEPT 3: LOOPS
# A loop repeats the same action for every item in a list.
# Like checking each alert in your queue one by one.
# ============================================================

print("=" * 50)
print("CONCEPT 3: LOOPS")
print("=" * 50)
print()
print("Looping through each IP in the list:")
for ip in suspicious_ips:
    print("  Checking IP:", ip)
print()
print("The loop ran", len(suspicious_ips), "times (once per item).")
print()
print("KEY LESSON: 'for item in list:' runs the indented code for each item.")
print()


# ============================================================
# CONCEPT 4: IF / ELSE (Decisions)
# Your code can choose different paths, like a playbook.
# ============================================================

severity = "Critical"

print("=" * 50)
print("CONCEPT 4: IF / ELSE (DECISIONS)")
print("=" * 50)
print()
print("Alert severity is:", severity)
print()

if severity == "Critical":
    print("  Decision: ESCALATE IMMEDIATELY!")
elif severity == "High":
    print("  Decision: Investigate within 1 hour")
else:
    print("  Decision: Add to backlog")

print()
print("Now let's try with severity = 'Low':")
severity = "Low"
print("  Alert severity is:", severity)

if severity == "Critical":
    print("  Decision: ESCALATE IMMEDIATELY!")
elif severity == "High":
    print("  Decision: Investigate within 1 hour")
else:
    print("  Decision: Add to backlog")

print()
print("KEY LESSON: == checks if values match. if/elif/else picks one path.")
print()


# ============================================================
# CONCEPT 5: FUNCTIONS (Reusable Procedures)
# Like a triage procedure you follow every time.
# Define once, use many times.
# ============================================================

def get_action(alert_severity):
    """Given a severity, return what action to take."""
    if alert_severity == "Critical":
        return "Escalate immediately"
    elif alert_severity == "High":
        return "Investigate within 1 hour"
    elif alert_severity == "Medium":
        return "Investigate within 4 hours"
    else:
        return "Add to backlog"

print("=" * 50)
print("CONCEPT 5: FUNCTIONS")
print("=" * 50)
print()
print("I defined a function called 'get_action'.")
print("Now I'll call it with different severities:")
print()
print("  Critical ->", get_action("Critical"))
print("  High     ->", get_action("High"))
print("  Medium   ->", get_action("Medium"))
print("  Low      ->", get_action("Low"))
print()
print("KEY LESSON: 'def' creates a function. 'return' sends back a result.")
print()


# ============================================================
# CONCEPT 6: DICTIONARIES (Key-Value Storage)
# Like an alert ticket with labeled fields.
# ============================================================

alert_ticket = {
    "id": "ALT-2024-001",
    "severity": "High",
    "source_ip": "10.0.0.5",
    "description": "Suspicious outbound connection",
    "status": "Open",
}

print("=" * 50)
print("CONCEPT 6: DICTIONARIES")
print("=" * 50)
print()
print("I created a dictionary called 'alert_ticket':")
print("  Alert ID:", alert_ticket["id"])
print("  Severity:", alert_ticket["severity"])
print("  Source IP:", alert_ticket["source_ip"])
print("  Description:", alert_ticket["description"])
print("  Status:", alert_ticket["status"])

# Change a value
alert_ticket["status"] = "Investigating"
print()
print("After changing status to 'Investigating':")
print("  Status:", alert_ticket["status"])
print()
print("KEY LESSON: Dictionaries use { }. Access values with dict[\"key\"].")
print()


# ============================================================
# CONCEPT 7: PUTTING IT ALL TOGETHER
# Loop through a list of alerts, use a function, count results.
# ============================================================

alerts = [
    {"id": "ALT-001", "severity": "Critical"},
    {"id": "ALT-002", "severity": "Low"},
    {"id": "ALT-003", "severity": "High"},
    {"id": "ALT-004", "severity": "Medium"},
    {"id": "ALT-005", "severity": "Critical"},
]

action_counts = {}

print("=" * 50)
print("CONCEPT 7: PUTTING IT ALL TOGETHER")
print("=" * 50)
print()
print("Processing 5 alerts through our triage function:")
print()

for alert in alerts:
    action = get_action(alert["severity"])
    print("  ", alert["id"], "(", alert["severity"], ") ->", action)

    # Count how many of each action we have
    if action in action_counts:
        action_counts[action] += 1
    else:
        action_counts[action] = 1

print()
print("Summary of actions needed:")
for action, count in action_counts.items():
    print("  ", action, ":", count)

print()
print("=" * 50)
print("DAY 1 COMPLETE!")
print("=" * 50)
print()
print("You now understand: variables, lists, loops,")
print("if/else, functions, and dictionaries.")
print()
print("When you're ready, tell me and I'll give you")
print("simple practice tasks to test your understanding!")