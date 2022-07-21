class Point:
    MIN_COORD = 11
    MAX_COORD = 101

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattribute__(self, item):
        print(f'Вызван маг метод __getattribute__. Автовызов при обращении к атрибуту: {item} класа: {self} '
              f'через екз. класса и возвращает это значение')
        return object.__getattribute__(self, item)  # если нет return, то по умолчанию возвращает None

    def __setattr__(self, key, value):
        print(f'Вызван маг метод __setattr__. Автовызов при изменении или присвоении свойству: {key} значения: {value}')
        object.__setattr__(self, key, value)
        # self.key = value  # если через self, то будет выполнятья по рекурсии и вызовет ошибку глубины рекурсии
        # self.__dict__[key] = value

    def __getattr__(self, item):
        print(f"Вызван маг метод __getattr__. Автовызов при обращении к несуществующему атрибуту: {item} екз. класа"
              f"если такого нет, возвращает None, если есть, не вызывается")

    def __delattr__(self, item):
        print(f"Вызван маг метод __delattr__. Автовызов при удалении существующего или не существующего атрибута : {item}")
        object.__delattr__(self, item)


pt = Point(1, 2)

print(pt.__dict__)
print(Point.MIN_COORD)

a = pt.x

print(a)

print(pt.xyz)
print(pt.__dict__)

del pt.x

print(pt.__dict__)
