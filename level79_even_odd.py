print("🚀 Level 79 Even or Odd Function")

def check_even_odd(number):
    if number % 2 == 0:
        return "Even ✅"
    else:
        return "Odd ✅"

name = input("Enter your name: ")
number = int(input("Enter a number: "))

result = check_even_odd(number)

print()
print("Hello", name)
print("Result:", result)
print("VS Code + AI Copilot + GitHub 🚀")