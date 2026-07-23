print("🤖 Level 200 VS Code + AI Copilot Equal Average Practice")

practice_minutes = []

for attempt in range(5):
    try:
        minutes = int(input("Enter practice minutes: "))

        if minutes > 0:
            practice_minutes.append(minutes)
            print("Practice time accepted.")
        else:
            print("Please enter a number greater than 0.")

    except ValueError:
        print("Please enter a whole number.")

print()

if len(practice_minutes) > 0:
    total_minutes = sum(practice_minutes)
    average_minutes = total_minutes / len(practice_minutes)

    equal_average_count = 0

    for minutes in practice_minutes:
        if minutes == average_minutes:
            equal_average_count += 1

    print("Practice minutes:", practice_minutes)
    print("Total accepted minutes:", total_minutes)
    print("Average practice minutes:", average_minutes)
    print("Entries equal to the average:", equal_average_count)
else:
    print("No valid practice times were entered.")

print("Practice program finished.")