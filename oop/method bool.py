class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return abs(self.x - self.y)

    def __bool__(self):
        return self.x != 0 or self.y != 0


# p1 = Point(0, 0)
# print(bool(p1))
#
# p2 = Point(1, 0)
# print(bool(p2))
#
# p3 = Point(0, 1)
# print(bool(p3))
#
# p4 = Point(False, 0)
# print(bool(p4))
#
# p5 = Point(False, True)
# print(bool(p5))
#
# p6 = Point(False, False)
# print(bool(p6))


class City:
    def __init__(self, name):
        self.name = name.title()

    def __str__(self):
        return self.name

    def __bool__(self):
        return self.name[-1] not in 'aeiou'


# p1 = City('new york')
# print(p1)
# print(bool(p1))
# p2 = City('SaN frANCISco')
# print(p2)
# print(p2 is True)

class Quadrilateral:
    def __init__(self, width, height=None):
        self.width = width
        self.height = height if height else width

    def __str__(self):
        return f"Куб размером {self.width}х{self.height}" if self.height == self.width \
            else f"Прямоугольник размером {self.width}х{self.height}"

    def __bool__(self):
        return self.width == self.height

q1 = Quadrilateral(10)
print(q1)
print(bool(q1))
q2 = Quadrilateral(3, 5)
print(q2)
print(q2 is True)
