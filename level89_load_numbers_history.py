
print("🚀 Level 89 Load Numbers History Back into List")

numbers = []

while True:
    print("\n1. Add Number")
    print("2. Show History")
    print("3. Save History to TXT")
    print("4. Load History from TXT")
    print("5. Clear History")
    print("6. Exit")

    choice = input("Choose (1-6): ")

    if choice == "1":
        try:
            number = float(input("Enter a number: "))
            numbers.append(number)
            
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
            numbers.clear()

            with open("numbers_history.txt", "r") as file:
                for line in file:
                    number = float(line.strip())
                    numbers.append(number)

            print("Numbers history loaded back into Python list ✅")
            print("History:", numbers)

        except FileNotFoundError:
            print("No saved history found ❌")
        except:
            print("Could not load history ❌")

    elif choice == "5":
        numbers.clear()
        print("History cleared 🧹")

    elif choice == "6":
        print("Goodbye Phillip! 👋")
        break

    else:
        print("Invalid choice ❌")