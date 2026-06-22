print("🤖 Level 155 VS Code AI GitHub 20-Minute Practice")

name = input("Enter your name: ")
device = input("Are you using Surface or iMac? ")
minutes = int(input("How many minutes are you practicing today? "))
ai_tool = input("Which AI tool are you using? ChatGPT or Copilot? ")

tasks = [
    "Open VS Code",
    "Create a new Python file",
    "Ask AI to explain one Python line",
    "Run the Python file",
    "Check Source Control",
    "Write Commit Message",
    "Commit and Sync",
    "Check GitHub Web"
]

print()
print("Hello", name)
print("Today you are practicing VS Code, AI, and GitHub.")
print("Device:", device)
print("AI tool:", ai_tool)
print("Practice time:", minutes, "minutes")

print()
print("Today's practice checklist:")
for task in tasks:
    print("✅", task)

print()
if minutes >= 20:
    print("Excellent! 20 minutes VS Code AI GitHub practice complete ✅")
else:
    print("Good start! Keep learning step by step.")

print("Level 155 complete! 🚀")