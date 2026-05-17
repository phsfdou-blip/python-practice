
print("🚀 Level 70 Smart Modulus Menu")

while True:

    print("\n1. Even or Odd")
    print("2. Positive or Negative")
    print("3. Exit")

    choice = input("Choose (1-3): ")

    if choice == "1":

        number = int(input("Enter a number: "))

        if number % 2 == 0:
            print("Even number ✅")
        else:
            print("Odd number ✅")

    elif choice == "2":

        number = int(input("Enter a number: "))

        if number > 0:
            print("Positive number ✅")

        elif number < 0:
            print("Negative number ✅")

        else:
            print("Zero ✅")

    elif choice == "3":
        print("Goodbye Phillip! 👋")
        break

    else:
        print("Invalid choice ❌")

print("Win win win! 🔥")