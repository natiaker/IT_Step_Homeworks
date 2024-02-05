def lst_sum(*args):
    list_sum = 0
    for arg in args:
        list_sum += arg
    print(list_sum)


lst = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
lst_sum(*lst)
