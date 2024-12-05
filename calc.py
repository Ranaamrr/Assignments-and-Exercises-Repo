def calc(command, num1, num2):
    if command == "add":
        return num1 + num2
    elif command == "sub":
        return num1 - num2
    elif command == "mult":
        return num1 * num2
    elif command == "div":
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid command"
import