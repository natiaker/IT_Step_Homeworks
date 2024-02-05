import random

my_list = []

for i in range(10):
    n = random.randint(0,20)
    my_list.append(n)

lowest = min(my_list)
highest = max(my_list)
print(my_list)
print(f"min = {lowest}")
print(f"max = {highest}")