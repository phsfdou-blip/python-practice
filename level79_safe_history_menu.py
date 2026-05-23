
print("🚀 Level 79 Safe History Menu")

numbers = []

while True:

    print("\n1. Add Number")
    print("2. Show History")
    print("3. Show Average")
    print("4. Clear History")
    print("5. Exit")

    choice = input("Choose (1-5): ")

    if choice == "1":

        try:

            number = float(input("Enter a number: "))

            numbers.append(number)

            print("Added:", number)

        except:

            print("Invalid number ❌")

    elif choice == "2":

        print("History:", numbers)

    elif choice == "3":

        if len(numbers) > 0:

            average = sum(numbers) / len(numbers)

            print("Average =", round(average, 2))

        else:

            print("No numbers yet ❌")

    elif choice == "4":

        numbers.clear()

        print("History cleared 🧹")

    elif choice == "5":

        print("Goodbye Phillip! 👋")

        break

    else:

        print("Invalid choice ❌")

print("Win win win! 🔥")