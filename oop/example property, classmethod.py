# ФИО только русские буквы и дефис
# возраст целое число от 14 до 120
# серия и номер паспорта в формате хххх хххххх, где х цыфра 0-9
# вес вещественное число от 40 до 500


class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, age, passport_id, weight):
        self.verify_fio(fio)
        self.verify_age(age)
        self.verify_pwd_id(passport_id)
        self.verify_weight(weight)

        self.fio = fio
        self.age = age
        self.passport = passport_id
        self.weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('ФИО должно быть строкой')

        f = fio.split()
        if len(f) != 3:
            raise TypeError("Неверный формат ФИО")

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for string in f:
            if len(string) < 1:
                raise TypeError('В ФИО должен быть хоть 1 символ')
            if len(string.strip(letters)) != 0:
                raise TypeError('В ФИО недопустимые символыб можно использовать только буквы и дефис')

    @classmethod
    def verify_age(cls, age):
        if type(age) != int or 14 < age > 120:
            raise TypeError('Возраст должен быть целым числом от 14 до 120')

    @classmethod
    def verify_weight(cls, weight):
        if any((not isinstance(weight, (int, float)), weight < 40, weight > 500)):
            raise TypeError('Вес должен быть числом в диапазоне от 40 кг до 500')

    @classmethod
    def verify_pwd_id(cls, psw):
        if type(psw) != str:
            raise TypeError('Пасспорт ИД должен быть строкой')
        psw_list = psw.split()
        if len(psw_list) != 2 or len(psw_list[0]) != 4 or len(psw_list[1]) != 6:
            raise TypeError("Неверный формат паспорта")

        for num in psw_list:
            if not num.isdigit():
                raise TypeError("Серия и номер паспорта должны быть числами")

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        self.verify_fio(fio)
        self.__fio = fio

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.verify_age(age)
        self.__age = age

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def pasport(self):
        return self.passport

    @pasport.setter
    def pasport(self, pst_id):
        self.verify_pwd_id(pst_id)
        self.passport = pst_id


# p = Person('Аск Влад Серг', 120, '9999 777777', 499)
# print(p.__dict__)
#
# print(p.fio)
# p.fio = 'Аскаров Владислав Сергеевич'
# print(p.fio)
#
# print(p.age)
# p.age = 26
# print(p.age)
#
# # p.fio = 'кдпб'
# # print(p.fio)
#
# print(p.pasport)
# p.pasport = '1234 123456'
# print(p.pasport)
#
# print(p.weight)
# p.weight = 69
# print(p.weight)

from string import ascii_letters


class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @staticmethod
    def is_include_digit(pwd):
        for symbol in pwd:
            if symbol.isdigit():
                return True
        raise ValueError('Пароль должен содержать хотя бы одну цифру')

    @staticmethod
    def is_include_all_register(pwd):
        s_upper = 0
        for symbol in pwd:
            if symbol.isupper():
                s_upper += 1
        if s_upper >= 2:
            return True
        raise ValueError('Пароль должен содержать хотя бы 2 заглавные буквы')

    @staticmethod
    def is_include_only_latin(pwd):
        s = ascii_letters + '0123456789'
        for symbol in pwd:
            if symbol not in s:
                raise ValueError('Пароль должен содержать только латинский алфавит')

    @staticmethod
    def check_password_dictionary(other):
        if other + '\n' in ['123456\n', 'password\n', '123456789\n', '12345\n', '12345678\n', 'qwerty\n', '1234567\n',
                            '111111\n', '1234567890\n', '123123\n', 'abc123\n', '1234\n', 'password1\n', 'iloveyou\n',
                            '1q2w3e4r\n', '000000\n', 'qwerty123\n', 'zaq12wsx\n', 'dragon\n', 'sunshine\n',
                            'princess\n',
                            'letmein\n', '654321\n', 'monkey\n', '27653\n', '1qaz2wsx\n', '123321\n', 'qwertyuiop\n',
                            'superman\n', 'asdfghjkl\n']:
            raise ValueError('Ваш пароль содержится в списке самых легких')

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, other):
        if "@" not in other:
            raise ValueError("Login must include at least one ' @ '")
        if '.' not in other:
            raise ValueError("Login must include at least one ' . '")
        self.__login = other

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, other):
        print('setter called')
        if not isinstance(other, str):
            raise TypeError("Пароль должен быть строкой")
        if len(other) < 5 or len(other) > 11:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        self.is_include_digit(other)
        self.is_include_all_register(other)
        self.is_include_only_latin(other)
        self.check_password_dictionary(other)
        self.__password = other


c = Registration('login@gmail.com', 'asdfghjKL1')
c1 = Registration('dsvsvs', 'efwf')


class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if isinstance(x, (int, float)):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) in (int, float):
            self.__y = y

    def __str__(self):
        return f'{self.__class__.__name__}{self.x, self.y}'


p1 = Point("1", 2)
print(p1.__dict__)
print(p1.x, p1.y)


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __str__(self):
        return f'{self.__class__.__name__}{self.coordinates.x, self.coordinates.y}'

v1 = Vector(Point(1, 2))
print(v1.coordinates.x)
print(p1)
print(v1)
