print("🤖 Level 194 VS Code + AI Copilot Continue Practice")

name = input("Enter your name: ")

attempts = 0
total_minutes = 0

while attempts < 3:
    try:
        minutes = int(input("Enter practice minutes: "))

        if minutes <= 0:
            print("Please enter a number greater than 0.")
            attempts += 1
            continue

        total_minutes += minutes
        attempts += 1
        print("Practice time added.")

    except ValueError:
        print("Please enter a whole number.")
        attempts += 1
        continue

print()
print("Hello", name)
print("Total practice minutes:", total_minutes)

if total_minutes >= 30:
    print("Excellent! You reached your 30-minute goal.")
else:
    print("Good work! Keep practicing.")

print("Practice program finished.")