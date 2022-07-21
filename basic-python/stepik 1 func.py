# Вводится список целых чисел в одну строчку через пробел. Необходимо вычислить сумму этих введенных значений, используя
# рекурсивную функцию (для перебора элементов списка) с именем get_rec_sum. Функция должна возвращать значение суммы.
# (Выводить на экран она ничего не должна).
# Вызовите эту функцию и выведите вычисленное значение суммы на экран.
# N = [*map(int, input().split())]
#
#
# def get_rec_sum(N):
#     sum = 0
#     for el in N:
#         sum += el
#     return sum
# print(get_rec_sum(N))
# Вводится натуральное число N. Необходимо с помощью рекурсивной функции fib_rec(N, f=[])
# (здесь N - общее количество чисел Фибоначчи; f - начальный список этих чисел) сформировать последовательность чисел Фибоначчи по правилу:
# первые два числа равны 1 и 1, а каждое следующе значение равно сумме двух предыдущих.
# Пример такой последовательности для первых 7 чисел: 1, 1, 2, 3, 5, 8, 13, ...
# Функция должна возвращать список сформированной последовательности длиной N.
# Вызывать функцию не нужно, только объявить.
# N = int(input('Enter num: '))
#
#
# def fib_rec(N):
#     a, b = 1, 1
#     for i in range(N):
#         yield a
#         a, b = b, a + b
#
#
# gen = fib_rec(N)
# for i in range(N):
#     print(next(gen), end=' ')
# print()
#
# n = int(input())
# n = 7
#
#
# def fib_rec(n, f=[1, 1]):
#     if n > 2:
#         f.append(f[-1] + f[-2])
#         fib_rec(n - 1, f)
#     return f
#
#
# print(fib_rec(n))
# Вводится натуральное число n. Необходимо с помощью рекурсивной функции fact_rec вычислить факториал числа n.
# Напомню, что факториал числа, равен: n! = 1 * 2 * 3 *...* n. Функция должна возвращать вычисленное значение.
# Вызывать функцию не нужно, только объявить со следующей сигнатурой:
# n = int(input("Enter number: "))
#
#
# def fact_rec(n):
#     return 1 if n in (0, 1) else n * fact_rec(n - 1)
#
#
# print(fact_rec(n))

# С помощью рекурсивной функции get_line_list создать на его основе одномерный список из значений элементов списка d.
# Функция должна возвращать новый созданный одномерный список.  (Только возвращать, выводить на экран ничего не нужно.)
# Вызывать функцию не нужно, только объявить со следующей сигнатурой:
# def get_line_list(d, a=[]):
#     if len(d) == 0:
#         return a
#     else:
#         for el in d:
#             if type(el) == list:
#                 get_line_list(el)
#             else:
#                 a.append(el)
#         return a


# def get_line_list(d, a=[]):
#     if len(d) == 0:
#         return a
#     else:
#         for i in d:
#             if type(i) == list:
#                 get_line_list(i, a)
#             else:
#                 a.append(i)
#         return a
# d = [1, 2, [True, False], ["Москва", [1, [2, 3, [4, 5]]], "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
# print(get_line_list(d))
# print(round((3 ** 2 + 4 ** 2) ** 0.5, 2))
# import math
# n = 6
# k = 3
# m = 39
# print(int(math.factorial(n)/(math.factorial(k) * math.factorial(n - k))))
# print(math.ceil((n+m)/20))

# a, b, c = map(int, input().split())
# print(a, b, c)
# a = map(float, input())
# b = map(float, input())
# print(a, b)
# n = float(input())
# n = 78.34
# print(int(n) % 3)
# print(bool(int(n) % 3))
# print(n % 100)
# print(n % 1)
# n = float(input())
# n = 2
# print(2.1 > n > 0 or 10 > n > 20)
# s1, s2 = input().split()
# print(s1 * 2, s2 * 3)
# a, b = map(int, input().split())
# print("Переменная a = " + str(a) + ',', 'переменная b = ' + str(b))
# a, b = input().split()
# print(f'Коды: {a} = ' + str(ord(a)) + ',', b, '=', str(ord(b)))
# s = 'BA--LA---KI--RE---V'
# print(s[::2])
# s1 = 'abrakadabra'
# print(s1[4::-1])
# print(s[1::2], s1[1::2])
# print(s[1::2] == s1[1::2][:len(s[1::2])])
# print(s.capitalize())
# print(s.replace('---', '-').replace('--', '-'))
# print(input().split().rjust(3, '0'))
# s = input().split()
# book = [input() for _ in range(4)] # ввести 4 значения с новой строки и добавить в список
# print(book)
# a = [*map(int, input().split())]
# print(max(a), min(a), sum(a))
# s = [int(i) for i in input().split()]
# print(max(s), min(s), sum(s))
# lst = [int(i) for i in input().split()]
# print(*(sorted(lst, reverse=True)))
# cities = ["Мос", "Тве", "Воло"]
# lst = input().split()
# lst = cities + lst
# print(*lst)
# s = [int(i) for i in input().split()]
# s.append(s[0] > s[-1])
# print(*s)
# cities = ["Москва", "Казань", "Ярославль"]
# cities.insert(1, "Ульяновск")
# print(*cities)
# lst = [*map(str, input())]
# lst = '+7(912)123-45-67'
# print(lst)
# lst = lst.replace('+', '').replace('7', '8', 1).replace('-', '')
# print(lst)
# print(input().replace('+7', '8').replace('-', ''))
# fio = input().split()
# print(f'{fio[2]} {fio[0][0]}.{fio[1][0]}.')
# nums = [*map(int, input().split())]
# print(sorted(nums)[:3])
# print(*sorted(map(int, input().split()))[:3])
# lst = [*map(int, input().split())]
# print(lst)
# lst.append(lst.pop() % 2 != 0)
# print(lst)
# print(lst.count(2))
# lst = input().split()
# lst.sort()
# del lst[0]
# print(*lst)
# print(*sorted(input().split())[1:])
# a = [5.4, 6.7, 10.4]
# lst = a + [list(map(int, input().split()))]
# print(lst)
# lst = input().split()
# print(lst)
# print(*[input().split()[-1] for _ in range(3)])
# t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
#     ["Я", "Python", "выучил", "с", "каналом"],
#     ["Балакирев", "что", "раздавал?"]]
# p = input()
# print(p in t[0] or p in t[1] or p in t[2])
# print(p in str(t))
# s = input()
# print('ДА' if 't' and 'h' and 'o' in s else 'НЕТ')
# a, b, c, d = map(int, input().split())
# print('ДА' if a >= c+2 and b >= d+2 or a >= d+2 and b >= c+2 else 'НЕТ')
# s = input()
# print('ДА' if sum([*map(int, s[:3])]) == sum([*map(int, s[3:])]) else 'НЕТ')
# t = float(input())
# if t % 5 <= 3:
#     print('green')
# else:
#     print('red')
# m = '''1. Введение в Python
# 2. Строки и списки
# 3. Условные операторы
# 4. Циклы
# 5. Словари, кортежи и множества
# 6. Выход'''
# print(m.split('\n')[int(input()) - 1])
# a, b, c = map(int, input().split())
# if a > b:
#     a, b = b, a
# if a > c:
#     a, c = c, a
# print(a)
# m = float(input())
# if m <= 60:
#     print(1)
# elif 60 < m <= 64:
#     print(2)
# elif 64 < m <= 69:
#     print(3)
# else:
#     print(4)
# print(1 + (60 < weight) + (64 < weight) + (69 < weight))
# year = ['', 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# month, day = map(int, input().split())
# if day == 1:
#     print(f'{month-1:02}.{year[month-1]:02} {month:02}.{day+1:02}')
# elif day == year[month]:
#     print(f'{month:02}.{day-1:02} {month+1:02}.{1:02}')
# else:
#     print(f'{month:02}.{day-1:02} {month:02}.{day+1:02}')
# k = int(input())
# week = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
# print(week[k % 7 - 1])
# s = map(int, input().split())
# m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
# for el in s:
#     print('#'+m[el-1] if el in [1, 4] else m[el-1], end=' ')
# start, stop = map(int, input().split())
# while start <= stop:
#     print(start ** 2, end=' ')
#     start += 1
# price = float(input())
# numb = 2
# while numb <= 10:
#     print(round(price * numb, 2), end=' ')
#     numb += 1
# s = 0
# num = 1
# while num != 0:
#     num = int(input())
#     s += num
# print(s)
# s = input()
# while '--' in s:
#     s = s.replace('--', '-')
# print(s)
# num = [*map(int, input())]
# i = 0
# s = 1
# while i in range(len(num)):
#     s *= num[i]
#     i += 1
# print(s)
# n = int(input())
# fib1 = 1
# fib2 = 1
# fib = [fib1, fib2]
# i = 0
# while i < n - 2:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i += 1
#     fib.append(fib_sum)
# print(*fib)
# n = int(input())
# lst = [1, 1]
# while len(lst) < n:
#     lst.append(lst[-2] + lst[-1])
# print(*lst)
# n = int(input())//3
# a = 1
# while n:
#     a *= 2
#     n -= 1
# print(a)
# n = int(input())
# dep = 1000
# while n:
#     dep *= 1.05
#     n -= 1
# print(round(dep, 2))
# n, m = map(int, input().split())
# while n < m:
#     print(n+1, end=' ')
#     n += 2
# n = 100
# while n < 1000:
#     if n % 47 == 43 and n % 3 == 0:
#         print(n, end=' ')
#     n += 1
# p = [0] * 10
# while sum(p) != 5:
#     n = int(input('Введите значение: '))
#     if p[n] == 1:
#         continue
#     p[n] = 1
# print(*p)
# s = 1
# n = 1
# while n:
#     n = int(input())
#     if n < 0:
#         continue
#     if n == 0:
#         break
#     s *= n
# print(s)
# city = input().split()
# i = 0
# while i < len(city):
#     if len(city[i]) <= 5:
#         print("Net")
#         break
#     i += 1
# else:
#     print('DA')
# lst = input().split()
# i = 0
# while i < len(lst):
#     if lst[i][0].lower() == lst[i][-1]:
#         print('ДА')
#         break
#     i += 1
# else:
#     print('НЕТ')
# for el in range(10, -1, -1):
#     print(el, end=' ')
# n = int(input())
# s = 0
# n = 21
# for el in range(n):
#     print(el, end=' ')
#     if el % 3 == 0 or el % 5 == 0:
#         s += el
# print(s)
N = int(input())
p = [1]
for el in range(N):
    for x in range(el):
        p[x] = 1
print(p)
