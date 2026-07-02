print("🤖 Level 164 VS Code + AI Copilot Function List Review")

name = input("Enter your name: ")
device = input("Are you using Surface or iMac? ")
minutes = int(input("How many minutes are you practicing today? "))

def show_summary(name, device, minutes):
    print()
    print("Hello", name)
    print("Today you practiced VS Code and AI Copilot.")
    print("Device:", device)
    print("Practice time:", minutes, "minutes")

def show_tasks():
    tasks = [
        "Open VS Code",
        "Create Level 164 Python file",
        "Review function",
        "Review list",
        "Review for loop",
        "Ask Copilot one question",
        "Run Python program",
        "Commit and Sync",
        "Check GitHub Web"
    ]

    print()
    print("Today's practice checklist:")

    for task in tasks:
        print("✅", task)

show_summary(name, device, minutes)
show_tasks()

if minutes >= 25:
    print()
    print("Excellent! Level 164 practice complete ✅")
else:
    print()
    print("Good start! Keep going step by step.")