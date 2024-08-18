import math
def scientific_calculator():
    while True:
        print("\nScientific Calculator:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square Root")
        print("6. Exponential (Power)")
        print("7. Logarithm")
        print("8. Sine")
        print("9. Cosine")
        print("10. Tangent")
        print("11. Back to Main Menu")

        choice = input("Choose an operation: ")

        if choice == '11':
            break

        if choice in ['1', '2', '3', '4']:
            num_count = int(input("How many numbers do you want to use in your equation?: "))
            numbers = [float(input(f"Enter number {i+1}: ")) for i in range(num_count)]

        if choice == '1':
            result = sum(numbers)
        elif choice == '2':
            result = numbers[0]
            for num in numbers[1:]:
                result -= num
        elif choice == '3':
            result = 1
            for num in numbers:
                result *= num
        elif choice == '4':
            result = numbers[0]
            for num in numbers[1:]:
                result /= num
        elif choice == '5':
            num = float(input("Enter number: "))
            result = math.sqrt(num)
        elif choice == '6':
            num1 = float(input("Enter base: "))
            num2 = float(input("Enter exponent: "))
            result = math.pow(num1, num2)
        elif choice == '7':
            num1 = float(input("Enter number: "))
            num2 = float(input("Enter base: "))
            result = math.log(num1, num2)
        elif choice == '8':
            num = float(input("Enter number (in radians): "))
            result = math.sin(num)
        elif choice == '9':
            num = float(input("Enter number (in radians): "))
            result = math.cos(num)
        elif choice == '10':
            num = float(input("Enter number (in radians): "))
            result = math.tan(num)
        else:
            print("Invalid choice. Please try again.")
            continue

        print(f"Result: {result}")