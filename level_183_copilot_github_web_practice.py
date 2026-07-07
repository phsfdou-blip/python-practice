print("🤖 Level 183 VS Code + GitHub Web + AI Copilot Practice")

name = input("Enter your name: ")
device = input("Are you using Surface or iMac? ")

try:
    minutes = int(input("How many minutes are you practicing today? "))
except ValueError:
    print("Please enter a number for minutes.")
    minutes = 0

def show_summary(name, device, minutes):
    print()
    print("Hello", name)
    print("Today you practiced VS Code, GitHub Web, and AI Copilot.")
    print("Device:", device)
    print("Practice time:", minutes, "minutes")

def show_tasks():
    tasks = [
        "Open VS Code",
        "Check correct python-practice folder",
        "Create Level 183 Python file",
        "Run the Python program",
        "Ask AI Copilot one question",
        "Check Source Control",
        "Commit and Sync",
        "Open GitHub Web",
        "Confirm the file is online"
    ]

    print()
    print("Today's tasks:")

    for task in tasks:
        print("✅", task)

show_summary(name, device, minutes)
show_tasks()

if minutes >= 20:
    print()
    print("Great job! You reached your 20-minute practice goal.")
else:
    print()
    print("Good start. Keep practicing step by step.")