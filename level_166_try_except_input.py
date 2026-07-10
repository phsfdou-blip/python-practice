print("🤖 Level 166 VS Code + AI Copilot Try/Except Input Practice")

name = input("Enter your name: ")
device = input("Are you using Surface or iMac? ")

try:
    minutes = int(input("How many minutes are you practicing today? "))

    print()
    print("Hello", name)
    print("Today you practiced VS Code with AI Copilot.")
    print("Device:", device)
    print("Practice time:", minutes, "minutes")

    if minutes >= 20:
        print("Excellent! You reached your 20-minute practice goal.")
    else:
        print("Good start. Keep practicing step by step.")

except ValueError:
    print()
    print("Please enter a whole number for minutes, like 20.")