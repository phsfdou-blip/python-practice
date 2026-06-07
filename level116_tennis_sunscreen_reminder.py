
print("🎾 Level 116 Tennis Sunscreen Reminder")

name = input("Enter your name: ")

minutes = int(input("How many minutes did you play tennis today? "))
water = input("Did you drink water? yes/no: ")
sunscreen = input("Did you use sunscreen? yes/no: ")

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
    print("Please answer yes or no for water next time.")

if sunscreen == "yes":
    print("Good job protecting your skin ☀️")
elif sunscreen == "no":
    print("Please use sunscreen before tennis ☀️")
else:
    print("Please answer yes or no for sunscreen next time.")