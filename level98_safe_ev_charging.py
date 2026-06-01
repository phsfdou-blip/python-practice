
print("🚀 Level 98 Safe EV Charging Cost Calculator")

name = input("Enter your name: ")

try:
    kwh_used = float(input("How many kWh did you charge? "))
    price_per_kwh = float(input("Price per kWh? "))

    if kwh_used <= 0:
        print("kWh must be more than 0 ❌")
    elif price_per_kwh <= 0:
        print("Price per kWh must be more than 0 ❌")
    else:
        total_cost = kwh_used * price_per_kwh

        print(f"\nGreat job {name}!")
        print("kWh used =", kwh_used)
        print("Price per kWh = $", price_per_kwh)
        print("Total charging cost = $", round(total_cost, 2))

        if total_cost >= 30:
            print("Result: Expensive charging session 💰")
        elif total_cost >= 10:
            print("Result: Normal charging cost ✅")
        else:
            print("Result: Low charging cost 👍")

except:
    print("Invalid input ❌ Please enter numbers only.")
