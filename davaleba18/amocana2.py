class Functor:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        if args[0] > 0:
            return self.func(args[0])
        else:
            raise ValueError('Argument is not positive')


def return_arg(num):
    return num


input_num = int(input('Enter a number: '))

check_num = Functor(return_arg)
result = check_num(input_num)
print(result)
