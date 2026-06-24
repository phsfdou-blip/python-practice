print("🤖 Level 159 AI Copilot Function Practice")

name = input("Enter your name: ")
device = input("Are you using Surface or iMac? ")
minutes = int(input("How many minutes are you practicing today? "))
ai_tool = input("Which AI tool are you using today? ChatGPT or GitHub Copilot? ")

def show_learning_summary(name, device, minutes, ai_tool):
    print()
    print("Hello", name)
    print("Today you are practicing VS Code with AI Copilot.")
    print("Device:", device)
    print("AI tool:", ai_tool)
    print("Practice time:", minutes, "minutes")

def show_tasks():
    tasks = [
        "Open VS Code",
        "Open python-practice folder",
        "Create Level 159 Python file",
        "Ask AI Copilot to explain one function",
        "Run the Python program",
        "Check Source Control",
        "Write commit message",
        "Commit and Sync",
        "Check GitHub Web"
    ]

    print()
    print("Today's AI Copilot checklist:")
    for task in tasks:
        print("✅", task)

show_learning_summary(name, device, minutes, ai_tool)
show_tasks()

print()
if minutes >= 20:
    print("Excellent! 20 minutes VS Code AI Copilot practice complete ✅")
else:
    print("Good start! Keep practicing step by step.")

print()
print("Copilot question:")
print("Ask GitHub Copilot: Can you explain what the function show_tasks() does?")

print()
print("Level 159 complete! 🚀")