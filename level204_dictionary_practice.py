print("🤖 Level 204 - Dictionary Practice")

practice = {
    "Monday": 20,
    "Tuesday": 30,
    "Wednesday": 40,
    "Thursday": 25,
    "Friday": 35
}

total = 0

for day, minutes in practice.items():
    print(day, ":", minutes, "minutes")
    total += minutes

average = total / len(practice)

print()
print("Total minutes:", total)
print("Average minutes:", average)