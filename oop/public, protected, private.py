class Point:

    def __init__(self, x, y):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @classmethod
    def __check_value(cls, x):
        return isinstance(x, (int, float))

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Coordinates must be numbers')

    def get_coord(self):
        return self.__x, self.__y


point_1 = Point(1, 2)

print(point_1.get_coord())

point_1.set_coord(10, 20)

print(point_1.get_coord())

# point_1.set_coord('rg', 'gr')

print(dir(point_1))

print(point_1._Point__x)
print(point_1._Point__y)

point_1._Point__x = 22
point_1._Point__y = 33

print(point_1.get_coord())

print(point_1._Point__check_value('10'))
