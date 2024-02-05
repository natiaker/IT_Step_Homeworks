import random

lst = [random.randint(1, 50) for i in range(100)]
print(lst)

sorted_list_ascending = sorted(lst)
print(f"sorted() func - ascending: {sorted_list_ascending}")

sorted_list_descending = sorted(lst, reverse=True)
print(f"sorted() func - descending: {sorted_list_descending}")

lst.sort()
print(f"sort() method - ascending: {lst}")

lst.sort(reverse=True)
print(f"sort() method - descending: {lst}")
