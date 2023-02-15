def calculator():
    print("Welcome to the calculator program")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    while True:
        choice = int(input("Enter your choice (1-5): "))
        if choice == 5:
            break
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == 1:
            result = num1 + num2
            print("The result is:", result)
        elif choice == 2:
            result = num1 - num2
            print("The result is:", result)
        elif choice == 3:
            result = num1 * num2
            print("The result is:", result)
        elif choice == 4:
            result = num1 / num2
            print("The result is:", result)
        else:
            print("Invalid choice! Try again.")

calculator()
