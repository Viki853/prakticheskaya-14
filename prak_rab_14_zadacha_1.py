import random
list= [[random.randint(1, 100) for _ in range(3)] for _ in range(4)]

print("Исходный список:")
for row in list:
    print(row)

max_value = list[0][0]
max_row = 0
max_col = 0

n = 0
while n < len(list):
    k = 0
    while k < len(list[n]):

        if list[n][k] > max_value:
            max_value = list[n][k]
            max_row = n
            max_col = k
        k += 1
    n += 1

print(f"\nМаксимальный элемент: {max_value}")
print(f"Позиция: строка {max_row}, столбец {max_col}")

