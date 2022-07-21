class Laptop:
    MID = 100

    def __init__(self, brand, model, price):
        self.laptop_name = f'{brand} {model}'
        self.brand = brand
        self.model = model
        self.price = price


laptop1 = Laptop('hp', '15-bw0xx', 57000)
laptop2 = Laptop('lenovo', 'y-520', 37000)


# print(laptop1.__dict__)
# print(laptop2.__dict__)


class SoccerPlayer:
    def __init__(self, name, surname, goals=0, assists=0):
        self.name = name
        self.surname = surname
        self.goals = goals
        self.assists = assists

    def score(self, total_goals=1):
        self.goals += total_goals

    def make_assist(self, total_assists=1):
        self.assists += total_assists

    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')


# leo = SoccerPlayer('Leo', 'Messi')
# leo.score(700)
# leo.make_assist(500)
# leo.statistics()
# kokorin = SoccerPlayer('Alex', 'Kokorin')
# kokorin.score()
# kokorin.statistics()

class Point:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # object.__new__(cls)

        return cls.__instance

    def __del__(self):
        Point.__instance = None

    def __init__(self, x, y):
        self.x = x
        self.y = y


point = Point(1, 2)
point1 = Point(3, 4)
print(id(point), id(point1))
print(point.x, point1.x)

class Zebra:
    def __init__(self):
        self.stripes = ["Полоска белая", "Полоска черная"]

    def which_stripe(self):
        print(self.stripes[0])
        self.stripes = self.stripes[::-1]


# zebra1 = Zebra()
#
# zebra1.which_stripe()
# zebra1.which_stripe()
# zebra1.which_stripe()
# zebra1.which_stripe()


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    def is_adult(self):
        return self.age >= 18


p1 = Person('Jimi', 'Hendrix', 55)


# print(p1.full_name())
# print(p1.is_adult())


class Stack:
    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if self.values:
            return self.values.pop()
        else:
            print("Empty Stack")

    def peek(self):
        return self.values[-1] if self.values else print("Empty Stack") and None

    def is_empty(self):
        return not bool(self.values)

    def size(self):
        return len(self.values)


s = Stack()
# s.peek()
# print(s.is_empty())
# s.push('cat')
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.is_empty())
# s.push(777)
# print(s.pop())
# print(s.pop())
# print(s.size())
