x = int(input('Input number1: '))
y = int(input('Input number2: '))
operator = str(input("Input Operator: "))

calculator_dict = {
    "+": x + y,
    "-": x - y,
    "*": x * y,
    "/": x / y,
    "//": x // y,
    "%": x % y,
}


def calculator(dictionary, op):
    for key in dictionary:
        if op == key:
            return calculator_dict[key]


print(calculator(calculator_dict, operator))
