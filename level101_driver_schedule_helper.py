
print("🚀 Level 101 Driver Schedule Helper")

name = input("Enter your name: ")

while True:
    print("\n===== Driver Schedule Helper =====")
    print("1. Check Morning Shift")
    print("2. Check Afternoon Shift")
    print("3. Check Total Work Hours")
    print("4. Exit")

    choice = input("Choose (1-4): ")

    if choice == "1":
        route = input("Enter morning route name: ")
        start_time = input("Enter morning start time: ")
        end_time = input("Enter morning end time: ")

        print("\nMorning Shift ✅")
        print("Route:", route)
        print("Start:", start_time)
        print("End:", end_time)

    elif choice == "2":
        route = input("Enter afternoon route name: ")
        start_time = input("Enter afternoon start time: ")
        end_time = input("Enter afternoon end time: ")

        print("\nAfternoon Shift ✅")
        print("Route:", route)
        print("Start:", start_time)
        print("End:", end_time)

    elif choice == "3":
        try:
            morning_hours = float(input("Enter morning shift hours: "))
            afternoon_hours = float(input("Enter afternoon shift hours: "))

            if morning_hours < 0 or afternoon_hours < 0:
                print("Hours cannot be negative ❌")
            else:
                total_hours = morning_hours + afternoon_hours
                print("Total work hours =", round(total_hours, 2))

                if total_hours >= 10:
                    print("Result: Long work day 🚍")
                elif total_hours >= 8:
                    print("Result: Full work day ✅")
                else:
                    print("Result: Short work day 👍")

        except:
            print("Invalid input ❌ Please enter numbers only.")

    elif choice == "4":
        print(f"Goodbye {name}! Great Level 101 work 🎉")
        break

    else:
        print("Invalid choice ❌ Please choose 1-4.")