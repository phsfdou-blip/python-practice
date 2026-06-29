
print("🤖 Level 168 VS Code + AI Copilot Next Step Practice")

name = input("Enter your name: ")
device = input("Are you using Surface or iMac? ")
minutes = int(input("How many minutes are you practicing today? "))
topic = input("What are you practicing today? ")

def show_summary(name, device, minutes, topic):
    print()
    print("Hello", name)
    print("Today you practiced VS Code with AI Copilot.")
    print("Device:", device)
    print("Practice time:", minutes, "minutes")
    print("Topic:", topic)

def show_steps():
    steps = [
        "Check correct folder",
        "Create new Python file",
        "Run Python program",
        "Ask AI Copilot one question",
        "Check Source Control",
        "Commit changes",
        "Sync to GitHub",
        "Check GitHub Web"
    ]

    print()
    print("Today's next-step checklist:")
    for step in steps:
        print("✅", step)

show_summary(name, device, minutes, topic)
show_steps()

print()
if minutes >= 20:
    print("Excellent! Level 168 practice complete ✅")
else:
    print("Good start! Keep practicing step by step.")

print()
print("Copilot question:")
print("Can you explain this Python checklist program step by step?")