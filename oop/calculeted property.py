class Square:
    def __init__(self, s):
        self.__side = s
        self.__area = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None

    @property
    def area(self):
        if self.__area is None:
            print("Calculate Area")
            self.__area = self.__side ** 2

        return self.__area


square_5 = Square(5)

print(square_5.side)
print(square_5.area)
print(square_5.area)

square_5.side = 8

print(square_5.side)
print(square_5.area)
print(square_5.area)
