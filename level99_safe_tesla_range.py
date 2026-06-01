
print("🚀 Level 99 Safe Tesla Range Calculator")

name = input("Enter your name: ")

try:
    battery_percent = float(input("Battery percent now? "))
    miles_per_percent = float(input("How many miles per 1% battery? "))

    if battery_percent < 0 or battery_percent > 100:
        print("Battery percent must be between 0 and 100 ❌")
    elif miles_per_percent <= 0:
        print("Miles per percent must be more than 0 ❌")
    else:
        estimated_range = battery_percent * miles_per_percent

        print(f"\nGreat job {name}!")
        print("Battery percent =", battery_percent)
        print("Miles per 1% =", miles_per_percent)
        print("Estimated range =", round(estimated_range, 1), "miles")

        if estimated_range >= 200:
            print("Result: Strong range ✅")
        elif estimated_range >= 100:
            print("Result: Medium range 👍")
        else:
            print("Result: Charge soon ⚡")

except:
    print("Invalid input ❌ Please enter numbers only.")