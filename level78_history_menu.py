print("🚀 Level 78 History Menu")

numbers = []

while True:

    print("\n1. Add Number")
    print("2. Show History")
    print("3. Show Average")
    print("4. Exit")

    choice = input("Choose (1-4): ")

    if choice == "1":

        number = int(input("Enter a number: "))
        numbers.append(number)

        print("Added:", number)

    elif choice == "2":

        print("History:", numbers)

    elif choice == "3":

        if len(numbers) > 0:

            average = sum(numbers) / len(numbers)

            print("Average =", round(average, 2))

        else:
            print("No numbers yet ❌")

    elif choice == "4":

        print("Goodbye Phillip! 👋")
        break

    else:
        print("Invalid choice ❌")

print("Win win win! 🔥")
