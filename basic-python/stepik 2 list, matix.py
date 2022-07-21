# n = int(input())
# n = 4
# a = [[1] * n for __ in range(n)]
# for i in a:
#     i[-1] = 5
# [print(*i) for i in a]
# lst_in = ['django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya',
#           'marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya']
# for i, v in enumerate(lst_in):
#     lst_in[i] = v.replace(' ', '-')
#     while '--' in lst_in[i]:
#         lst_in[i] = lst_in[i].replace('--', '-')
# for el in lst_in:
#     print(el)
# for i in lst_in:
#     print('-'.join(i.split()))

# a = []
# for i in range(2, n):
#     k = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             k += 1
#     if k == 2:
#         a.append(i)
# print(*a)
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
lst_in = [[1, 0, 0, 0, 1],
          [0, 0, 1, 0, 1],
          [0, 0, 0, 0, 0],
          [0, 1, 0, 1, 0],
          [0, 0, 0, 0, 0]]
# не касаются ли единицы друг друга по горизонтали, вертикали и диагонали
break_out_flag = False
for i in range(len(lst_in) - 1):
    if lst_in[i][-1] == 1 and lst_in[i][-1] == lst_in[i + 1][-1]:
        print('НЕТ')
        break
    for j in range(len(lst_in[i]) - 1):
        if lst_in[i][j] != 1:
            continue
        else:
            if lst_in[i][j] in [lst_in[i][j + 1], lst_in[i + 1][j], lst_in[i + 1][j + 1]]:
                break_out_flag = True
                break
    if break_out_flag:
        print('НЕТ')
        break
else:
    print('ДА')
