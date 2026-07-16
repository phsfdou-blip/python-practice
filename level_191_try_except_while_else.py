print("🤖 Level 191 Try/Except While-Else Practice")

name = input("Enter your name: ")
device = input("Are you using Surface or iMac? ")

attempts = 0
minutes = 0

while attempts < 3:
    try:
        minutes = int(input("How many minutes are you practicing today? "))

        if minutes > 0:
            print("Valid practice time entered.")
            break
        else:
            print("Please enter a number greater than 0.")
            attempts += 1

    except ValueError:
        print("Please enter a whole number.")
        attempts += 1

else:
    print("You used all 3 attempts.")

print()

if minutes > 0:
    print("Hello", name)
    print("Device:", device)
    print("Today's practice:", minutes, "minutes")

    if minutes >= 20:
        print("Excellent! You reached your 20-minute goal.")
    else:
        print("Good practice. Keep working step by step.")
else:
    print("No valid practice time was entered.")