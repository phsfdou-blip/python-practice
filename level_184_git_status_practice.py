print("🚀 Level 184 VS Code Git Status Practice")

name = input("Enter your name: ")
minutes = int(input("How many minutes are you practicing today? "))

tasks = [
    "Open VS Code",
    "Check correct python-practice folder",
    "Create Level 184 Python file",
    "Run the Python program",
    "Check git status",
    "Add the file",
    "Commit the file",
    "Push to GitHub",
    "Check GitHub Web"
]

print()
print("Hello", name)
print("Today you are practicing VS Code and Git.")
print("Practice time:", minutes, "minutes")

print()
print("Today's tasks:")
for task in tasks:
    print("✅", task)

if minutes >= 10:
    print()
    print("Great job! You completed your 10-minute practice.")
else:
    print()
    print("Good start! Keep practicing.")