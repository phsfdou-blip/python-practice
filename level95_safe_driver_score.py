
print("🚀 Level 95 Safe Driver Score Practice")

name = input("Enter your name: ")

try:
    miles = float(input("How many miles did you drive today? "))
    stops = int(input("How many stops did you make today? "))

    if miles <= 0:
        print("Miles must be more than 0 ❌")
    elif stops < 0:
        print("Stops cannot be negative ❌")
    else:
        score = miles / (stops + 1)

        print(f"\nGreat job {name}!")
        print("Miles =", miles)
        print("Stops =", stops)
        print("Driver score =", round(score, 2))

        if score >= 10:
            print("Result: Long distance driving day 🚍")
        elif score >= 5:
            print("Result: Normal driving day ✅")
        else:
            print("Result: Many stops today 🛑")

except:
    print("Invalid input ❌ Please enter numbers only.")