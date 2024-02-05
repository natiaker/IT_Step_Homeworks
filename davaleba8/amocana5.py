import functools

lst = [1, 2, 3, 4, 5]


def multiply(num_lst):
    try:
        return functools.reduce(lambda x, y: x * y, num_lst)
    except TypeError:
        return "Invalid type"


print(multiply(lst))
