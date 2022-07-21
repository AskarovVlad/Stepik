# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p = Point(1, 2)
# print(p.__dict__)
# p.z = 10
# print(p.__dict__)


class Point2D:
    __slots__ = ('x', 'y')

    m = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point2D(3, 4)
print(p1.m)


# p1.i = 100

class Point3D(Point2D):
    __slots__ = 'z',

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z


p2 = Point3D(10, 20, 30)
print(p2.x, p2.y, p2.z)


# print(p1.__dict__)    # AtributeError
# p1.z = 10     # AtributeError


class Rectangle:
    __slots__ = ('__width', '__height')

    def __init__(self, a, b):
        self.__width = a
        self.__height = b

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        print('setter called')
        self.__width += value

    def sum_side(self):
        return self.__width + self.__height


r = Rectangle(10, 20)
print(r)

print(r.width)
r.width = 50
print(r.width)
print(r.sum_side())
