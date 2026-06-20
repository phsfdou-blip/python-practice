print("🤖 Level 150 AI Copilot GitHub Web Practice")

name = input("Enter your name: ")
minutes = int(input("How many minutes are you practicing today? "))
goal = input("What is today's learning goal? ")

tasks = [
    "Write Python code in VS Code",
    "Use AI Copilot to explain or improve code",
    "Run the Python file",
    "Commit and Sync Changes",
    "Check the file on GitHub Web"
]

print()
print("Hello", name)
print("Today you are practicing VS Code, AI Copilot, and GitHub Web.")
print("Practice time:", minutes, "minutes")
print("Learning goal:", goal)

print()
print("Today's checklist:")
for task in tasks:
    print("-", task)

if minutes >= 20:
    print("Great job! 20 minutes VS Code AI Copilot GitHub Web practice complete ✅")
else:
    print("Good start! Keep practicing step by step.")

print("Level 150 complete! 🚀")