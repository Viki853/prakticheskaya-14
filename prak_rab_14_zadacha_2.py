import random
list = [[random.randint(1, 100) for _ in range(3)] for _ in range(4)]

total = 0
row_sum=0
col_sum=0
max_sum=0
for i in range(3):
    n=0
    for j in range(4):
        n+=list[j][i]
        total+=list[j][i]
    print(f'Cумма строки {i} равна {j} ')

    if n>max_sum:
        max_sum=n
        max_row=i

print(f'Общая сумма:{total}')
print(f'Строка с минимальной суммой:{max_row}')



