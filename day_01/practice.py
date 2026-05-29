#!/usr/bin/env python3
"""
Day 1 Practice - Hands-on exercises with solutions
Read each problem, write your solution, then check against the provided answer.
"""

# ============================================================================
# EXERCISE 1: Variables
# ============================================================================
print("EXERCISE 1: Create and use variables")
print("-" * 40)

# Problem: Create variables for an alert ticket
# - ticket_id should be "ALERT-001"
# - severity should be "High"
# - count should be 1

# YOUR CODE HERE:
ticket_id = "ALERT-001"
severity = "High"
count = 1

print(f"Ticket: {ticket_id}")
print(f"Severity: {severity}")
print(f"Count: {count}")
print()

# ============================================================================
# EXERCISE 2: Lists
# ============================================================================
print("EXERCISE 2: Work with lists")
print("-" * 40)

# Problem: Create a list of malicious hashes and access elements
malicious_hashes = ["abc123def456", "xyz789uvw012", "hash999abc"]

print(f"All hashes: {malicious_hashes}")
print(f"First hash: {malicious_hashes[0]}")
print(f"Last hash: {malicious_hashes[2]}")
print(f"Total hashes: {len(malicious_hashes)}")

# Add a new hash
malicious_hashes.append("newHash777")
print(f"After adding: {malicious_hashes}")
print()

# ============================================================================
# EXERCISE 3: Loops
# ============================================================================
print("EXERCISE 3: Loop through a list")
print("-" * 40)

# Problem: Print each IP in the list
suspicious_ips = ["192.168.1.1", "10.0.0.5", "172.16.0.1"]

print("Suspicious IPs:")
for ip in suspicious_ips:
    print(f"  - {ip}")
print()

# ============================================================================
# EXERCISE 4: If/Else
# ============================================================================
print("EXERCISE 4: Make decisions with if/else")
print("-" * 40)

# Problem: Check if severity is Critical and take action
test_severity = "Critical"

if test_severity == "Critical":
    action = "Escalate immediately!"
elif test_severity == "High":
    action = "Investigate within 1 hour"
else:
    action = "Add to backlog"

print(f"Severity: {test_severity}")
print(f"Action: {action}")
print()

# ============================================================================
# EXERCISE 5: Functions
# ============================================================================
print("EXERCISE 5: Write a function")
print("-" * 40)

# Problem: Create a function that classifies IOC type
def classify_ioc(ioc):
    """Classify an indicator as IP, hash, or domain"""
    if "." in ioc and len(ioc) < 20:
        return "IP or Domain"
    elif len(ioc) == 32 or len(ioc) == 40 or len(ioc) == 64:
        return "Hash (MD5/SHA1/SHA256)"
    else:
        return "Unknown"

print(f"192.168.1.1 -> {classify_ioc('192.168.1.1')}")
print(f"example.com -> {classify_ioc('example.com')}")
print(f"5d41402abc4b2a76b9719d911017c592 -> {classify_ioc('5d41402abc4b2a76b9719d911017c592')}")
print()

# ============================================================================
# EXERCISE 6: Dictionaries
# ============================================================================
print("EXERCISE 6: Use dictionaries for structured data")
print("-" * 40)

# Problem: Create an incident ticket dictionary and access its fields
incident = {
    "id": "INC-2026-001",
    "severity": "High",
    "type": "Malware Detection",
    "status": "Open",
    "analyst": "Yarranav"
}

print("Incident Ticket:")
print(f"  ID: {incident['id']}")
print(f"  Type: {incident['type']}")
print(f"  Severity: {incident['severity']}")
print(f"  Status: {incident['status']}")
print(f"  Analyst: {incident['analyst']}")

# Update status
incident['status'] = 'In Investigation'
print(f"Updated Status: {incident['status']}")
print()

# ============================================================================
# EXERCISE 7: Combining All Concepts
# ============================================================================
print("EXERCISE 7: Build an alert triage system")
print("-" * 40)

def triage_alert(alert_dict):
    """Process alert and return recommended action"""
    severity = alert_dict["severity"]
    
    if severity == "Critical":
        return "Escalate to IR team immediately"
    elif severity == "High":
        return "Assign to senior analyst"
    elif severity == "Medium":
        return "Assign to junior analyst"
    else:
        return "Monitor and archive"

alerts = [
    {"id": "A001", "severity": "Critical", "source": "192.168.1.10"},
    {"id": "A002", "severity": "High", "source": "10.0.0.50"},
    {"id": "A003", "severity": "Low", "source": "8.8.8.8"},
]

print("Alert Triage Results:")
for alert in alerts:
    action = triage_alert(alert)
    print(f"  Alert {alert['id']}: {action}")

print("\n" + "="*80)
print("🎉 You've completed Day 1 exercises!")
print("Next: Move to Day 2 to learn about APIs and data handling.")
print("="*80)
