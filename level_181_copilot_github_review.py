print("🤖 Level 181 VS Code + AI Copilot and GitHub Web Practice")

name = input("Enter your name: ")
device = input("Are you using Surface or iMac? ")
minutes = int(input("How many minutes are you practicing today? "))

def show_summary(name, device, minutes):
    print()
    print("Hello", name)
    print("Today you practiced VS Code with AI Copilot and GitHub Web.")
    print("Device:", device)
    print("Practice time:", minutes, "minutes")

def show_tasks():
    tasks = [
        "Open VS Code",
        "Check correct python-practice folder",
        "Create Level 181 Python file",
        "Ask AI Copilot one question",
        "Run the Python program",
        "Check Source Control",
        "Commit and Sync",
        "Check GitHub Web"
    ]

    print()
    print("Today's practice tasks:")
    for task in tasks:
        print("✅", task)

def show_result(minutes):
    print()
    if minutes >= 20:
        print("Great job! You completed your 20-minute practice goal.")
    else:
        print("Good start! Try to reach 20 minutes next time.")

show_summary(name, device, minutes)
show_tasks()
show_result(minutes)