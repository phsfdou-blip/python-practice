
print("🎾 Level 114 Tennis Practice Checker")

name = input("Enter your name: ")

minutes = int(input("How many minutes did you play tennis today? "))

if minutes <= 0:
    print("No tennis practice today.")
elif minutes < 30:
    print("Good small practice", name)
elif minutes <= 90:
    print("Great tennis practice", name)
else:
    print("Wow", name, "long tennis practice! Remember water and sunscreen.")