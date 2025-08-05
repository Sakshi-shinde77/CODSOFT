def main():
    
    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b
    
    def multiply(a, b):
        return a * b
    
    def divide(a, b):
        if b == 0:
            return "Error! Division by zero."
        return a / b

    while True:
        print("\nSimple Calculator Menu:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '5':
            print("Exiting the calculator.")
            break
        
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == '1':
                print(f"The result is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"The result is: {result}")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
    