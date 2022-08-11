import math


class Point:
    def __init__(self):
        self.counter = 0
        self.summa = 0
        self.length = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        self.summa += sum(args)
        self.length += len(args)
        print(f'Экземпляр вызывался {self.counter} раз')

# p1 = Point()
# print(p1.__dict__)
# p1()
# p1()
# print(p1.summa, p1.length, p1.counter)
# p1(1, 2, 3)
# print(p1.summa, p1.length, p1.counter)
#
# p2 = Point()
# p2()
# p2()
# p2(4, 5, 6)
# print(p2.summa, p2.length, p2.counter)


class Counter:
    INSTANCE = 0

    @classmethod
    def counter_instance(cls):
        cls.INSTANCE += 1

    def __init__(self):
        self.__counter = 0
        self.counter_instance()

    def __call__(self, *args, **kwargs):
        self.__counter += 1
        print(f'Класс {self}, экземпляр {self.INSTANCE}: вызывался {self.__counter} раз')

    def __str__(self):
        return 'Counter'

# c = Counter()
# c()
# c()
# print(c.__dict__)
# c2 = Counter()
# c2()
# c2()
# c3 = Counter()
# c3()
# c3()


class StripStr:
    def __init__(self, chars=' '):
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError('Аргумент должен быть строкой')

        return args[0].strip(self.__chars)

s = StripStr('!?><:;<. ')
res = s('. :; Hello World <><!?')
print(res)

s1 = StripStr()
res = s1("!! Hello Wow !!")
print(res)


class Derivate:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx


@Derivate
def df_func(x):
    return math.sin(x)

print(df_func(math.pi/3))
