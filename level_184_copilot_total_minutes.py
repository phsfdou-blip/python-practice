print("🤖 Level 184 VS Code + AI Copilot Total Minutes Practice")

name = input("Enter your name: ")
device = input("Are you using Surface or iMac? ")

def add_minutes(minutes_list):
    total = 0

    for minutes in minutes_list:
        total = total + minutes

    return total

practice_minutes = [10, 15, 25]

total_minutes = add_minutes(practice_minutes)

print()
print("Hello", name)
print("Today you practiced VS Code with AI Copilot.")
print("Device:", device)
print("Practice minutes list:", practice_minutes)
print("Total practice minutes:", total_minutes)

if total_minutes >= 25:
    print()
    print("Excellent! You reached your 25-minute practice goal.")
else:
    print()
    print("Good start. Keep practicing step by step.")