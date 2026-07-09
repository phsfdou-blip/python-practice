print("🤖 Level 185 VS Code + Copilot Try/Except Input Practice")

name = input("Enter your name: ")
device = input("Are you using Surface or iMac? ")

try:
    minutes = int(input("How many minutes are you practicing today? "))
except ValueError:
    print()
    print("Please enter a number next time.")
    minutes = 0

def show_summary(name, device, minutes):
    print()
    print("Hello", name)
    print("Today you practiced VS Code with AI Copilot and GitHub Web.")
    print("Device:", device)
    print("Practice time:", minutes, "minutes")

def check_goal(minutes):
    if minutes >= 25:
        print()
        print("Excellent! You reached your 25-minute practice goal.")
    else:
        print()
        print("Good start. Keep practicing step by step.")

show_summary(name, device, minutes)
check_goal(minutes)