# a = dict()
# print(a)
# a = {"river": "река", 'road': 'Дорога', 'one': 1}
# print(a)
# a = {}
# print(a)
# a = dict(you='ты', we='мы', they='они', us='нам')
# print(a)
# a = dict([[1, 'one'], [2, 'two'], [3, 'three']])
# print(a)
# Вводятся данные в формате ключ=значение в одну строчку через пробел. Значениями здесь являются целые числа
# (см. пример ниже). Необходимо на их основе создать словарь d с помощью функции dict() и вывести его на экран командой:
# print(*sorted(d.items()))
# s = input().split()
# d = [i.split('=') for i in s]
# d = dict([[i[0], int(i[1])] for i in d])
# print(*sorted(d.items()))
# lst_in = ['5=отлично', '4=хорошо', '3=удовлетворительно']
# lst = [i.split('=') for i in lst_in]
# print(lst)
# d = {int(i): v for i, v in lst}
# print(*sorted(d.items()))
# lst_in = input().split()
# print(lst_in)
# d = dict(i.split('=') for i in lst_in)
# print(d)
# if 'house' and 'True' and '5' in d:
#     print('da')
# else:
#     print('net')

# lst_in = input().split()
# d = dict()
# for i in lst_in:
#     if i[:2] in d:
#         d[i[:2]].append(i)
#     else:
#         d[i[:2]] = [i]
# print(*sorted(d.items()))
#
# print('')

# morze = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.', 'ё': '.', 'ж': '...-', 'з': '--..',
#          'и': '..', 'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--', 'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.',
#          'с': '...', 'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.', 'ч': '---.', 'ш': '----', 'щ': '--.-',
#          'ъ': '--.--', 'ы': '-.--', 'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-', ' ': '-...-'}
# s = input('Vvedite: ')
# morze_s = ''
# for el in s:
#     morze_s = morze_s + morze[el.lower()] + " "
# morze_s = morze_s.rstrip()
# print(morze_s)
# morze_s = input().split()
# s = ''
# for el in morze_s:
#     for k, v in morze.items():
#         if el == v:
#             s += k
#             break
#
# print(s)
# s = map(int, input().split())
# d = {a: a**2 for a in s}
# print(*d)
# import sys
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# d = {}
# for el in lst_in:
#     lt = [el.split()]
#     d = {lt[0]: [lt[1]]}
#
# lst_in = input().split()
# d = dict()
# for i in lst_in:
#     if i[:2] in d:
#         d[i[:2]].append(i)
#     else:
#         d[i[:2]] = [i]
# print(*sorted(d.items()))

# d = dict()
# n = True
# while n:
#     n = int(input())
#     if not n:
#         break
#     elif n not in d:
#         d[n] = round(n**0.5, 2)
#         print(d[n])
#     else:
#         print(f'значение из кэша: {d[n]}')

# import sys


# lst_in = list(map(str.strip, sys.stdin.readlines()))

# lst_in = [x.split() for x in lst_in]
# birth_dict = dict()
# for date in lst_in:
#     if date[0] in birth_dict:
#         birth_dict[date[0]].append(date[1])
#     else:
#         birth_dict[date[0]] = [date[1]]
# [print(f'{k}: '+', '.join(birth_dict[k])) for k, v in birth_dict.items()]

# things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
#           'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
#           'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
# things = dict(sorted(things.items(), key=lambda x: -x[1]))
#
# N = 450
# backpack = []
#
# while N >= 0:
#     for k, v in things.items():
#         if N - int(v) >= 0:
#             N -= int(v)
#             backpack.append(k)
#         else:
#             continue
#     break
#
# print(*backpack)

# lst_in = ['1', 'ужасно', 'неудовлетворительно', 'удовлетворительно', 'прилично', 'отлично']
# lst = {i: v for i, v in enumerate(lst_in[1:], int(lst_in[0]))}
# print(lst[4])

# lst = [x.lower() for x in input().split()]
# lst = ['и', 'что', 'сказать', 'и', 'что', 'сказать', 'и', 'нечего', 'и', 'точка']
# print(lst)
# lst_dict = {k: lst.count(k) for k in {*lst}}
# print(lst_dict.get('и', 0))


lst_in = ['Пушкин: Сказака о рыбаке и рыбке',
          'Есенин: Письмо к женщине',
          'Тургенев: Муму',
          'Пушкин: Евгений Онегин',
          'Есенин: Русь']
d = {}
for item in lst_in:
    author, book = item.split(': ')
    d[author] = d.get(author, set()) | {book, }
print(d)
