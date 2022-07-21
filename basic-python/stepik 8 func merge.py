# def get_biggest_city(*args):
#     a = ''
#     for i in args:
#         if len(a) < len(i):
#             a = i
#     return a
#
# print(get_biggest_city('Питер', 'Москва', 'Самара', 'Воронеж'))

# def get_data_fig(*args, **kwargs):
#     d = {'type': None, 'color': None, 'closed': None, 'width': None}
#     for k, v in kwargs.items():
#         d[k] = v
#
#     return tuple([sum(args), *[v for v in d.values() if v is not None]])
#
#
# print(get_data_fig(2, 3, 4, type=True, width=23, color=13, closed=False))
#
#
# def get_data_fig(*args, **kwargs):
#     """Best version previous func"""
#     return (sum(args),) + tuple(kwargs.get(i) for i in ['type', 'color', 'closed', 'width'] if i in kwargs)


# def is_isolate(lst_in):
#     for i in range(len(lst_in) - 2):
#         if lst_in[i] + lst_in[i+1] > 1:
#             return False
#     return True
#
#
# def verify(lst):
#     res = True
#     for list_input in lst:
#         res = is_isolate(list_input)
#         if res is False:
#             return res
#     for i in range(len(lst) - 1):
#         lis = [lst[i][j] + lst[i + 1][j] for j in range(len(lst))]
#         if 2 in lis or '11' in ''.join([str(_) for _ in lis]):
#             return False
#     return res

lst_in3 = [[1, 0, 0, 0, 0],
           [0, 0, 1, 0, 1],
           [0, 0, 0, 0, 0],
           [0, 1, 0, 1, 0],
           [0, 0, 0, 0, 0]]

lst_in2 = [[1, 0, 0, 0, 1],
           [0, 0, 1, 0, 1],
           [0, 0, 0, 0, 1],
           [0, 1, 0, 0, 1],
           [0, 0, 0, 0, 1]]

lst_in4 = [[1, 0, 0, 0, 0],
           [0, 0, 1, 0, 1],
           [0, 0, 0, 0, 0],
           [0, 1, 0, 0, 0],
           [1, 1, 1, 1, 1]]
lst_in1 = [[1, 0, 0, 0, 1],
           [0, 0, 1, 0, 1],
           [0, 0, 0, 0, 0],
           [0, 1, 0, 1, 0],
           [0, 0, 0, 0, 0]]


def is_isolate(i, j, a):
    return 1 if a[i][j] + a[i][j + 1] + a[i + 1][j] + a[i + 1][j + 1] > 1 else 0


def verify(a):
    m_len = len(a)
    lst = [is_isolate(i, j, a) for i in range(m_len - 1) for j in range(m_len - 1)]
    return not (1 in lst)


print(verify(lst_in1), verify(lst_in2), verify(lst_in3), verify(lst_in4))

# for i in range(4):
#     ls = [lst_in1[i][j] + lst_in1[i + 1][j] for j in range(5)]
#     if 2 in ls or '11' in ''.join([str(_) for _ in ls]):
#         print('НЕТ')
#         break
# else:
#     print('ДА')

# def str_min(str_1, str_2):
#     return min(str_1, str_2)
#
#
# def str_min3(str_1, str_2, str_3):
#     return min(str_min(str_1, str_2), str_3)
#
#
# def str_min4(str_1, str_2, str_3, str_4):
#     return min(str_min3(str_1, str_2, str_3), str_4)

# nums = map(float, input().split())
# cities = input().split()
# lst = [*nums, *cities]
# print(*lst)

# lst_in = [*map(int, input().split())]


# def merge(l_1, l_2):
#     gen_list = []
#     i = 0
#     j = 0
#     while i < len(l_1) and j < len(l_2):
#         if l_1[i] <= l_2[j]:
#             gen_list.append(l_1[i])
#             i += 1
#         else:
#             gen_list.append(l_2[j])
#             j += 1
#     gen_list += l_1[i:] + l_2[j:]
#     return gen_list
#
#
# def separation(lst):
#     n = len(lst) // 2
#     lst_1 = lst[:n]
#     lst_2 = lst[n:]
#     if len(lst_1) > 1:
#         lst_1 = separation(lst_1)
#     if len(lst_2) > 1:
#         lst_2 = separation(lst_2)
#     return merge(lst_1, lst_2)
#
#
# print(*separation(lst_in))
