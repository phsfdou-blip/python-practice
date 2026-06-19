print("🤖 Level 144 AI VS Code Helper Practice.")
print("🤖 Level 144 AI VS Code Helper Practice")

name = input("Enter your name: ")
topic = input("What AI topic are you practicing today? ")
minutes = int(input("How many minutes are you practicing today? "))

ai_helpers = [
    "Explain one Python line",
    "Find one possible mistake",
    "Improve one print sentence",
    "Summarize what this program does",
    "Suggest one next learning step"
]

print()
print("Hello", name)
print("Today you are practicing AI with Python and VS Code.")
print("Your AI topic today is:", topic)
print("Practice time:", minutes, "minutes")

print()
print("Your AI helper checklist:")
for helper in ai_helpers:
    print("-", helper)

if minutes >= 20:
    print("Great job! 20 minutes AI VS Code practice complete ✅")
else:
    print("Good start! Keep practicing step by step.")

print("Level 144 complete! 🚀")