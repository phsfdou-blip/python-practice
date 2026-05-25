print("🚀 Level 85 Smart Stats Report")

numbers = []

while True:
    print("\n1. Add Number")
    print("2. Show History")
    print("3. Smart Stats Report")
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
            total = sum(numbers)
            count = len(numbers)
            average = total / count
            highest = max(numbers)
            lowest = min(numbers)

            print("\n📊 Smart Stats Report")
            print("----------------------")
            print("Count =", count)
            print("Total =", total)
            print("Average =", round(average, 2))
            print("Max =", highest)
            print("Min =", lowest)
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