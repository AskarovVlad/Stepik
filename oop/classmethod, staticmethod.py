class Point:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, value):
        return cls.MIN_COORD <= value <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def sqr_norm(x, y):
        return x * x + y * y


# point_1 = Point(1, 2)
#
# print(point_1.get_coord())
# print(Point.get_coord(point_1))
#
# res = Point.validate(500)
#
# print(res)
# print(Point.validate(101))
# print(Point.validate(10))
#
# point_2 = Point(101, 101)
#
# print(point_2.get_coord())
# print(Point.sqr_norm(10, 10))


class Point1:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coord(self):
        return self.x, self.y

    def set_coord(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def set_bound(cls, value):
        cls.MIN_COORD = value


# pt = Point1(1, 2)
#
# print(pt.get_coord())
# print(pt.MAX_COORD, pt.MIN_COORD)
#
# pt.set_bound(200)
#
# print(pt.__dict__)
# print(Point1.MIN_COORD)


class Robot:
    population = 0

    @classmethod
    def add_pop(cls):
        cls.population += 1

    @classmethod
    def reduce(cls):
        cls.population -= 1

    @classmethod
    def how_many(cls):
        print(f"{cls.population}, вот сколько нас еще осталось")

    def __init__(self, name):
        self.name = name
        print(f"Робот {name} был создан")
        self.add_pop()

    def destroy(self):
        print(f"Робот {self.name} был уничтожен")
        self.reduce()
        del self.name

    def say_hello(self):
        print(f'Робот {self.name} приветствует тебя, особь человеческого рода')


r2 = Robot("R2-D2")  # печатает "Робот R2-D2 был создан"
r2.say_hello()  # печатает "Робот R2-D2 приветствует тебя, особь человеческого рода"
Robot.how_many()  # печатает "1, вот сколько нас еще осталось"
r2.destroy()  # печатает "Робот R2-D2 был уничтожен"
r2.name = "R2-D2"
