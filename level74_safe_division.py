
print("🚀 Level 74 Safe Division Menu")

while True:

    print("\n1. Addition")
    print("2. Multiplication")
    print("3. Division")
    print("4. Exit")

    choice = input("Choose (1-4): ")

    if choice == "1":

        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))

        print("Answer:", num1 + num2)

    elif choice == "2":

        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))

        print("Answer:", num1 * num2)

    elif choice == "3":

        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))

        if num2 == 0:
            print("Cannot divide by zero ❌")
        else:
            answer = num1 / num2
            print("Answer:", round(answer, 2))
    
    elif choice == "4":

        print("Goodbye Phillip! 👋")
        break

    else:
        print("Invalid choice ❌")

print("Great work Phillip! 🔥")
print("Win win win! 🚀")