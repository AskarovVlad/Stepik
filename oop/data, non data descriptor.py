class ReadInyX:
    def __set_name__(self, owner, name):
        self.name = '_x'


class IntegerData:
    @classmethod
    def verify_int(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом")

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        # return instance.__dict__[self.name] то же самое
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_int(value)
        # instance.__dict__[self.name] = value то же самое
        setattr(instance, self.name, value)


class Point:
    x = IntegerData()
    y = IntegerData()
    z = IntegerData()
    xr = ReadInyX()

    def __init__(self, a, b, c):
        self.x = a
        self.y = b
        self.z = c


p1 = Point(1, 2, 3)
print(p1.__dict__)
print(p1.z)
