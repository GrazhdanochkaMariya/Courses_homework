n, m = int(input()), int(input())
matrix = []

for i in range(n):
    matrix.append(input().split())

maximum = -10 ** 10
maximum_index = []
for j in range(n):
    for k in range(m):
        if int(matrix[j][k]) > maximum:
            maximum = int(matrix[j][k])
            maximum_index.clear()
            maximum_index.append(str(j))
            maximum_index.append(str(k))

print(' '.join(maximum_index))
