print("🤖 Level 180 VS Code Practice")

name = input("Enter your name: ")
device = input("Are you using Surface or iMac? ")
minutes = int(input("How many minutes are you practicing today? "))

def show_summary(name, device, minutes):
    print()
    print("Hello", name)
    print("Today you practiced VS Code.")
    print("Device:", device)
    print("Practice time:", minutes, "minutes")

def show_tasks():
    tasks = [
        "Open VS Code",
        "Check correct folder",
        "Create clean Python file name",
        "Run Python program",
        "Check Source Control",
        "Commit and Sync",
        "Check GitHub Web"
    ]

    print()
    print("Tonight's tasks:")
    for task in tasks:
        print("✅", task)

show_summary(name, device, minutes)
show_tasks()

if minutes >= 15:
    print()
    print("Excellent! 15 minutes VS Code practice complete ✅")
else:
    print()
    print("Good start! Keep practicing step by step.")