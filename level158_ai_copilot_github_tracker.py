print("🤖 Level 158 AI Copilot GitHub Web Progress Tracker")

name = input("Enter your name: ")
device = input("Are you using Surface or iMac? ")
minutes = int(input("How many minutes are you practicing today? "))
ai_tool = input("Which AI tool are you practicing? ChatGPT or GitHub Copilot? ")
github_status = input("Did you check GitHub Web today? yes or no: ")

practice_steps = [
    "Open VS Code",
    "Open python-practice folder",
    "Create a new Python file",
    "Ask AI Copilot to explain one line",
    "Run the Python program",
    "Check Source Control",
    "Write commit message",
    "Commit and Sync",
    "Check GitHub Web"
]

print()
print("Hello", name)
print("Today you are practicing VS Code, AI Copilot, and GitHub Web.")
print("Device:", device)
print("AI tool:", ai_tool)
print("Practice time:", minutes, "minutes")
print("GitHub Web checked:", github_status)

print()
print("Today's practice checklist:")
for step in practice_steps:
    print("✅", step)

print()
if minutes >= 25 and github_status == "yes":
    print("Excellent! 25 minutes complete and GitHub Web checked ✅")
elif minutes >= 25:
    print("Great 25 minutes practice! Remember to check GitHub Web.")
else:
    print("Good start! Keep practicing step by step.")

print()
print("AI Copilot question:")
print("Ask Copilot or ChatGPT: What does this if / elif / else part mean?")

print("Level 158 complete! 🚀")