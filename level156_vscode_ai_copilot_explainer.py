print("🤖 Level 156 VS Code AI Copilot Code Explainer")

name = input("Enter your name: ")
device = input("Are you using Surface or iMac? ")
minutes = int(input("How many minutes are you practicing today? "))
python_line = input("Type one Python line you want AI Copilot to explain: ")

copilot_steps = [
    "Open VS Code",
    "Create a new Python file",
    "Type or paste one Python line",
    "Ask Copilot to explain the line",
    "Run the Python file",
    "Check Source Control",
    "Write Commit Message",
    "Commit and Sync",
    "Check GitHub Web"
]

print()
print("Hello", name)
print("Today you are practicing VS Code AI Copilot.")
print("Device:", device)
print("Practice time:", minutes, "minutes")

print()
print("Python line for AI Copilot to explain:")
print(python_line)

print()
print("Today's Copilot practice checklist:")
for step in copilot_steps:
    print("✅", step)

print()
if minutes >= 20:
    print("Excellent! 20 minutes VS Code AI Copilot practice complete ✅")
else:
    print("Good start! Keep learning step by step.")

print("Level 156 complete! 🚀")