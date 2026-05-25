print("🚀 Level 82 Counter Numbers + Clear History")

numbers = []

while True:
    print("\n1. Add Number")
    print("2. Show History")
    print("3. Count Numbers")
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
        print("Count =", len(numbers))

    elif choice == "4":
        numbers.clear()
        print("History cleared 🧹")

    elif choice == "5":
        print("Goodbye Phillip! 👋")
        break

    else:
        print("Invalid choice ❌")