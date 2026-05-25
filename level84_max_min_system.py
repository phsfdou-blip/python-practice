
print("🚀 Level 84 Max + Min System")

numbers = []

while True:
    print("\n1. Add Number")
    print("2. Show History")
    print("3. Count Numbers")
    print("4. Show Total")
    print("5. Show Average")
    print("6. Show Max")
    print("7. Show Min")
    print("8. Clear History")
    print("9. Exit")

    choice = input("Choose (1-9): ")

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
        if len(numbers) > 0:
            print("Max =", max(numbers))
        else:
            print("No numbers yet ❌")

    elif choice == "7":
        if len(numbers) > 0:
            print("Min =", min(numbers))
        else:
            print("No numbers yet ❌")

    elif choice == "8":
        numbers.clear()
        print("History cleared 🧹")

    elif choice == "9":
        print("Goodbye Phillip! 👋")
        break

    else:
        print("Invalid choice ❌")