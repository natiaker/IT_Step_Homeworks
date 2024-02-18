def check_num(func):
    def wrapper(*args, **kwargs):
        if args[0] > 0:
            return func(args[0])
        else:
            raise ValueError('Argument is not positive')
    return wrapper


@check_num
def return_arg(num):
    return num


print(return_arg(6))
print(return_arg(-7))
