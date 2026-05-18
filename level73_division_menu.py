print("🚀 Level 73 Division Menu")

while True:

    print("\n1. Addition")
    print("2. Multiplication")
    print("3. Square")
    print("4. Cube")
    print("5. Division")
    print("6. Exit")

    choice = input("Choose (1-6): ")

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

        number = int(input("Enter a number: "))

        print("Cube:", number ** 3)

    elif choice == "5":

        num1 = int(input("First number: "))
        num2 = int(input("Second number: "))

        print("Answer:", num1 / num2)

    elif choice == "6":

        print("Goodbye Phillip! 👋")
        break

    else:

        print("Invalid choice ❌")

print("Win win win! 🔥")