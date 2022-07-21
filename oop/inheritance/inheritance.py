class NewInt(int):
    def repeat(self, n=2):
        return int(n * str(self))

    def to_bin(self):
        return int(bin(self)[2:])


# a = NewInt(9)
# print(a.repeat())  # печатает число 99
# d = NewInt(a + 5)
# print(d.repeat(3))  # печатает число 141414
# b = NewInt(NewInt(7) * NewInt(5))
# print(b.to_bin())  # печатает 100011 - двоичное представление числа 35


class Human:
    def breathe(self):
        print('Human breathe!!!')

    def walk(self):
        print('Human walk!!!')

    def combo(self):
        self.breathe()
        self.walk()
        if hasattr(self, 'help'):
            self.help()


class Doctor(Human):
    age = 35

    def help(self):
        print('Doctor help to someone!')


d = Doctor()
print(d.__dict__)

