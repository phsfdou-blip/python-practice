
print("🎾 Level 115 Tennis Water Reminder")

name = input("Enter your name: ")

minutes = int(input("How many minutes did you play tennis today? "))
water = input("Did you drink water? yes/no: ")

if minutes <= 0:
    print("No tennis practice today.")
elif minutes < 30:
    print("Good short practice", name)
elif minutes <= 90:
    print("Great tennis practice", name)
else:
    print("Long tennis practice", name)

if water == "yes":
    print("Good job staying hydrated 💧")
elif water == "no":
    print("Please drink water after tennis 💧")
else:
    print("Please answer yes or no next time.")