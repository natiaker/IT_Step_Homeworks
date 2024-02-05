num1 = float(input("input first number: "))
num2 = float(input("input second number: "))
operator = input("input operator: ")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "%":
    print(num1 % num2)
elif operator == "**":
    print(num1 ** num2)
elif operator == "//":
    print(num1 // num2)
else:
    print("please input valid operator")
