
print("🚀 Level 117 Daily Learning Summary")

name = input("Enter your name: ")

python_minutes = int(input("Python minutes: "))
excel_minutes = int(input("Excel minutes: "))
word_minutes = int(input("Word minutes: "))
ai_minutes = int(input("AI minutes: "))

total = python_minutes + excel_minutes + word_minutes + ai_minutes

print("Learning summary for", name)
print("Python:", python_minutes, "minutes")
print("Excel:", excel_minutes, "minutes")
print("Word:", word_minutes, "minutes")
print("AI:", ai_minutes, "minutes")
print("Total learning time:", total, "minutes")

if total >= 45:
    print("Great learning day ✅")
else:
    print("Good start, keep practicing ✅")