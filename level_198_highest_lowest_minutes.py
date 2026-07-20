print("🤖 Level 198 VS Code + AI Copilot Highest and Lowest Minutes Practice")

practice_minutes = []
attempts = 0

while attempts < 5:
    try:
        minutes = int(input("Enter practice minutes: "))

        if minutes <= 0:
            print("Please enter a number greater than 0.")
            attempts += 1
            continue

        practice_minutes.append(minutes)
        print("Practice time accepted.")

    except ValueError:
        print("Please enter a whole number.")

    attempts += 1

print()

if len(practice_minutes) > 0:
    total_minutes = sum(practice_minutes)
    average_minutes = total_minutes / len(practice_minutes)
    highest_minutes = max(practice_minutes)
    lowest_minutes = min(practice_minutes)

    print("Accepted practice times:", practice_minutes)
    print("Total accepted minutes:", total_minutes)
    print("Valid entries:", len(practice_minutes))
    print("Average practice minutes:", average_minutes)
    print("Highest practice minutes:", highest_minutes)
    print("Lowest practice minutes:", lowest_minutes)
else:
    print("No valid practice times were entered.")

print("Practice program finished.")