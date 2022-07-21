# lst_in = ['ножницы=100',
#           'котелок=500',
#           'спички=20',
#           'зажигалка=40',
#           'зеркальце=50']
# lst_dict = {k: int(v) for k, v in map(lambda x: x.split('='), lst_in)}
#
# print(*sorted(lst_dict, key=lambda x: lst_dict[x], reverse=True))
#
# lst_in = ['Номер;Имя;Оценка;Зачет',
#           '1;Портос;5;Да',
#           '2;Арамис;3;Да',
#           '3;Атос;4;Да',
#           '4;дАртаньян;2;Нет',
#           '5;Балакирев;1;Нет']
#
#
# t_sorted = tuple([(name, offset, int(grade) if grade.isdigit() else grade, int(number) if number.isdigit() else number) \
#                   for number, name, grade, offset in [*map(lambda x: x.split(';'), lst_in)]])
# print(t_sorted)

# rank_list = ['рядовой', 'сержант', 'старшина', 'прапорщик', 'лейтенант', 'капитан', 'майор', 'подполковник', 'полковник']

# def get_add(a, b):
#     if isinstance(a, str) and isinstance(b, str) or type(a) == type(b) in (int, float):
#         return a+b
#
#     return None

# def get_sum(iter_object):
#     return sum(filter(lambda x: isinstance(x, int), iter_object))
#
#
# print(get_sum([1, 2, 3, "a", True, [4, 5], "c", (4, 5)]))


# def get_even_sum(iter_object):
#     return sum(filter(lambda x: isinstance(x, int) and x % 2 == 0, iter_object))
#
#
# print(get_even_sum([1, 3, "a", True, [4, 5], "c", (4, 5)]))
#
#
# def get_list_dig(lst):
#     return [*filter(lambda x: type(x) in (int, float), lst)]
#
#
# print(get_list_dig([1, 3, "a", True, [4, 5], "c", (4, 5)]))
#
#
# def is_string(lst):
#     return all([*map(lambda x: isinstance(x, str), lst)])
#
#
# print(is_string(['1', '3', "a", 'True', '[4, 5]', "c", '(4, 5)']))

lst_x = input().split()


def is_free(s):
    return any([*map(lambda x: x == '#', s)])

print(is_free(lst_x))

