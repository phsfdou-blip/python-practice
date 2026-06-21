
print("🤖 Level 153 AI Copilot Office Tracker")

name = input("Enter your name: ")
word_minutes = int(input("Word minutes: "))
excel_minutes = int(input("Excel minutes: "))
copilot_minutes = int(input("VS Code AI Copilot minutes: "))

total_minutes = word_minutes + excel_minutes + copilot_minutes
average_minutes = total_minutes / 3

learning_tasks = [
    "Write a Word learning summary",
    "Practice Excel formulas",
    "Use AI Copilot to explain Python code",
    "Run the Python file in VS Code",
    "Commit and Sync Changes",
    "Check GitHub Web"
]

print()
print("Hello", name)
print("Today you practiced Word, Excel, and VS Code AI Copilot.")
print("Word:", word_minutes, "minutes")
print("Excel:", excel_minutes, "minutes")
print("VS Code AI Copilot:", copilot_minutes, "minutes")
print("Total practice time:", total_minutes, "minutes")
print("Average practice time:", average_minutes, "minutes")

print()
print("Level 153 learning checklist:")
for task in learning_tasks:
    print("-", task)

if total_minutes >= 60:
    print("Excellent! One hour learning completed ✅")
else:
    print("Good start! Keep learning step by step.")

print("Level 153 complete! 🚀")