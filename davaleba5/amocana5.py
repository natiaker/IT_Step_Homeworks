matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = [[matrix[j][i] for j in range(len(matrix[i]))] for i in range(len(matrix))]

for r in result:
    print(r)