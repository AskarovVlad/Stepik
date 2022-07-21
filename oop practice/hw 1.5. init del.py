# class Point:
#     def __init__(self, x, y, color='black'):
#         self.x = x
#         self.y = y
#         self.color = color
# points = [Point(i, i) for i in range(1, 2001, 2)]
# points[1].color = 'yellow'
# print(len(points))


# from random import randint, choice
#
#
# class Line:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# class Rect:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# class Elipse:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
# figures = [Line, Rect, Elipse]
# elements = [choice(figures)(randint(1, 1000), randint(1, 1000), randint(1, 1000), randint(1, 1000)) for _ in range(217)]
# print(len(elements))
# print(elements[1].sp)
# print(elements[2].sp)
# elements = [Line(0, 0, 0, 0) if isinstance(figure, Line) else figure for figure in elements]
#
# print(elements[1].sp)
# print(elements[2].sp)
# print(elements[3].sp)
# print(elements[4].sp)


# class TriangleChecker:
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def is_triangle(self):
#         if not f'{self.a}{self.b}{self.c}'.isdigit():
#             return 1
#         elif self.a <= 0 or self.b <= 0 or self.c <= 0:
#             return 1
#         elif self.a > self.b + self.c or self.b > self.a + self.c or self.c > self.b + self.a:
#             return 2
#         else:
#             return 3
#
#
# a, b, c = 'a', 1, 2
#
# tr = TriangleChecker(a, b, c)
# print(tr.is_triangle())

# data_graph = [8, 11, 10, -32, 0, 7, 18]   # list(map(int, input().split()))
#
#
# class Graph:
#     def __init__(self, data, is_show=True):
#         self.data = data
#         self.is_show = is_show
#
#     def set_data(self, data):
#         self.data = data[:]
#
#     def show_table(self):
#         print(' '.join(str(x) for x in self.data) if self.is_show else "Отображение данных закрыто")
#
#     def show_graph(self):
#         print(f"Графическое отображение данных: " + " ".join(map(str, self.data)) if self.is_show else "Отображение данных закрыто")
#
#     def show_bar(self):
#         print(f"Столбчатая диаграмма: " + " ".join(map(str, self.data)) if self.is_show else "Отображение данных закрыто")
#
#     def set_show(self, fl_show):
#         self.is_show = fl_show
#
# gr = Graph(data_graph)
# gr.show_bar()
# gr.set_show(fl_show=False)
# gr.show_table()

# class CPU:
#     def __init__(self, name, fr):
#         self.name = name
#         self.fr = fr
#
#
# class Memory:
#     def __init__(self, name, volume):
#         self.name = name
#         self.volume = volume
#
#
# class MotherBoard:
#     def __init__(self, name, cpu: CPU, *args):
#         self.name = name
#         self.cpu = cpu
#         self.total_mem_slots = 4
#         self.mem_slots = list()
#
#         if len(args) <= 4:
#             self.mem_slots.extend(args)
#         else:
#             self.mem_slots.extend(list(args)[:4])
#
#     def get_config(self):
#         return [f'Материнская плата: {self.name}',
#                 f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
#                 f'Слотов памяти: {self.total_mem_slots}',
#                 f'Память: ' + '; '.join(map(lambda x: f'{x.name} - {x.volume}', self.mem_slots))]
#
# mb = MotherBoard('Asus', CPU("Intel", '5,5'), Memory('Kingston', '16'), Memory('Samsung', '8'))
# print(mb.get_config())

class Cart:
    def __init__(self):
        self.goods = list()

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return list(map(lambda x: f'{x.name}: {x.price}', self.goods))


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price

cart = Cart()
cart.add(TV('S', '10'))
cart.add(TV('L', '11'))
cart.add(Table('T', '5'))
cart.add(Notebook('A', '20'))
cart.add(Notebook('D', '40'))
cart.add(Cup('Q', '1'))
print(cart.get_list())
