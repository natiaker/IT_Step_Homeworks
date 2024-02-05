import random

random_lst = [random.randint(1, 50) for i in range(100)]
print(random_lst)


def merge_sort(lst):
    if len(lst) > 1:
        left = lst[:len(lst)//2]
        right = lst[len(lst)//2:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1


def selection_sort(lst):
    for i in range(len(lst)):
        min_i = i

        for j in range(i+1, len(lst)):
            if lst[min_i] < lst[j]:
                min_i = j

        lst[i], lst[min_i] = lst[min_i], lst[i]


merge_sort(random_lst)
print("ascending:", random_lst)

selection_sort(random_lst)
print("descending:", random_lst)
