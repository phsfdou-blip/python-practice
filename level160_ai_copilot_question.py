print("🤖 Level 160 AI Copilot Question Practice")

name = input("Enter your name: ")
device = input("Are you using Surface or iMac? ")
minutes = int(input("How many minutes are you practicing today? "))
question = input("What AI Copilot question do you want to ask today? ")

def show_practice_summary(name, device, minutes, question):
    print()
    print("Hello", name)
    print("Today you are practicing AI Copilot with VS Code and GitHub Web.")
    print("Device:", device)
    print("Practice time:", minutes, "minutes")
    print("Your Copilot question:", question)

def show_github_steps():
    steps = [
        "Open VS Code",
        "Open python-practice folder",
        "Create Level 160 Python file",
        "Ask Copilot one question",
        "Run the Python program",
        "Check Source Control",
        "Write commit message",
        "Commit and Sync",
        "Check GitHub Web"
    ]

    print()
    print("Today's GitHub checklist:")
    for step in steps:
        print("✅", step)

show_practice_summary(name, device, minutes, question)
show_github_steps()

print()
if minutes >= 20:
    print("Excellent! 20 minutes AI Copilot practice complete ✅")
else:
    print("Good start! Keep practicing step by step.")

print("Level 160 complete! 🚀")