def digit_sum(number):
    if number == 0:
        return 0
    else:
        return number % 10 + digit_sum(number // 10)


print(digit_sum(12345))
