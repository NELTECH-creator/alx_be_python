# daily_reminder.py

# Prompt user for a single task and details (exact wording expected)
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Generate reminder using match case for priority
match priority:
    case "high":
        reminder = f"High-priority task: '{task}'"
    case "medium":
        reminder = f"Medium-priority task: '{task}'"
    case "low":
        reminder = f"Low-priority task: '{task}'"
    case _:
        reminder = f"Task: '{task}' (priority not specified)"

# Check if the task is time-sensitive
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Print the customized reminder (exact format required)
print(f"Reminder: {reminder}")
