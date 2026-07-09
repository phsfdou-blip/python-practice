print("🤖 Level 165 VS Code + AI Copilot Input Review")

name = input("Enter your name: ")
device = input("Are you using Surface or iMac? ")
minutes = int(input("How many minutes are you practicing today? "))

def show_summary(name, device, minutes):
    print()
    print("Hello", name)
    print("Today you practiced VS Code with AI Copilot.")
    print("Device:", device)
    print("Practice time:", minutes, "minutes")

def check_goal(minutes):
    print()
    if minutes >= 20:
        print("Excellent! You reached your 20-minute practice goal ✅")
    else:
        print("Good start! Keep practicing step by step.")

show_summary(name, device, minutes)
check_goal(minutes)