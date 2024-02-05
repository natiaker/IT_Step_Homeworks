tuple1 = (1, 2, 3, 4, 5, 6)
tuple2 = (4, 5, 5, 6, 6, 7)


def func(tpl1, tpl2):
    set1 = set(tpl1)
    set2 = set(tpl2)

    tuple_union = tuple(set1.union(set2))
    print(f"გაერთიანება: {tuple_union}")

    duplicated_values = list(set1.intersection(set2))
    print(f"დუბლირებული ელემენტები: {duplicated_values}")


func(tuple1, tuple2)
