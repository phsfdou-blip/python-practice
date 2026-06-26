print("🤖 Level 163 VS Code + AI Copilot List Function Practice")

name = input("Enter your name: ")
device = input("Are you using Surface or iMac? ")
minutes = int(input("How many minutes are you practicing today? "))

def show_summary(name, device, minutes):
    print()
    print("Hello", name)
    print("Today you practiced VS Code with AI Copilot.")
    print("Device:", device)
    print("Practice time:", minutes, "minutes")

def show_tasks():
    tasks = [
        "Open VS Code",
        "Create Level 163 Python file",
        "Ask Copilot one question",
        "Read Copilot answer",
        "Run Python program",
        "Fix any mistake",
        "Commit and Sync",
        "Check GitHub Web"
    ]

    print()
    print("Today's VS Code + AI Copilot checklist:")
    for task in tasks:
        print("✅", task)

show_summary(name, device, minutes)
show_tasks()

if minutes >= 25:
    print()
    print("Excellent! 25 minutes VS Code + AI Copilot practice complete ✅")
else:
    print()
    print("Good start! Keep practicing step by step.")