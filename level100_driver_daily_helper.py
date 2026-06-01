
print("🚀 Level 100 Driver Daily Helper Mini Project")

name = input("Enter your name: ")

while True:
    print("\n===== Driver Daily Helper Menu =====")
    print("1. Calculate Driver Score")
    print("2. Calculate Fuel Cost")
    print("3. Calculate EV Charging Cost")
    print("4. Exit")

    choice = input("Choose (1-4): ")

    if choice == "1":
        try:
            miles = float(input("How many miles did you drive today? "))
            stops = int(input("How many stops did you make today? "))

            if miles <= 0:
                print("Miles must be more than 0 ❌")
            elif stops < 0:
                print("Stops cannot be negative ❌")
            else:
                score = miles / (stops + 1)
                print("Driver score =", round(score, 2))

                if score >= 10:
                    print("Result: Long distance driving day 🚍")
                elif score >= 5:
                    print("Result: Normal driving day ✅")
                else:
                    print("Result: Many stops today 🛑")

        except:
            print("Invalid input ❌ Please enter numbers only.")

    elif choice == "2":
        try:
            miles = float(input("How many miles did you drive? "))
            mpg = float(input("How many miles per gallon? "))
            gas_price = float(input("Gas price per gallon? "))

            if miles <= 0:
                print("Miles must be more than 0 ❌")
            elif mpg <= 0:
                print("MPG must be more than 0 ❌")
            elif gas_price <= 0:
                print("Gas price must be more than 0 ❌")
            else:
                gallons_used = miles / mpg
                total_cost = gallons_used * gas_price

                print("Gallons used =", round(gallons_used, 2))
                print("Total fuel cost = $", round(total_cost, 2))

        except:
            print("Invalid input ❌ Please enter numbers only.")

    elif choice == "3":
        try:
            kwh_used = float(input("How many kWh did you charge? "))
            price_per_kwh = float(input("Price per kWh? "))

            if kwh_used <= 0:
                print("kWh must be more than 0 ❌")
            elif price_per_kwh <= 0:
                print("Price per kWh must be more than 0 ❌")
            else:
                total_cost = kwh_used * price_per_kwh
                print("Total charging cost = $", round(total_cost, 2))

        except:
            print("Invalid input ❌ Please enter numbers only.")

    elif choice == "4":
        print(f"Goodbye {name}! Great job reaching Level 100 🎉")
        break

    else:
        print("Invalid choice ❌ Please choose 1-4.")