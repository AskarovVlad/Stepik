# Виртуальное окружение (Virtual environment/ venv)
# директория с изолированным питоном и его зависимостями,
# позволяет для разных проектов иметь разные версии питона и библиотек

# Типы данных !!
types = (str, int, bool, float, None, list, tuple, dict, set, frozenset)

# Операторы
# int/float
a = 5
print(a * 2)
print(a + 3)
print(a / 2)
print(a // 2)
print(a ** 3)
print(a % 3)
a += 3
a -= 2
a /= 3
a *= 4
print(a > 4)
print(a < 4)
print(a >= 10)
print(a <= 10)
print(a != 7)
print(a == 4)

# str !!
b = 'python'
print(b + ' cool')
print(b * 3)
b += ' awesome'
b *= 4

# Словари
dct = {'key1': True}
dct['key2'] = 'value'  # добавление пары ключ/значение
dct.setdefault('key4', 5)  # безопасное добавление значения для ключа
if not dct.get('key4'):  # реализация setdefault
    dct['key4'] = 5
print(dct['key1'])  # получение значения по ключу
print(dct.get('key3', 0))  # безопасное получение значения по ключу
dct.pop('key2')  # удаления значения по ключу
dct.clear()  # очистка словаря
dct2 = {'key3': True}
dct.update(dct2)  # добавление пар ключ/значение из dct2 в dct
print(dct.keys())  # вывод всех ключей словаря
print(dct.values())  # вывод всех значений словаря

# 1 Инициализация
a = {'0': 1, '1': 1, '2': 1}
# 2 Присваивание через цикл
a = {}
for i in range(10):
    a[str(i)] = 1
print(a)
# 3 Генератор словаря (лучший вариант)
import random

a = {str(i): random.randint(0, 50) for i in range(10)}
print(a)
print('#####################')
# Ссылки в питоне
from copy import deepcopy

dct1 = {'a': 5, 'b': [8, 4, 6]}
dct2 = dct1  # dct1 и dct2 ссылаются на один объект
dct3 = dct1.copy()  # dct3 хранит копии неизменяемых и ссылки изменяемых элементов
dct4 = deepcopy(dct1)  # dct4 хранит копии всех элементов
dct1['c'] = 6
dct1['b'].append(9)

print(id(dct2))  # id объекта питона
print(dct1 is dct2)  # имеют ли объекты одинаковую ссылку
print(dct4 == dct1)  # имеют ли объекты одинаковые элементы

print(dct2)
print(dct3)
print(dct4)

# Преобразование типов
print(str(a))
c = '46'
print(int(c))
print(bool('python'))
print(bool(''))
print(bool(1))
print(bool(0))
print(bool(-1))

# Форматирование строк !
print('python cool'.split(' '))
print(' '.join(['python', 'cool']))
print('world ptn pnh'.capitalize())
print('WORLD'.lower())
print('world'.upper())
print('world ptn pnh'.title())

# Условный оператор / оператор ветвления
a = 5
if a > 3:
    print(str(a) + ' больше, чем 3')
elif a < 10:
    print(f'{a} меньше 10')
    # print('{} меньше 10' % a)
    print('{} меньше 10'.format(a))
else:
    print(f'{a} не больше 3 и {a} не меньше 10')

# Циклы !!!
d = [8, 4, 6]
for element in d:
    print(element + 4)
for i in [0, 1, 2]:
    print(d[i])
for i in range(5):
    print(i)
for i in range(len(d)):
    print(d[i])
print([element + 4 for element in d])  # генератор списка (фишка питона)

e = 4
while e < 6:
    print(e)
    e += 2

# Импорты
import math
import datetime

# Функции
def foo(x, y):
    return math.sqrt(x ** 2 + y ** 2)


print(foo(2, 3))


def foo1(x, y):
    print((x * y) ** 2)


print(foo1(2, 3))

# *Args, **Kwargs !
def foo2(*args):
    return args


print(foo2(5, True, ''))


def sum(*args):
    total = 0
    for element in args:
        total += element
    return total


print(sum(5, 7, 9))


def wrapper(**kwargs):
    kwargs.update({'datetime': datetime.datetime.now(), 'a': 5})
    return kwargs


print(wrapper(b=True, c=8))


def foo3(**kwargs):
    return kwargs


print(foo3(a=3, b=True))

# Области видимости
a = 5  # Глобальная


def foo1():
    a = 10  # Локальная
    def foo3():
        nonlocal a  # берется значение a из родительской функции
        a = 5


def foo2():
    global a  # меняет локальную область на глобальную
    a = 10

# Lambda, map, filter !!!
foo4 = lambda x, y: math.sqrt(x ** 2 + y ** 2)

print(foo4(5, 6))

print(list(map(lambda x: x + 4, d)))


import re


print('hello1 world2'.split('l'))
print(re.split('[lw]', 'hello1 world2'))
print(re.findall('\d*\sградусов$', 'сегодня температура 5 градусов'))


# ООП

class A:
    a = [15]  # хранится общая ссылка для всех объектов, не использовать

    def __init__(self, b):
        self.b = b


obj_a = A(6)
obj_b = A(7)
obj_a.a.append(10)
print(obj_a.a, obj_a.b)
print(obj_b.a, obj_b.b)


class A:
    a = 5

    def __init__(self, b):
        self.b = [b]  # отдельная ссылка для каждого объекта

    def foo(self, value_b):
        self.b.append(value_b)

obj_a = A(6)
obj_b = A(7)
obj_a.foo(6)
print(obj_a.a, obj_a.b)
print(obj_b.a, obj_b.b)

# Наследование - получение классов и методов из класса-предка


class B(A):
    def __init__(self, b, c):
        self.c = c
        super().__init__(b)  # супер вызывает срабатывание метода родительского класа

    def foo(self, value_b):
        self.b = [value_b]


obj_b = B(8, 'any_string')
print(obj_b.a, obj_b.b, obj_b.c)

# Множественное наследование


class C(B, A):
    pass


obj_c = C(9, 'fsgsgfd')
obj_c.foo(5)  # mro - метод разрешения порядка - вызывает метод, который есть у кого-либо наледника,
# в определенном порядке (1 предок, 2 предок, 1 предок первого предка, 2 предок первого предка и т. д.)

# Полиморфизм - способность менять поведение класса

# Не может быть несколько методов с одинаковыми названиями! Берется последняя реализация


class B(A):
    def foo(self, value_b):  # переопределение метода
        self.b = [value_b]

    def __eq__(self, other):  # переопределение оператора
        return self.a == other


obj_b = B(9)
print(obj_b == 9)
print(obj_b == 5)

# Инкапсуляция - сокрытие данных


class C:
    a = 'secret'
    _a = 'super_secret'  # не выводит поле в списке доступных
    __a = 'mega_super_secret'  # не позволяет обратиться по имени поля


obj_c = C()
print(obj_c.a)
print(obj_c._a)
print(obj_c._C__a)


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @staticmethod  # чтобы использовать метод без создания объекта
    def root(value):
        return math.sqrt(value)

    @classmethod  # тоже самое, но с переменной класса
    def class_inf(cls):
        return cls.__name__


print(Point.root(5))
print(Point.class_inf())
