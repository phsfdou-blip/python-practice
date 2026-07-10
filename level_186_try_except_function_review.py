print("🤖 Level 186 VS Code + AI Copilot Try/Except Function Review")

name = input("Enter your name: ")
device = input("Are you using Surface or iMac? ")

def get_minutes():
    try:
        minutes = int(input("How many minutes are you practicing today? "))
        return minutes
    except ValueError:
        print()
        print("Please enter a whole number next time.")
        return 0

def show_summary(name, device, minutes):
    print()
    print("Hello", name)
    print("Today you practiced VS Code with AI Copilot.")
    print("Device:", device)
    print("Practice time:", minutes, "minutes")

def check_goal(minutes):
    if minutes >= 25:
        print()
        print("Excellent! You reached your 25-minute practice goal.")
    else:
        print()
        print("Good start. Keep practicing step by step.")

minutes = get_minutes()

show_summary(name, device, minutes)
check_goal(minutes)