operator = input()
number1 = int(input())
number2 = int(input())

def operation_numbers (operator_: str, num1: int, num2: int):

    result = None

    if operator_ == "multiply":
        result = num1 * num2
    elif operator_ == "divide":
        result = num1 // num2
    elif operator_ == "add":
        result = num1 + num2
    elif operator_ == "subtract":
        result = num1 - num2

    return result

print(operation_numbers(operator, number1, number2))
