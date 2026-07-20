print("🤖 Level 197 VS Code + AI Copilot Average Minutes Practice")

total_minutes = 0
valid_entries = 0
attempts = 0

while attempts < 5:
    try:
        minutes = int(input("Enter practice minutes: "))
        attempts += 1

        if minutes <= 0:
            print("Please enter a number greater than 0.")
            continue

        total_minutes += minutes
        valid_entries += 1
        print("Practice time accepted.")

    except ValueError:
        attempts += 1
        print("Please enter a whole number.")

print()
print("Total accepted minutes:", total_minutes)
print("Valid entries:", valid_entries)

if valid_entries > 0:
    average_minutes = total_minutes / valid_entries
    print("Average practice minutes:", average_minutes)
else:
    print("No valid practice times were entered.")

print("Practice program finished.")