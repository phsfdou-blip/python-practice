print("🚀 Level 96 Safe Driver Trip Checker")

name = input("Enter your name: ")

try:
    miles = float(input("How many miles is the trip? "))
    passengers = int(input("How many passengers? "))

    if miles <= 0:
        print("Miles must be more than 0 ❌")
    elif passengers < 0:
        print("Passengers cannot be negative ❌")
    else:
        print(f"\nGreat job {name}!")
        print("Trip miles =", miles)
        print("Passengers =", passengers)

        if miles >= 80 and passengers >= 20:
            print("Result: Long busy shuttle trip 🚍")
        elif miles >= 80:
            print("Result: Long trip ✅")
        elif passengers >= 20:
            print("Result: Busy passenger trip ✅")
        else:
            print("Result: Normal trip 👍")

except:
    print("Invalid input ❌ Please enter numbers only.")