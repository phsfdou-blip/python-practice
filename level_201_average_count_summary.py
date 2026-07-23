print("🤖 Level 201 VS Code + AI Copilot Average Count Summary")

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

if len(practice_minutes) > 0:
    total_minutes = sum(practice_minutes)
    average_minutes = total_minutes / len(practice_minutes)

    above_average_count = 0
    below_average_count = 0
    equal_average_count = 0

    for minutes in practice_minutes:
        if minutes > average_minutes:
            above_average_count += 1
        elif minutes < average_minutes:
            below_average_count += 1
        else:
            equal_average_count += 1

    print()
    print("Practice minutes:", practice_minutes)
    print("Average practice minutes:", average_minutes)
    print("Above average:", above_average_count)
    print("Below average:", below_average_count)
    print("Equal to average:", equal_average_count)
else:
    print("No valid practice times were entered.")

print("Practice program finished.")