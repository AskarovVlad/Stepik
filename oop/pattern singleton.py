# class TreadData:
#     shared_attr = {'name': 'threar1',
#                    'data': {},
#                    'id': 1}
#
#     def __init__(self):
#         self.__dict__ = self.shared_attr
#
#
# th1 = TreadData()
# th2 = TreadData()
#
# print(th1.id)
# print(th2.id)
#
# th1.id = 10
#
# print(th2.id)
#
#
# def singleton(cls):
#     def inner(*args, **kwargs):
#         if not inner.instance:
#             inner.instance = cls(*args, **kwargs)
#         else:
#             pass
#
#     inner.instance = None
#     return inner
#
#
# @singleton
# class A:
#     def __init__(self, a):
#         self.a = a
#
#
# c1 = A(1)
# c2 = A(2)
# print(id(c1), id(c2))


# def singleton(class_):
#     instances = {}
#
#     def getinstance(*args, **kwargs):
#         if class_ not in instances:
#             instances[class_] = class_(*args, **kwargs)
#         return instances[class_]
#
#     return getinstance
#
#
# @singleton
# class MyClass:
#     def __init__(self, name):
#         self.name = name
#
#
# m = MyClass('Max')
# n = MyClass('Zax21')
# print(n.name)


# class Singleton(type):
#     _instances = {}
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
#         return cls._instances[cls]
#
#
# class MyClass(metaclass=Singleton):
#     pass

import random


class Singleton:
    """Classic singleton"""

    __instance = None

    def __init__(self):
        self.number = random.randint(1, 10)

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(Singleton)
        return cls.__instance


class Regular:
    """Simple class to compare behavior"""

    def __init__(self, *args, **kwargs):
        self.number = random.randint(1, 10)


def testing():
    print("Singleton instances")
    list_singleton = [Singleton() for i in range(0, 5)]
    for index, element in enumerate(list_singleton):
        print(f"Element: {index}  number : {element.number}")

    print("Instances of a regular class")
    list_regular = [Regular() for i in range(0, 5)]
    for index, element in enumerate(list_regular):
        print(f"Element: {index}  number : {element.number}")


if __name__ == "__main__":
    testing()
