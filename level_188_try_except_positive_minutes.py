
print("🤖 Level 188 VS Code + AI Copilot Positive Minutes Practice")

name = input("Enter your name: ")
device = input("Are you using Surface or iMac? ")

def get_minutes():
    while True:
        try:
            minutes = int(input("How many minutes are you practicing today? "))

            if minutes > 0:
                return minutes
            else:
                print("Please enter a number greater than 0.")

        except ValueError:
            print("Please enter a whole number.")

minutes = get_minutes()

print()
print("Hello", name)
print("Device:", device)
print("Today's practice:", minutes, "minutes")

if minutes >= 20:
    print("Excellent! You reached your goal.")
else:
    print("Keep practicing every day!")
