class Person:
    @classmethod
    def verify_gender(cls, gender):
        if type(gender) != str or gender not in ('male', 'female'):
            print("Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
            return False
        return True

    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        self.gender = gender if self.verify_gender(gender) else 'male'

    def __str__(self):
        return f"Гражданин {self.surname} {self.name}" if self.gender == 'male' else f"Гражданка {self.surname} {self.name}"


# p = Person('gerg', 'rgr', 'efw')
# print(p.gender)

# p1 = Person('Chuck', 'Norris')
# print(p1)

# p2 = Person('Mila', 'Kunis', 'female')
# print(p2)

# p3 = Person('Оби-Ван', 'Кеноби', True)
# print(p3)

class Vector:
    def __init__(self, *args):
        self.values = sorted(filter(lambda x: type(x) is int, [*args]))

    def __str__(self):
        return f"Вектор{tuple(self.values)}" if self.values else "Пустой вектор"


# p = Vector(1, 2, 2.2, 'rgg', 3, 4, True, 10, 11)
# print(p.values)
# print(p)
#
# p1 = Vector()
# print(p1.values)
# print(p1)
#
# v1 = Vector(1, 2, 3)
# print(v1)
# v2 = Vector()
# print(v2)

class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__}: {self.name}"

    def __str__(self):
        return f"{self.name}"

c = Cat('Vasya')
print(c)
print(str(c))
