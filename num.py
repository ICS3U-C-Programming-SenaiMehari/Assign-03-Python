# This is a program that compares two numbers and tells the user which is larger, smaller, or if they are equal.
#Accept two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the numbers
if num1 > num2:
    print(f"{num1} is larger and {num2} is smaller.")
elif num2 > num1:
    print(f"{num2} is larger and {num1} is smaller.")
else:
    print(f"Both numbers are equal.")