# a = [[1, 2, 3, 4], [5, 6, 7, 8]]
# b = [[1, 1, 1, 1], [2, 3, 4, 5]]
# c = []
# # суммирование матрицы
# for i, row in enumerate(a):
#     r = []
#     for j, x in enumerate(row):
#         r.append(x + b[i][j])
#
#     c.append(r)
# print(c)
# Транспонирование матрицы
# lst_in1 = [[2, 3, 4, 5, 6],
#            [3, 2, 7, 8, 9],
#            [4, 7, 2, 0, 4],
#            [5, 8, 0, 2, 1],
#            [6, 9, 4, 1, 2]]
# for i in range(len(lst_in1)):
#     for j in range(i + 1, len(lst_in1)):
#         lst_in1[i][j], lst_in1[j][i] = lst_in1[j][i], lst_in1[i][j]
# print(lst_in1)

# Проверка на симетричность относительно главной диагонали
# lst_in = [[2, 3, 4, 5, 6],
#           [3, 2, 7, 8, 9],
#           [4, 7, 2, 0, 4],
#           [5, 8, 0, 2, 1],
#           [6, 9, 4, 1, 2]]
# lst2 = []
# break_flag = False
# for el in lst_in:
#     lst2.append(el)
# for i in range(len(lst2)):
#     for j in range(i + 1, len(lst2)):
#         lst2[i][j], lst2[j][i] = lst2[j][i], lst2[i][j]
# for i in range(len(lst_in)):
#     for j in range(i+1, len(lst_in)):
#         if lst_in[i][j] != lst2[i][j]:
#             break_flag = True
#             break
#     if break_flag:
#         print("НЕТ")
#         break
#     else:
#         print("ДА")
#         break
#
# print(lst2)
# break_flag = False
# for i in range(len(lst_in)):
#     for j in range(i + 1, len(lst_in[i])):
#         if lst_in[i][j] != lst_in[j][i]:
#             break_flag = True
#             break
#         else:
#             continue
#     if break_flag:
#         print("НЕТ")
#         break
#     else:
#         print("ДА")
#         break
# lst = [*map(int, input().split())]
# print(lst)
# # Сортировка вставкой
# lst = [*map(int, input().split())]
# def selection_sort(lst):
#     for i in range(0, len(lst) - 1):
#         small = i
#         for j in range(i + 1, len(lst)):
#             if lst[j] < lst[small]:
#                 small = j
#         lst[i], lst[small] = lst[small], lst[i]
# selection_sort(lst)
# print(*lst)
# # Сортировка пузырьком
# lst = [*map(int, input().split())]
# def bubble_sort(lst):
#     flag = True
#     while flag:
#         flag = False
#         for i in range(len(lst) - 1):
#             if lst[i] > lst[i + 1]:
#                 lst[i], lst[i + 1] = lst[i + 1], lst[i]
#                 flag = True
# bubble_sort(lst)
# print(*lst)
# # В некоторой стране используются денежные купюры достоинством в 1, 2, 4, 8, 16, 32 и 64. Вводится натуральное число n.
# # Как наименьшим количеством таких денежных купюр можно выплатить сумму n? Вывести на экран список купюр для формирования
# # суммы n (в одну строчку через пробел, начиная с наибольшей и заканчивая наименьшей). Предполагается, что имеется
# # достаточно большое количество купюр всех достоинств.
# lst = [64, 32, 16, 8, 4, 2, 1]
# n = int(input())
# lst2 = []
# for i in lst:
#     m, n = divmod(n, i)
#     lst2.extend([i] * m)
# print(*lst2)
# x = int(input())
# for nominal in [64, 32, 16, 8, 4, 2, 1]:
#     for _ in range(x // nominal):
#         print(nominal, end=' ')
#     x %= nominal
# print([abs(el) for el in [*map(float, input().split())]])
#  Вводится натуральное число N. С помощью list comprehension сформировать двумерный список размером N x N,
#  состоящий из нулей, а по главной диагонали - единицы.
# n = int(input())
# lst = [[0] * n for el in range(n)]
# for i in range(len(lst)):
#     for j in range(i, i+1):
#         lst[i][j] = 1
#         print(*lst[i])
# print(*[el for el in input().split() if len(el) > 5])
# Вводится натуральное число n. Необходимо сформировать список с помощью list comprehension,
# состоящий из делителей числа n
# n = int(input())
# lst = []
# for el in range(1, n+1):
#     if n % el == 0:
#         lst.append(el)
# print(*lst)
# Вводится натуральное число N. Необходимо сгенерировать вложенный список с помощью list comprehension, размером N x N,
# где первая строка содержала бы все нули, вторая - все единицы, третья - все двойки и так до N-й строки.
# n = int(input())
# m = 0
# lst = []
# for i in range(n):
#     lst.append([m]*n)
#     m += 1
# for el in lst:
#     print(*el)
lst1 = [*map(int, input().split())]
lst2 = [*map(int, input().split())]
lst3 = []
for i in range(len(lst1)):
    lst3.append(lst1[i] + lst2[i])
print(*lst3)
