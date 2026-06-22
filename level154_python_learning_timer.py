print("🐍 Level 154 Python Learning Timer")

name = input("Enter your name: ")
device = input("Are you using Surface or iMac? ")
minutes = int(input("How many minutes are you learning Python today? "))
topic = input("What Python topic are you practicing? ")

learning_steps = [
    "Open VS Code",
    "Create a new Python file",
    "Type Python code carefully",
    "Run the Python file",
    "Fix any mistake step by step",
    "Commit and Sync to GitHub"
]

print()
print("Hello", name)
print("Today you are learning Python on:", device)
print("Your topic today is:", topic)
print("Your learning time:", minutes, "minutes")

print()
print("Today's learning checklist:")
for step in learning_steps:
    print("✅", step)

print()
if minutes >= 25:
    print("Excellent! 25 minutes Python learning complete ✅")
else:
    print("Good start! Keep learning step by step.")

print("Level 154 complete! 🚀")