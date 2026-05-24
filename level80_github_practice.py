print("🚀 Level 80 GitHub Practice")

numbers = []

while True:
    print("\n1. Add Number")
    print("2. Show History")
    print("3. Show Total")
    print("4. Show Average")
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
        print("Total =", sum(numbers))

    elif choice == "4":
        if len(numbers) > 0:
            average = sum(numbers) / len(numbers)
            print("Average =", round(average, 2))
        else:
            print("No numbers yet ❌")

    elif choice == "5":
        print("Goodbye Phillip! 👋")
        break

    else:
        print("Invalid choice ❌")