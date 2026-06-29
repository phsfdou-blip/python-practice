
print("🤖 Level 166 VS Code + AI Copilot Improve Code Practice")

name = input("Enter your name: ")
device = input("Are you using Surface or iMac? ")
minutes = int(input("How many minutes are you practicing today? "))
goal = input("What is your coding goal today? ")

def show_summary(name, device, minutes, goal):
    print()
    print("Hello", name)
    print("Today you practiced VS Code with GitHub Copilot.")
    print("Device:", device)
    print("Practice time:", minutes, "minutes")
    print("Goal:", goal)

def show_checklist():
    tasks = [
        "Open VS Code",
        "Create Level 166 Python file",
        "Ask GitHub Copilot to improve code",
        "Run the Python program",
        "Fix any mistake",
        "Check Source Control",
        "Write commit message",
        "Commit and Sync",
        "Check GitHub Web"
    ]

    print()
    print("Today's GitHub checklist:")
    for task in tasks:
        print("✅", task)

show_summary(name, device, minutes, goal)
show_checklist()

print()
if minutes >= 25:
    print("Excellent! Level 166 practice complete ✅")
else:
    print("Good start! Keep practicing step by step.")

print()
print("Copilot question:")
print("Can you improve this Python program and make the output cleaner?")