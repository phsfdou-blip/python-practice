print("🤖 Level 146 Copilot AI Practice")

name = input("Enter your name: ")
tool = input("Which AI tool are you practicing today? ")
minutes = int(input("How many minutes are you practicing today? "))

copilot_tasks = [
    "Ask Copilot to explain this program",
    "Ask Copilot to suggest one better variable name",
    "Ask Copilot to improve one print sentence",
    "Ask Copilot to find one possible mistake",
    "Ask Copilot to suggest the next Python practice idea"
]

print()
print("Hello", name)
print("Today you are practicing AI help with VS Code.")
print("AI tool:", tool)
print("Practice time:", minutes, "minutes")

print()
print("Your Copilot AI tasks:")
for task in copilot_tasks:
    print("-", task)

if minutes >= 20:
    print("Great job! 20 minutes Copilot AI practice complete ✅")
else:
    print("Good start! Keep learning step by step.")

print("Level 146 complete! 🚀")