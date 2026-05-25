print("🚀 Level 88 Save Numbers History to TXT")

numbers = []

while True:
    print("\n1. Add Number")
    print("2. Show History")
    print("3. Save History to TXT")
    print("4. Read History from TXT")
    print("5. Clear History")
    print("6. Exit")

    choice = input("Choose (1-6): ")

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
            with open("numbers_history.txt", "w") as file:
                for number in numbers:
                    file.write(str(number) + "\n")

            print("Numbers history saved to numbers_history.txt ✅")
        else:
            print("No numbers yet ❌")

    elif choice == "4":
        try:
            with open("numbers_history.txt", "r") as file:
                content = file.read()
                print("\n📄 Saved Numbers History")
                print(content)
        except FileNotFoundError:
            print("No saved history found ❌")

    elif choice == "5":
        numbers.clear()
        print("History cleared 🧹")

    elif choice == "6":
        print("Goodbye Phillip! 👋")
        break

    else:
        print("Invalid choice ❌")