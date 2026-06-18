print("🤖 Level 142 AI Helper List Practice")

name = input("Enter your name: ")
topic = input("What AI topic do you want to practice today? ")
minutes = int(input("How many minutes are you practicing today? "))

ai_tasks = [
    "Ask ChatGPT to explain one Python line",
    "Ask Copilot to suggest one improvement",
    "Ask AI to find one possible mistake",
    "Ask AI to make the code easier to read"
]

print("Hello", name)
print("Today you are practicing AI with Python and VS Code.")
print("Your topic today is:", topic)

print("Your AI helper tasks:")
for task in ai_tasks:
    print("-", task)

if minutes >= 15:
    print("Great job! 15 minutes AI VS Code practice complete ✅")
else:
    print("Good start! Keep practicing step by step.")

print("Level 142 complete! 🚀")