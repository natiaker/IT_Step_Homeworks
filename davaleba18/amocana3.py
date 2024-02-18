def commission(func):
    def wrapper(*args, **kwargs):
        balance = func(*args, **kwargs)
        if balance >= 1:
            return balance - 1
        else:
            return "Not enough money"
    return wrapper


@commission
def transaction(balance, payment):
    amount_left = balance - payment
    return amount_left


print(transaction(100, 80))
print(transaction(100, 100))
