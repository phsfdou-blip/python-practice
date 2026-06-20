
print("🤖 Level 151 AI Copilot GitHub Review Practice")

name = input("Enter your name: ")
minutes = int(input("How many minutes are you practicing today? "))
github_check = input("Did you check GitHub Web today? ")

review_tasks = [
    "Use AI Copilot to review one Python file",
    "Ask Copilot to explain one line",
    "Ask Copilot to suggest one improvement",
    "Run the Python file in VS Code",
    "Commit and Sync Changes",
    "Confirm the file on GitHub Web"
]

print()
print("Hello", name)
print("Today you are practicing AI Copilot and GitHub Web review.")
print("Practice time:", minutes, "minutes")
print("GitHub Web checked:", github_check)

print()
print("Today's review checklist:")
for task in review_tasks:
    print("-", task)

if minutes >= 25:
    print("Excellent! 25 minutes AI Copilot GitHub Web practice complete ✅")
else:
    print("Good start! Keep practicing step by step.")

print("Level 151 complete! 🚀")