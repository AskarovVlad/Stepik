# n = int(input())
# lst = []
# while n < 100:
#     for num in range(1, n + 1):
#         if num % 3 == 0 and num % 5 == 0:
#             lst.append(num)
#     print(*lst)
#     break
# else:
#     print("слишком большое значение n")
# n = int(input())
# i = 1
# while i ** 2 <= n:
#     i += 1
# else:
#     print(i)
# x = int(input())
# l = 10
# day = 1
# cof = 1.1
# while l <= x:
#     day += 1
#     l *= cof
# else:
#     print(day)
# import sys
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in = ['Муму', 'Евгений Онегин', 'Сияние', 'Мастер и Маргарита', 'Пиковая дама', 'Колобок']
# i = 0
# while i < len(lst_in):
#     if " " in lst_in[i]:
#         lst_in.pop(i)
#     else:
#         i += 1
# print(*lst_in)
# print(*range(1,20,3))
# lst = list(map(int, input().split()))
# sum = 0
# for el in lst:
#     if el % 2 != 0:
#         sum += el
# print(sum)
# n = map(int, input().split())
# print(n)
# print(sum([i for i in n if i % 2 != 0]))
# cities = input().split()
# cities = ['Москва', 'Уфа', 'Караганда', 'Тверь', 'Минск', 'Казань']
# for index, element in enumerate(cities):
#     cities[index] = len(element)
# print(*cities)
# print(*map(len, input().split()))
# x = int(input())
# for el in range(1, x+1):
#     if x % el == 0:
#         print(el)
# n = int(input())
# [print(i) for i in range(1, n + 1) if n % i == 0]
# n = int(input())
# for el in range(2, n):
#     if n % el == 0:
#         print("НЕТ")
#         break
# else:
#     print('ДА')
# cities = input().upper().split()
# cities = ['МОСКВА', 'АСТРАХАНЬ', 'НОВГОРОД', 'ДИМИТРОВГРАД', 'ДУШАНБЕ']
# flag = False
# for i in range(len(cities) - 1):
#     lstsumbol = cities[i].lower()[-1]
#     if lstsumbol in ['ь', 'ъ', 'ы']:
#         if cities[i].lower()[-2] != cities[i + 1].lower()[0]:
#             flag = True
#             break
#     elif lstsumbol != cities[i + 1].lower()[0]:
#         flag = True
#         break
#     else:
#         flag = False
# print("НЕТ" if flag else "ДА")
# string = 'Барабанщик бил бой в барабан'
# string = input()
# print(string)
# if 'ра' in string:
#     print(*[i for i in range(len(string)) if string.startswith('ра', i)])
# else:
#     print(-1)
# num = input()
# flag = False
# phone_num = num[1] + num[3:6] + num[7:10] + num[11:13] + num[14:]
# if num[0] == '+' and num[1] == '7' and num[2] == '(' and num[6] == ')' and num[10] == '-' and num[13] == '-':
#     flag = True
# if flag and phone_num.isdigit() and len(num) == 16:
#     print('ДА')
# else:
#     print("НЕТ")
# a = 5
# s = '120+25   - 12'
# print(eval('2 + a'))
# print(exec('2 + a'))
# lst = [* map(int, input().split())]
# for i, v in enumerate(lst):
#     lst[i] = v ** 2
# print(*lst)
# lst = [* map(int, input().split())]
# lst2 = []
# for i, v in enumerate(lst):
#     lst2.extend([v, v])
# print(lst2)
# lst = [* map(float, input().split())]
# lst = [2, 3, 4, 1, 2, 3]
# num = lst[0]
# for i in lst:
#     if num > i:
#         num = i
#     else:
#         continue
# print(num)
# a = iter([1, True, "abc", -5.6])
# # b = iter(7) не правильно
# c = iter([])
# # d = iter(True) не правильно
# f = iter("")
# g = iter("python")
# lst = [* input().split()]
# a = iter(lst)
# print(next(a), next(a))
# s = input()
# a = iter(s)
# for el in s:
#     if el == " ":
#         break
#     else:
#         print(next(a), end=" ")
# num = int(input())
# num = str(num)
# a = iter(num)
# for el in num:
#     print(next(a), end=" ")
# lst = input().split()
# print(lst)
# lst2 = []
# for i in range(0, len(lst), 2):
#     if lst[i+1].isdigit():
#         lst[i+1]=int(lst[i+1])

#     lst2.append([lst[i], lst[i+1]])
# print(lst2)
# lst = input().split()
# print([[lst[i], int(lst[i+1])] for i in range(0, len(lst), 2)])
# lst_in = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# lst3 = []
# for el in lst_in:
#     lst3.extend(el)
# lst3.reverse()
# print(*lst3)
# print(*[j for i in lst_in[::-1] for j in i[::-1]])
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# n = int(len(lst) ** 0.5)
# lst2 = [[lst[i] for i in range(j, j+n)] for j in range(0, len(lst), n)]
# print(lst2)
t = ["– Скажи-ка, дядя, ведь не даром",
     "Я Python выучил с каналом",
     "Балакирев что раздавал?",
     "Ведь были ж заданья боевые,",
     "Да, говорят, еще какие!",
     "Недаром помнит вся Россия",
     "Как мы рубили их тогда!"
     ]
# Необходимо преобразовать его в двумерный (вложенный) список lst, где каждая строка представляется списком из слов
# (слова разделяются пробелом), но сохранять слова только длиной более трех символов. Решить данную задачу с использованием
# # list comprehension. Результат отобразить с помощью команды:
# t2 = []
# for el in t:
#     t2.append(el.split())
# print(t2)
# for row in t2:
#     for el in row:
#         if len(el) < 3:
#             row.remove(el)
# print(t2)
# print([[el for el in row.split() if len(el) > 3] for row in t])
# list_in = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
# A = [[i[j] for i in list_in] for j in range(len(list_in[0]))]
# for row in A:
#     print(*row)
print(t)