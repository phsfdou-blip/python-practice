print("🤖 Level 170 VS Code + AI Copilot Function Return Practice")

name = input("Enter your name: ")
device = input("Are you using Surface or iMac? ")
minutes = int(input("How many minutes are you practicing today? "))

def square(number):
    return number * number

def show_summary(name, device, minutes):
    print()
    print("Hello", name)
    print("Today you practiced VS Code with AI Copilot.")
    print("Device:", device)
    print("Practice time:", minutes, "minutes")

def show_result(minutes):
    squared_minutes = square(minutes)
    print()
    print("Your practice minutes squared is:", squared_minutes)

def show_tasks():
    tasks = [
        "Open VS Code",
        "Create Level 170 Python file",
        "Ask Copilot about return",
        "Run the program",
        "Check Source Control",
        "Commit and Sync",
        "Check GitHub Web"
    ]

    print()
    print("Today's checklist:")
    for task in tasks:
        print("✅", task)

show_summary(name, device, minutes)
show_result(minutes)
show_tasks()

if minutes >= 25:
    print()
    print("Excellent! 25 minutes VS Code + AI Copilot practice complete ✅")
else:
    print()
    print("Good start! Keep going step by step.")