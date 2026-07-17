print("🤖 Level 193 While-Else-Break Review")

attempts = 0

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
    print("You used all three attempts.")

print("Practice program finished.")