input_string = str(input("შეიყვანეთ სტრიქონი: "))
input_symbol = str(input("შეიყვანეთ სიმბოლო რომლის რაოდენობაც გაინტერესებთ სტრიქონში: "))


def check_symbol(string, symbol):
    string = string.lower()
    return string.count(symbol)


print(check_symbol(input_string, input_symbol))
