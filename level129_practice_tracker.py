
print("🚀 Level 129 Python + GitHub + Office Practice Tracker")

name = input("Enter your name: ")

python_minutes = int(input("Python + GitHub minutes: "))
github_web_minutes = int(input("GitHub Web minutes: "))
excel_minutes = int(input("Excel minutes: "))
word_minutes = int(input("Word minutes: "))

total_minutes = python_minutes + github_web_minutes + excel_minutes + word_minutes

print()
print("Hello", name)
print("Today's learning agenda:")
print("Python + GitHub:", python_minutes, "minutes")
print("GitHub Web:", github_web_minutes, "minutes")
print("Excel:", excel_minutes, "minutes")
print("Word:", word_minutes, "minutes")
print("Total learning time:", total_minutes, "minutes")

if total_minutes >= 60:
    print("Great job Phillip! 1 hour completed ✅")
else:
    print("Keep going step by step 👍")