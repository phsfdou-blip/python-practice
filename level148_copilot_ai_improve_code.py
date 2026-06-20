print("🤖 Level 148 Copilot AI Improve Code Practice")

name = input("Enter your name: ")
topic = input("What Python topic are you practicing today? ")
minutes = int(input("How many minutes are you practicing today? "))

copilot_improvements = [
    "Make one print sentence clearer",
    "Suggest one better variable name",
    "Explain one if statement",
    "Explain one for loop",
    "Suggest one next feature for this program"
]

print()
print("Hello", name)
print("Today you are practicing Python with Copilot AI.")
print("Python topic:", topic)
print("Practice time:", minutes, "minutes")

print()
print("Copilot improvement checklist:")
for improvement in copilot_improvements:
    print("-", improvement)

if minutes >= 25:
    print("Excellent! 25 minutes Copilot AI practice complete ✅")
else:
    print("Good start! Keep improving step by step.")

print("Level 148 complete! 🚀")