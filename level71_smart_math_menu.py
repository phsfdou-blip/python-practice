
print("🚀 Level 71 Smart Math Menu")

while True:

    print("\n1. Addition")
    print("2. Multiplication")
    print("3. Square")
    print("4. Exit")

    choice = input("Choose (1-4): ")

    if choice == "1":

        num1 = int(input("First number: "))
        num2 = int(input("Second number: "))

        print("Answer:", num1 + num2)

    elif choice == "2":

        num1 = int(input("First number: "))
        num2 = int(input("Second number: "))

        print("Answer:", num1 * num2)

    elif choice == "3":

        number = int(input("Enter a number: "))

        print("Square:", number ** 2)

    elif choice == "4":

        print("Goodbye Phillip! 👋")
        break

    else:
        print("Invalid choice ❌")

print("Win win win! 🔥")