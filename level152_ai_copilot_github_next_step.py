print("🤖 Level 152 AI Copilot GitHub Web Next Step")

name = input("Enter your name: ")
minutes = int(input("How many minutes are you practicing today? "))
ai_goal = input("What AI Copilot skill do you want to improve today? ")
github_status = input("Did GitHub Web show your last file correctly? ")

next_steps = [
    "Open VS Code",
    "Write a Python practice file",
    "Ask AI Copilot to explain the code",
    "Ask AI Copilot to suggest one improvement",
    "Run the program",
    "Commit and Sync Changes",
    "Check GitHub Web"
]

print()
print("Hello", name)
print("Today you are practicing VS Code, AI Copilot, and GitHub Web.")
print("Practice time:", minutes, "minutes")
print("AI Copilot goal:", ai_goal)
print("GitHub Web status:", github_status)

print()
print("Level 152 checklist:")
for step in next_steps:
    print("-", step)

if minutes >= 20:
    print("Great job! Level 152 practice complete ✅")
else:
    print("Good start! Keep practicing step by step.")

print("Level 152 complete! 🚀")