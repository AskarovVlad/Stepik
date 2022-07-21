# print(len(set(input().lower().split())))

# s = input()
# s1 = set()
# for el in s:
#     if el.isdigit():
#         s1.add(int(el))
# print(*sorted(s1) if s1 else "NOT")

# print(len(set(iter(input, 'q'))))

# lst_in = map(int, input().split())
# print('НЕ ДОПУЩЕН' if 2 in set(lst_in) else 'ДОПУЩЕН')

# lst_1 = set(input().split())
# lst_2 = set(input().split())
# print('ДА' if lst_1.issubset(lst_2 else 'НЕТ')

# def output_res(lst_in):
#     print(f'Min = {min(lst_in)}, max = {max(lst_in)}, sum = {sum(lst_in)}')
#
# lst = [*map(int, input().split())]
#
# print(lst)
# import re
#
#
# def valid_email(email):
#     print("ДА" if re.fullmatch(r'^[a-zA-z0-9_]+@[a-zA-z0-9_]+.[a-z]+', email) else 'НЕТ')
#
# email_in = input()
# valid_email(email_in)

# def is_even(num):
#     return num % 2 == 0
#
#
# while True:
#     number = int(input())
#     if number == 1:
#         break
#     if is_even(number):
#         print(number)

# def get_tuple(s):
#     return tuple([s, len(s)])
#
# lst_cities = input().split()
# d = {}
# for lst in lst_cities:
#     d.update({get_tuple(lst)})
# a = sorted(d, key=lambda x: d[x])
# print(*a)

# def check_password(password, chars="$%!?@#"):
#     for el in chars:
#         if el in password and len(password) >= 8:
#             return True
#         else:
#             continue
#     return False
# print(check_password('12345678!'))

# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
#
# def transliteration_1(srt_in, sep='-'):
#     srt_in = srt_in.lower()
#     trans_s = ''
#     for el in srt_in:
#         if el == " ":
#             trans_s += sep
#             continue
#         elif el not in t:
#             trans_s += el
#         else:
#             trans_s += t[el]
#     return trans_s
#
#
# print(transliteration_1('Лучший курс по Python!'))
# print(transliteration_1('Лучший курс по Python!', sep='+'))
#
#
# def replace_func(func):
#     def wrapper(args):
#         str_input = func(args)
#         while '--' in str_input:
#             str_input = str_input.replace('--', '-')
#         str_input = str_input.strip(": ;.,_-")
#         return str_input
#
#     return wrapper
#
#
# @replace_func
# def transliteration(words, sep='-'):
#     words = words.lower()
#     for k, v in t.items():
#         words = words.replace(k, v)
#     for s in words:
#         if s in [':', ';', '.', ',', '_', ' ']:
#             words = words.replace(s, sep)
#
#     return words
#
#
# s = ': ;.,_Python - это круто!: ;.,_'
# print(transliteration(s))

from functools import wraps

s = '1, 2, 3 , 4 , 5'


def decorator(func):
    @wraps
    def wrapper(*args):
        return sum(func(*args))

    return wrapper


@decorator
def get_list(str_in):
    """Функция для формирования списка целых значений"""
    return [*map(int, str_in.split())]


print(get_list.__doc__)

