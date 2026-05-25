
print("🚀 Level 86 Save Smart Stats Report")

numbers = []

while True:
    print("\n1. Add Number")
    print("2. Show History")
    print("3. Smart Stats Report")
    print("4. Save Report to TXT")
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
        if len(numbers) > 0:
            total = sum(numbers)
            count = len(numbers)
            average = total / count
            highest = max(numbers)
            lowest = min(numbers)

            with open("stats_report.txt", "w") as file:
                file.write("📊 Smart Stats Report\n")
                file.write("----------------------\n")
                file.write(f"Count = {count}\n")
                file.write(f"Total = {total}\n")
                file.write(f"Average = {round(average, 2)}\n")
                file.write(f"Max = {highest}\n")
                file.write(f"Min = {lowest}\n")

            print("Report saved to stats_report.txt ✅")
        else:
            print("No numbers yet ❌")

    elif choice == "5":
        numbers.clear()
        print("History cleared 🧹")

    elif choice == "6":
        print("Goodbye Phillip! 👋")
        break

    else:
        print("Invalid choice ❌")