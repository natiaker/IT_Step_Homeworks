a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

b = [
    [5, 2, 5, 9],
    [5, 8, 10, 11],
    [4, 2, 1, 10],
    [7, 3, 14, 13]
]

result = [[a[i][j] + b[i][j] for j in range(len(a[i]))] for i in range(len(a))]

for r in result:
    print(r)
