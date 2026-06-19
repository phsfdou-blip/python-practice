print("🤖 Level 143 AI Dictionary Practice")

name = input("Enter your name: ")
topic = input("What AI topic are you practicing today? ")
minutes = int(input("How many minutes are you practicing today? "))

ai_helper = {
    "explain": "Ask AI to explain one Python line",
    "improve": "Ask AI to improve one print sentence",
    "debug": "Ask AI to find one possible mistake",
    "summary": "Ask AI to summarize what this program does"
}

print("Hello", name)
print("Today you are practicing AI with Python and VS Code.")
print("Your AI topic today is:", topic)

print("Your AI helper menu:")
for key, task in ai_helper.items():
    print(key, ":", task)

if minutes >= 15:
    print("Great job! 15 minutes AI VS Code practice complete ✅")
else:
    print("Good start! Keep practicing step by step.")

print("Level 143 complete! 🚀")