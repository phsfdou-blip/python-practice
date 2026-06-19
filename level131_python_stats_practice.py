print("🚀 Level 131 Python Stats Practice")

name = input("Enter your name: ")

monday = int(input("Monday minutes: "))
tuesday = int(input("Tuesday minutes: "))
wednesday = int(input("Wednesday minutes: "))
thursday = int(input("Thursday minutes: "))
friday = int(input("Friday minutes: "))

minutes = [monday, tuesday, wednesday, thursday, friday]

total = sum(minutes)
average = total / len(minutes)
smallest = min(minutes)
biggest = max(minutes)

print()
print("Hello", name)
print("Your practice minutes:", minutes)
print("Total minutes:", total)
print("Average minutes:", average)
print("Min minutes:", smallest)
print("Max minutes:", biggest)

if total >= 100:
    print("Excellent work Phillip! Strong practice week ✅")
else:
    print("Good start. Keep practicing step by step 👍")

print("Level 131 complete! 🚀")