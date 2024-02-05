import random

random_list = [random.randint(0, 50) for i in range(10)]
print(random_list)

multiples_of_three = lambda x: x % 3 == 0
res = []


def linear_search(lst, l_func):
    for i in range(len(lst)):
        if l_func(lst[i]):
            res.append(i)


linear_search(random_list, multiples_of_three)
print("indexes of multiples of three:", res)
