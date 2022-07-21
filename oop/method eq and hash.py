class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y
#   если переопределять маг метод eq, то функция hаsh перестает работать

    def __hash__(self):
        return hash((self.x, self.y))




p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)
print(hash(p1))
print(hash(p2))

d = dict()
#  данные действия позволяют использовать екземпляр в качестве ключа словаря
d[p1] = 1
print(d)
