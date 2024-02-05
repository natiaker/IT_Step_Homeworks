lst = ['hello', 'world', 'coding', 'nod', "bald", "calming"]
end1 = 'ing'
end2 = 'ld'
end3 = 5


def new_lst(str_list, ending):
    try:
        return list(filter(lambda el: ending in el[(-len(ending)):], str_list))
    except TypeError:
        return "Invalid type"


print(new_lst(lst, end1))
print(new_lst(lst, end2))
print(new_lst(lst, end3))
