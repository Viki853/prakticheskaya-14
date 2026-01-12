import random
matrix = [[random.randint(1, 100) for _ in range(3)] for _ in range(4)]

print("Исходная матрица:")
for row in matrix:
    print(row)

max_value = matrix[0][0]
max_row = 0
max_col = 0

n = 0
while n < len(matrix):
    k = 0
    while k < len(matrix[n]):

        if matrix[n][k] > max_value:
            max_value = matrix[n][k]
            max_row = n
            max_col = k
        k += 1
    n += 1

print(f"\nМаксимальный элемент: {max_value}")
print(f"Позиция: строка {max_row}, столбец {max_col}")
