import random

random_list = [random.randint(0, 50) for i in range(100)]
print(random_list)


def linear_search(lst, x):
    for i in range(len(lst)):
        if lst[i] == x:
            return i

    return -1


print(f"(linear search) element 5 is on index {linear_search(random_list, 5)}")


def bubble_sort(lst):
    for i in range(len(lst)):
        swapped = False

        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break


def binary_search(lst, x):
    low = 0
    high = len(lst) - 1
    mid = 0

    while high >= low:
        mid = (high + low) // 2

        if lst[mid] < x:
            low = mid + 1
        elif lst[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1


bubble_sort(random_list)
print(f"sorted list: {random_list}")
result = binary_search(random_list, 1)
print(f"(binary search) element 1 is on index {result} ")
