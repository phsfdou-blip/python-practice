print("🤖 Level 191 VS Code + AI Copilot Try/Except Else Practice")

name = input("Enter your name: ")
device = input("Are you using Surface or iMac? ")

attempts = 0
minutes = 0

while attempts < 3:
    try:
        minutes = int(input("How many minutes are you practicing today? "))

        if minutes <= 0:
            print("Please enter a number greater than 0.")
            attempts += 1
        else:
            break

    except ValueError:
        print("Please enter a whole number.")
        attempts += 1

if attempts == 3:
    print()
    print("You used all 3 attempts.")
else:
    print()
    print("Hello", name)
    print("Device:", device)
    print("Today's practice:", minutes, "minutes")

    if minutes >= 25:
        print("Excellent! You reached your 25-minute goal.")
    else:
        print("Good practice! Keep working toward 25 minutes.")