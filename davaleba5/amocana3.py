my_list = [43, '22', 12, 66, 210, ["hi"]]

print(my_list.index(210))  # a

my_list[-1].append("hello")  # b
print(my_list)

my_list.pop(2)  # c
print(my_list)

my_list_2 = my_list  # d
my_list_2.clear()
print(f"my list: {my_list}, my list 2: {my_list_2}")

