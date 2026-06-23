print("🤖 Level 157 AI Copilot Commit Helper Practice")

name = input("Enter your name: ")
device = input("Are you using Surface or iMac? ")
minutes = int(input("How many minutes are you practicing today? "))
commit_message = input("What is your GitHub commit message today? ")

github_steps = [
    "Save the Python file",
    "Run the program",
    "Check Source Control",
    "Review changed file",
    "Write commit message",
    "Click Commit",
    "Click Sync Changes",
    "Check GitHub Web"
]

print()
print("Hello", name)
print("Today you are practicing AI Copilot, VS Code, and GitHub commit skills.")
print("Device:", device)
print("Practice time:", minutes, "minutes")
print("Commit message:", commit_message)

print()
print("GitHub practice checklist:")
for step in github_steps:
    print("✅", step)

print()
if minutes >= 25:
    print("Excellent! 25 minutes GitHub Web practice complete ✅")
else:
    print("Good start! Keep practicing step by step.")

print()
print("Copilot task:")
print("Ask Copilot: Can you make my checklist sentence clearer?")

print("Level 157 complete! 🚀")