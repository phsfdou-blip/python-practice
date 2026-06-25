print("🤖 Level 161 AI Copilot Question Practice")

name = input("Enter your name: ")
device = input("Are you using Surface or iMac? ")
minutes = int(input("How many minutes are you practicing today? "))
question = input("What Copilot question did you ask today? ")

def show_summary(name, device, minutes, question):
    print()
    print("Hello", name)
    print("Today you practiced VS Code with AI Copilot.")
    print("Device:", device)
    print("Practice time:", minutes, "minutes")
    print("Copilot question:", question)

def show_next_steps():
    steps = [
        "Open VS Code",
        "Create Level 161 Python file",
        "Ask Copilot one question",
        "Read Copilot answer",
        "Run the Python program",
        "Fix any mistake",
        "Commit and Sync",
        "Check GitHub Web"
    ]

    print()
    print("Today's checklist:")
    for step in steps:
        print("✅", step)

show_summary(name, device, minutes, question)
show_next_steps()

if minutes >= 20:
    print()
    print("Excellent! 20 minutes AI Copilot practice complete 🚀")
else:
    print()
    print("Good start! Keep practicing step by step.")