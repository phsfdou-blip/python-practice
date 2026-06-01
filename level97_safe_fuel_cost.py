
print("🚀 Level 97 Safe Fuel Cost Calculator")

name = input("Enter your name: ")

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

        print(f"\nGreat job {name}!")
        print("Miles =", miles)
        print("MPG =", mpg)
        print("Gas price =", gas_price)
        print("Gallons used =", round(gallons_used, 2))
        print("Total fuel cost = $", round(total_cost, 2))

        if total_cost >= 50:
            print("Result: Expensive driving day 💰")
        elif total_cost >= 20:
            print("Result: Normal fuel cost ✅")
        else:
            print("Result: Low fuel cost 👍")

except:
    print("Invalid input ❌ Please enter numbers only.")