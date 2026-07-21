print("🤖 Level 199 VS Code + AI Copilot Above-Average Minutes Practice")

practice_minutes = []
attempts = 0

while attempts < 5:
    try:
        minutes = int(input("Enter practice minutes: "))

        if minutes <= 0:
            print("Please enter a number greater than 0.")
        else:
            practice_minutes.append(minutes)
            print("Practice time accepted.")

    except ValueError:
        print("Please enter a whole number.")

    attempts += 1

print()

if len(practice_minutes) > 0:
    total_minutes = sum(practice_minutes)
    average_minutes = total_minutes / len(practice_minutes)

    above_average_count = 0

    for minutes in practice_minutes:
        if minutes > average_minutes:
            above_average_count += 1

    print("Practice minutes:", practice_minutes)
    print("Total minutes:", total_minutes)
    print("Average minutes:", average_minutes)
    print("Highest minutes:", max(practice_minutes))
    print("Lowest minutes:", min(practice_minutes))
    print("Entries above average:", above_average_count)
else:
    print("No valid practice minutes were entered.")

print("Practice program finished.")