# a, b = map(int, input().split())
#
# gen = (x ** 2 for x in range(a, b + 1))
# tp = tuple(gen)
# print(tp)
#
# a, b = map(int, input().split())
# gen = (abs(x) for x in range(a, b + 1))
# i = 0
# for el in gen:
#     print(el)
#     i += 1
#     if i == 5:
#         break

# from string import ascii_lowercase
#
# gen = (s + s1 for s in ascii_lowercase for s1 in ascii_lowercase)
# for i in range(50):
#     print(next(gen), end=' ')

# from itertools import cycle

# cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
# gen = cycle(cities)
# for i in range(20):
#     print(next(gen), end=' ')

# gen = (cities[j] for i in range(int(1000000)) for j in range(6))
# for i in range(20):
#     print(next(gen), end=' ')

# a, b = map(int, input().split())
# gen = (0.5 * ((i/100) ** 2) - 2 for i in range(0, 1000))
#
# for i in range(20):
#     print(next(gen), end=' ')
# s = input()
# s_lst = s.split()
# tp = tuple(tuple(x.split('=')) for x in s_lst)
# print(tp)

# tp = tuple(map(lambda x: tuple(x.split('=')), s_lst))
# print(tp)

# N = 7


# def get_sum(num):
#     for i in range(1, num + 1):
#         yield sum(range(1, i + 1))
#
#
# def get_balakirev(n):
#     if n <= 3:
#         yield 1
#
#     yield next(get_balakirev(n - 1)) + next(get_balakirev(n - 2)) + next(get_balakirev(n - 3))
#
#
# for i in range(1, N + 1):
#     print(next(get_balakirev(i)), end=' ')
#
#
# print()
# def get_balakirev_1(n):
#     a = b = c = 1
#     for _ in range(N):
#         yield a
#         a, b, c = b, c, a + b + c
#
# print(*get_balakirev_1(N))


# import random
#
# random.seed(1)


# chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
#
#
# def gen_pswd(n):
#     password = ''
#     for i in range(n):
#         indx = random.randint(0, len(chars))
#         password += chars[indx]
#     yield password
#
# for _ in range(5):
#     print(next(gen_pswd(10)))

# chars = ascii_lowercase + ascii_uppercase
#
#
# def gen_pswd(n):
#     password = ''
#     for i in range(n):
#         indx = random.randint(0, len(chars) - 1)
#         password += chars[indx]
#     yield password + '@mail.ru'
#
#
# for _ in range(5):
#     print(next(gen_pswd(N)))

# def get_prime_num():
#     n = 1000
#     for num in range(2, n):
#         for j in range(2, num):
#             if num % j == 0:
#                 break
#         else:
#             yield num
#
# prime = get_prime_num()
# for i in range(20):
#     print(next(prime), end=' ')
#
#
# def prime_generator(end):
#     for n in range(2, end):
#         for x in range(2, n):
#             if n % x == 0:
#                 break
#         else:
#             yield n
#
#
# g = prime_generator(1000)
# for i in range(20):
#     print(next(g), end=' ')

# lst_in = ['зонт=1000',
#           'палатка=10000',
#           'спички=22',
#           'котелок=543']
#
# lst_tup = tuple(map(lambda x: tuple(x.split('=')), lst_in))
# lst = filter(lambda x: x[0] if int(x[1]) > 500 else None, lst_tup)
# for el in lst:
#     print(el[0], end=' ')

# s1 = [1, 5, 2, 7, 10, 25, 50, 100]
# s2 = [5, 2, 3, 7, 10, 25, 55]
# s3 = set(s1) & set(s2)
# s3 = filter(lambda x: not x % 2, s3)
# print(*s3)
# import re
# lst_email = ['abc@it.ru', 'dfd3.ru@mail', 'biba123@list.ru', 'sc_lib@list.ru', '$fg9@fd.com', 'vladislav.oskarov30@gmail.com']
#
# s = filter(lambda x: True if re.fullmatch(r"^[0-9a-zA-Z-._]+@[a-zA-Z0-9-_]+\.[a-zA-Z0-9-.]{2,3}", x) else False, lst_email)
#
# print(*list(s))


# cities = input().split()
# cities = ['Москва', 'Уфа', 'Тула', 'Самара', 'Омск', 'Воронеж', 'Владивосток', 'Лондон', 'Калининград', 'Севастополь']
# lst = zip(*[iter(cities)]*3)
# print(*lst)

# lst = [1, 2, 3, 4, 5, 6]
# lst.sort(key=lambda x: x % 2)




