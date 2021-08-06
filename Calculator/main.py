from art import logo

print("logo")


def add(n1, n2):
    """Adds two numbers"""
    return n1 + n2


def subtract(n1, n2):
    """Subtracts the second number from the first"""
    return n1 - n2


def multiply(n1, n2):
    """Multiplies two numbers"""
    return n1 * n2


def divide(n1, n2):
    """Divides the first number by the second number"""
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def next_operation(previous_answer):
    """Requests the next operation to be executed and returns the result"""
    operation_symbol = input("Pick an operation: ")
    next_number = float(input("What's the next number?: "))
    new_answer = operations[operation_symbol](previous_answer, next_number)
    print(f"{previous_answer} {operation_symbol} {next_number} = {new_answer}")
    return new_answer


def calculator():
    response = "y"
    number1 = float(input("What's the first number?: "))
    for operation in operations:
        print(operation)
    answer = number1

    while response == 'y':
        next_answer = next_operation(answer)
        answer = next_answer
        response = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")

    calculator()


calculator()
