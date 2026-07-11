print("🤖 Level 187 Try/Except Loop Practice")

name = input("Enter your name: ")
device = input("Are you using Surface or iMac? ")

def get_minutes():
    while True:
        try:
            minutes = int(input("How many minutes are you practicing today? "))
            return minutes
        except ValueError:
            print("Please enter a whole number.")

minutes = get_minutes()

print()
print("Hello", name)
print("Device:", device)
print("Practice time:", minutes, "minutes")

if minutes >= 20:
    print("Excellent! You reached your 20-minute goal.")
else:
    print("Good start. Keep practicing step by step.")