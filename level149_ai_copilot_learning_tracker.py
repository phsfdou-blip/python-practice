
print("🤖 Level 149 AI Copilot Learning Tracker")

name = input("Enter your name: ")
word_minutes = int(input("Word minutes: "))
excel_minutes = int(input("Excel minutes: "))
copilot_minutes = int(input("VS Code AI Copilot minutes: "))

total_minutes = word_minutes + excel_minutes + copilot_minutes
average_minutes = total_minutes / 3

copilot_tasks = [
    "Ask Copilot to explain this program",
    "Ask Copilot to improve one sentence",
    "Ask Copilot to suggest one better variable name",
    "Ask Copilot to find one possible mistake",
    "Ask Copilot to suggest the next Python level"
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
print("Your Copilot AI checklist:")
for task in copilot_tasks:
    print("-", task)

if total_minutes >= 60:
    print("Excellent! One hour learning completed ✅")
else:
    print("Good start! Keep learning step by step.")

print("Level 149 complete! 🚀")