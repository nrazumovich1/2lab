import random
n = 4
matrix = [[random.randint(-10,10) for j in range(n)] for i in range(n)]

for row in matrix:
    print(row)      # Вывод матрицы

sum = 0
for j in range(n):
    has_negative = False
    for i in range(n):
        if matrix[i][j] < 0:
            has_negative = True
            break
    if not has_negative:
        for i in range(n):
            sum += matrix[i][j]

print("Сумма элементов в столбцах без отрицательных элементов:", sum)