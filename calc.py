def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calc():
    num1 = float(input("What's the first number?: \n"))
    go_again = True

    while go_again:
        symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        # pull the functon from the dictionar and call it
        calc_function = operations[symbol]
        answer = calc_function(num1, num2)

        print(f"{num1} {symbol} {num2} = {answer}")

        if (
            input(
                f"Type 'y' to continue calculating with {answer}, or 'n' to start new: "
            )
            == "y"
        ):
            num1 = answer  # This is why we need the return and not print
        else:
            go_again = False
            calc()


calc()
