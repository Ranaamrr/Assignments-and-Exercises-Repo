import calc
def run_calculator():
    while True:
        choice = input("Enter a choice (add, sub, mult, div): ")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = calc.calc(choice, num1, num2)
        print("Result:", result)
        again = input("Would you like to perform another operation? (yes to continue, stop to exit): ")

        if again == "stop":
            print("exiting the calculator")
            break
        elif again != "yes":
            print("Invalid input! Exiting the calculator.")
            break

run_calculator()