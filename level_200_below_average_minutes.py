print("🤖 Level 200 VS Code + AI Copilot Below-Average Minutes Practice")

practice_minutes = []

for attempt in range(5):
    try:
        minutes = int(input("Enter practice minutes: "))

        if minutes <= 0:
            print("Please enter a number greater than 0.")
        else:
            practice_minutes.append(minutes)
            print("Practice time accepted.")

    except ValueError:
        print("Please enter a whole number.")

if len(practice_minutes) > 0:
    total_minutes = sum(practice_minutes)
    average_minutes = total_minutes / len(practice_minutes)

    below_average_count = 0

    for minutes in practice_minutes:
        if minutes < average_minutes:
            below_average_count += 1

    print()
    print("Practice minutes:", practice_minutes)
    print("Total minutes:", total_minutes)
    print("Average minutes:", average_minutes)
    print("Entries below average:", below_average_count)
else:
    print()
    print("No valid practice times were entered.")

print("Practice program finished.")