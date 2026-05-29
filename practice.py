"""
Day 1 - Practice Tasks (Test Your Understanding)

Instructions:
- Each task tells you WHAT to do.
- Write your code below each task comment.
- Run this file after each task to check your output.
- Expected output is shown so you can verify.

Good luck!
"""


# ============================================================
# TASK 1: Create Variables
# ============================================================
# Create 3 variables:
#   - alert_id       -> store the text "INC-2026-0042"
#   - is_malicious   -> store True
#   - risk_score     -> store the number 85
#
# Then print all three like this:
#   Alert: INC-2026-0042
#   Malicious: True
#   Risk Score: 85

# YOUR CODE BELOW:
alert_id = "INC-2026-0042"
is_malicious = True
risk_score = 85

print("Alert:", alert_id)
print("Malicious:", is_malicious)
print("Risk Score:", risk_score)
print()

# ============================================================
# TASK 2: Create a List and Loop Through It
# ============================================================
# Create a list called "blocked_ips" with these 4 IPs:
#   "10.0.0.5", "192.168.1.99", "172.16.0.10", "10.0.0.22"
#
# Then loop through the list and print each one like this:
#   Blocked: 10.0.0.5
#   Blocked: 192.168.1.99
#   Blocked: 172.16.0.10
#   Blocked: 10.0.0.22

# YOUR CODE BELOW:
blocked_ips = ["10.0.0.5", "192.168.1.99", "172.16.0.10", "10.0.0.22"]

for ip in blocked_ips:
    print("Blocked:", ip)
print()

# ============================================================
# TASK 3: Use If/Else
# ============================================================
# Create a variable called "threat_level" and set it to "High"
#
# Write an if/elif/else that prints:
#   If "Critical" -> "ACTION: Isolate host immediately"
#   If "High"     -> "ACTION: Investigate within 1 hour"
#   If "Medium"   -> "ACTION: Review in next shift"
#   Anything else -> "ACTION: Log and monitor"
#
# Expected output (since threat_level is "High"):
#   ACTION: Investigate within 1 hour

# YOUR CODE BELOW:

threat_level = "High"

if threat_level == "Critical":
    print("ACTION: Isolate host immediately")
elif threat_level == "High":
    print("ACTION: Investigate within 1 hour")
elif threat_level == "Medium":
    print("ACTION: Review in next shift")
else:
    print("ACTION: Log and monitor")
print()


# ============================================================
# TASK 4: Create a Dictionary
# ============================================================
# Create a dictionary called "incident" with these keys and values:
#   "title"    -> "Phishing email detected"
#   "severity" -> "`High`"
#   "status"   -> "Open"
#   "analyst"  -> "Yarranav"
#
# Then print:
#   Incident: Phishing email detected
#   Severity: High
#   Assigned to: Yarranav

# YOUR CODE BELOW:
incident = {
    "title": "Phishing email detected",
    "severity": "High",
    "status": "Open",
    "analyst": "Yarranav"
}

print("Incident:", incident["title"])
print("Severity:", incident["severity"])
print("Assigned to:", incident["analyst"])


# ============================================================
# TASK 5: Write a Function
# ============================================================
# Create a function called "check_port" that takes one parameter: port_number
#
# The function should:
#   - If port_number is 22, return "SSH"
#   - If port_number is 80, return "HTTP"
#   - If port_number is 443, return "HTTPS"
#   - If port_number is 3389, return "RDP"
#   - For anything else, return "Unknown"
#
# After defining the function, call it and print results like this:
#   Port 22: SSH
#   Port 443: HTTPS
#   Port 8080: Unknown

# YOUR CODE BELOW:
def check_port(port_number):
    if port_number == 22:
        return "SSH"
    elif port_number == 80:
        return "HTTP"
    elif port_number == 443:
        return "HTTPS"
    elif port_number == 3389:
        return "RDP"
    else:
        return "Unknown"

print("Port 22:", check_port(22))
print("Port 443:", check_port(443))
print("Port 8080:", check_port(8080))
    




# ============================================================
# BONUS TASK: Combine Everything
# ============================================================
# This one uses lists, loops, dictionaries, if/else, and functions together.
#
# 1. Create this list of alert dictionaries:
#
#    alerts = [
#        {"id": "ALT-001", "severity": "Critical"},
#        {"id": "ALT-002", "severity": "Low"},
#        {"id": "ALT-003", "severity": "High"},
#    ]
#
# 2. Loop through each alert.
# 3. For each alert, if severity is "Critical" or "High",
#    print:  "[URGENT] ALT-001 requires immediate action"
#    Otherwise print:  "[OK] ALT-002 logged for review"
#
# Expected output:
#   [URGENT] ALT-001 requires immediate action
#   [OK] ALT-002 logged for review
#   [URGENT] ALT-003 requires immediate action

# YOUR CODE BELOW:

alerts = [
    {"id": "ALT-001", "severity": "Critical"},
    {"id": "ALT-002", "severity": "Low"},
    {"id": "ALT-003", "severity": "High"},
]

for alert in alerts:
    if alert["severity"] == "Critical" or alert["severity"] == "High":
        print("[URGENT]", alert["id"], "requires immediate action")
    else:
        print("[OK]", alert["id"], "logged for review")
print()