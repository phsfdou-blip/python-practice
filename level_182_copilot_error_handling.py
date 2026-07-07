print("🤖 Level 182 VS Code + AI Copilot Error Handling Practice")

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
    print("Today you practiced VS Code with AI Copilot.")
    print("Device:", device)
    print("Practice time:", minutes, "minutes")

def show_tasks():
    tasks = [
        "Open VS Code",
        "Create Level 182 Python file",
        "Practice try and except",
        "Ask AI Copilot one question",
        "Run the Python program",
        "Check Source Control",
        "Commit and Sync",
        "Check GitHub Web"
    ]

    print()
    print("Tonight's tasks:")
    for task in tasks:
        print("✅", task)

show_summary(name, device, minutes)
show_tasks()

if minutes >= 20:
    print()
    print("Excellent! You completed your 20-minute goal.")
else:
    print()
    print("Good practice. Keep going step by step.")