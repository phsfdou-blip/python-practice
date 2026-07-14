print("🤖 Level 190 VS Code + AI Copilot Limited Attempts Practice")

name = input("Enter your name: ")
device = input("Are you using Surface or iMac? ")

attempts = 0
minutes = 0

while attempts < 3:
    try:
        minutes = int(input("How many minutes are you practicing today? "))

        if minutes > 0:
            break
        else:
            print("Please enter a number greater than 0.")

    except ValueError:
        print("Please enter a whole number.")

    attempts = attempts + 1
    print("Attempts used:", attempts)

print()

if minutes > 0:
    print("Hello", name)
    print("Device:", device)
    print("Today's practice:", minutes, "minutes")

    if minutes >= 20:
        print("Excellent! You reached your 20-minute goal.")
    else:
        print("Good practice! Keep building your skills.")
else:
    print("Too many invalid attempts. Please try again later.")