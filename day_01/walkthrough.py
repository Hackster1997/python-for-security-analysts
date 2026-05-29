# Day 1 Walkthrough - Python Basics
# Run this file to see Python concepts in action!
# No need to write code - just run and read the output.

print("="*80)
print("DAY 1 WALKTHROUGH - PYTHON BASICS")
print("="*80)

# VARIABLES
print("\n--- CONCEPT 1: VARIABLES ---")
alert_severity = "High"
analyst_name = "Yarranav"
alert_count = 42

print(f"Alert Severity: {alert_severity}")
print(f"Analyst Name: {analyst_name}")
print(f"Alert Count: {alert_count}")

# LISTS
print("\n--- CONCEPT 2: LISTS ---")
suspicious_ips = ["10.0.0.1", "192.168.1.100", "172.16.0.5"]
print(f"Suspicious IPs: {suspicious_ips}")
print(f"First IP: {suspicious_ips[0]}")
print(f"Total IPs: {len(suspicious_ips)}")

# LOOPS
print("\n--- CONCEPT 3: LOOPS ---")
alerts = ["Alert-1", "Alert-2", "Alert-3"]
print("Processing alerts:")
for alert in alerts:
    print(f"  - {alert}")

# IF/ELSE
print("\n--- CONCEPT 4: IF/ELSE ---")
severity = "Critical"

if severity == "Critical":
    print(f"Action: {severity} alert - Escalate now!")
elif severity == "High":
    print(f"Action: {severity} alert - Investigate within 1 hour")
else:
    print(f"Action: {severity} alert - Add to backlog")

# FUNCTIONS
print("\n--- CONCEPT 5: FUNCTIONS ---")

def check_severity(level):
    if level == "Critical":
        return "Escalate!"
    else:
        return "Monitor"

result = check_severity("Critical")
print(f"Check result: {result}")

# DICTIONARIES
print("\n--- CONCEPT 6: DICTIONARIES ---")
alert = {
    "severity": "High",
    "source_ip": "10.0.0.5",
    "status": "Open"
}

print(f"Alert Ticket:")
print(f"  Severity: {alert['severity']}")
print(f"  Source IP: {alert['source_ip']}")
print(f"  Status: {alert['status']}")

# COMBINING CONCEPTS
print("\n--- COMBINING CONCEPTS: ALERT TRIAGE PIPELINE ---")

def triage_alert(alert_data):
    """Process an alert and recommend action"""
    if alert_data["severity"] == "Critical":
        return "Escalate to incident response"
    elif alert_data["severity"] == "High":
        return "Assign to senior analyst"
    else:
        return "Add to backlog"

alerts_queue = [
    {"severity": "Critical", "source_ip": "192.168.1.1"},
    {"severity": "High", "source_ip": "10.0.0.5"},
    {"severity": "Medium", "source_ip": "8.8.8.8"}
]

print("Processing alert queue:")
for idx, alert in enumerate(alerts_queue, 1):
    action = triage_alert(alert)
    print(f"  Alert {idx}: {alert['source_ip']} (Severity: {alert['severity']}) -> {action}")

print("\n" + "="*80)
print("Great! You've seen all Day 1 concepts in action.")
print("Now head to practice.py to try writing code yourself!")
print("="*80)
