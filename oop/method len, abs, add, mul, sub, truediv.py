class Vector:
    def __init__(self, *args):
        self.values = sorted(filter(lambda x: type(x) is int, [*args]))

    def __str__(self):
        return f"Вектор{tuple(self.values)}" if self.values else "Пустой вектор"

    def __add__(self, other):
        if isinstance(other, int):
            return Vector(*[int(v) + int(other) for v in self.values])
        elif isinstance(other, Vector) and len(other.values) == len(self.values):
            return Vector(*[self.values[i] + other.values[i] for i in range(len(self.values))])
        else:
            print(f"Вектор нельзя сложить с {other}")

    def __radd__(self, other):
        return self.values + other

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(*[v * other for v in self.values])
        if isinstance(other, Vector) and len(other.values) == len(self.values):
            return Vector(*[self.values[i] * other.values[i] for i in range(len(self.values))])
        elif isinstance(other, Vector) and len(other.values) != len(self.values):
            print(f"Умножение векторов разной длины недопустимо")
        else:
            print(f"Вектор нельзя умножать с {other}")


# v1 = Vector(1, 2, 3)
# print(v1)  # печатает "Вектор(1, 2, 3)"
#
# v2 = Vector(3, 4, 5)
# print(v2)  # печатает "Вектор(3, 4, 5)"
#
# v3 = v1 + v2
# print(v3)  # печатает "Вектор(4, 6, 8)"
#
# v4 = v3 + 5
# print(v4)  # печатает "Вектор(9, 11, 13)"
#
# v5 = v1 * 2
# print(v5)  # печатает "Вектор(2, 4, 6)"
# v5 + 'hi'  # печатает "Вектор нельзя сложить с hi"

class Point:
    def __init__(self, *args):
        self.__coord = args

    def __len__(self):
        return len(self.__coord)

    def __abs__(self):
        return list(map(abs, self.__coord))


# p = Point(1, 2)
# print(p.__dict__)
# print(p.__len__())
# print(len(p))
# p2 = Point(-1, -2)
# print(abs(p2))

class Clock:
    __DAY = 86400  # число секунд в 1 сутках

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, '0')

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Правый операнд должен быть целым числом(int) или Clock')

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        return Clock(self.seconds + sc)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Правый операнд должен быть целым числом(int) или Clock')

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        self.seconds += sc
        return self




c1 = Clock(1000)
print(c1.get_time())
c1 = c1 + 100
print(c1.get_time())
c2 = Clock(1000)
c3 = c1 + c2
print(c3.get_time())
c1 += 100
print(c1.get_time())
