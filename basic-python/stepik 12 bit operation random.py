# a = 0b11010001
# # выключите 4-й и 1-й биты
# print(153 & 0b11101101)
# print(153 & ~0b10010)
# # переключите 3-й и 0-й биты
# print(22 ^ 0b1001)
# s = 'ѩкю[щюлцхZ'
# [print(chr(ord(i) ^ 123), end='') for i in s]
# print()
# # включен ли 5-й или 1-й
# n = 74
# print('ДА' if n & 0b10 or n & 0b100000 else 'НЕТ')

import random

# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

# здесь продолжайте программу
a, b = -4, 5

print(round(random.uniform(a, b), 2))
print(random.randint(a, b))
print(random.shuffle([1, 2, 3]))

# начальная инициализация поля (переменные P и N не менять, единицы записывать в список P)
N = 10
P = [[0] * N for i in range(N)]

# здесь продолжайте программу
M = 10
while M:
    i = random.randint(0, N - 1)
    j = random.randint(0, N - 1)
    if P[i][j] == 1:
        continue
    if not sum(P[row][column] for row in range(max(0, i - 1), min(i + 2, N))
               for column in range(max(0, j - 1), min(j + 2, N))):
        P[i][j] = 1
        M -= 1
for el in P:
    print(el)
