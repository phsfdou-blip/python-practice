
print("🚀 Level 93 Safe Age Checker")

while True:
    print("\n1. Enter Name and Age")
    print("2. Exit")

    choice = input("Choose (1-2): ")

    if choice == "1":
        name = input("Enter your name: ")

        try:
            age = int(input("Enter your age: "))

            if age < 0:
                print("Age cannot be negative ❌")
            elif age < 18:
                print(f"{name}, you are a minor.")
            elif age < 65:
                print(f"{name}, you are an adult.")
            else:
                print(f"{name}, you are a senior adult.")

        except:
            print("Invalid age ❌ Please enter a whole number.")

    elif choice == "2":
        print("Goodbye Phillip! 👋")
        break

    else:
        print("Invalid choice ❌")