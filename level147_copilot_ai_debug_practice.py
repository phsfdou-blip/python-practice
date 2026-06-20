
print("🐞 Level 147 Copilot AI Debug Practice")

name = input("Enter your name: ")
minutes = int(input("How many minutes are you practicing today? "))

debug_tasks = [
    "Read the error message",
    "Ask Copilot to explain the error",
    "Find the line with the problem",
    "Fix the code",
    "Run the program again"
]

print()
print("Hello", name)
print("Today you are practicing Copilot AI debugging.")
print("Practice time:", minutes, "minutes")

print()
print("Your debug checklist:")
for task in debug_tasks:
    print("-", task)

if minutes >= 20:
    print("Great job! 20 minutes debug practice complete ✅")
else:
    print("Good start! Keep debugging step by step.")

print("Level 147 complete! 🚀")