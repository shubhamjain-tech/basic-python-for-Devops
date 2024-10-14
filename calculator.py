# Simple Calculator Program

# Get user input for two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Display data types
print("Type of num1:", type(num1))
print("Type of num2:", type(num2))

# Menu for selecting operation
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Get user choice
choice = input("Enter choice (1/2/3/4): ")

# Perform operation based on user choice
if choice == '1':
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}")
elif choice == '2':
    result = num1 - num2
    print(f"The difference between {num1} and {num2} is: {result}")
elif choice == '3':
    result = num1 * num2
    print(f"The product of {num1} and {num2} is: {result}")
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"The quotient when {num1} is divided by {num2} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid input! Please select a valid operation.")
