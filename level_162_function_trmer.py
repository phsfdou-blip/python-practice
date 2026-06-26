print("🤖 Level 162 VS Code 10-Minute Function Practice")

name = input("Enter your name: ")
device = input("Are you using Surface or iMac? ")
minutes = int(input("How many minutes are you practicing today? "))

def show_summary(name, device, minutes):
    print()
    print("Hello", name)
    print("Today you practiced VS Code Python.")
    print("Device:", device)
    print("Practice time:", minutes, "minutes")

def show_next_step():
    print()
    print("Next step:")
    print("✅ Save file")
    print("✅ Run Python program")
    print("✅ Check Source Control")
    print("✅ Commit and Sync")
    print("✅ Check GitHub Web")

show_summary(name, device, minutes)
show_next_step()

if minutes >= 10:
    print()
    print("Excellent! 10 minutes VS Code practice complete ✅")
else:
    print()
    print("Good start! Keep going step by step.")