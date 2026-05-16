#calcultor logic

# INITIAL INPUT BY USER
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# OPERATION SELECTOR
print("\nSelect operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# USER SELECTS AN OPTION FROM THE OPERATION SELECTOR
choice = input("Enter choice (1/2/3/4): ")

# PERFORM THE SELECTED OPERATION
if choice == "1":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

elif choice == "2":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

elif choice == "3":
    result = num1 * num2
    print(f"Result: {num1} x {num2} = {result}")

elif choice == "4":
    # HANDLE THE DIVISION BY ZERO
    if num2 == 0:
        print("Error: You can't divide by zero. Be For REAL!.")
    else:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")

else:
    print("You is a FAILURE.")