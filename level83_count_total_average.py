
print("🚀 Level 83 Count + Total + Average")

numbers = []

while True:
    print("\n1. Add Number")
    print("2. Show History")
    print("3. Count Numbers")
    print("4. Show Total")
    print("5. Show Average")
    print("6. Clear History")
    print("7. Exit")

    choice = input("Choose (1-7): ")

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
        print("Count =", len(numbers))

    elif choice == "4":
        print("Total =", sum(numbers))

    elif choice == "5":
        if len(numbers) > 0:
            average = sum(numbers) / len(numbers)
            print("Average =", round(average, 2))
        else:
            print("No numbers yet ❌")

    elif choice == "6":
        numbers.clear()
        print("History cleared 🧹")

    elif choice == "7":
        print("Goodbye Phillip! 👋")
        break

    else:
        print("Invalid choice ❌")