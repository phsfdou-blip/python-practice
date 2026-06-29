print("🤖 Level 169 VS Code + AI Copilot Practice")

name = input("Enter your name: ")
minutes = int(input("How many minutes are you practicing today? "))

def show_summary(name, minutes):
    print()
    print("Hello", name)
    print("You are practicing VS Code with AI Copilot.")
    print("Practice time:", minutes, "minutes")

def show_tasks():
    tasks = [
        "Open VS Code",
        "Create Python file",
        "Ask Copilot one question",
        "Run the program",
        "Commit and Sync",
        "Check GitHub Web"
    ]
    
    print()
    print("Today's tasks:")
    for task in tasks:
        print("✅", task)

show_summary(name, minutes)
show_tasks()

if minutes >= 25:
    print()
    print("Excellent! 25 minutes complete 🚀")
else:
    print()
    print("Good progress! Keep going step by step.")