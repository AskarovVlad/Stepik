class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        if isinstance(new_email, str) and new_email.count('@') == 1 and \
                new_email[new_email.index('@'):].find('.') != -1:
            self.__email = new_email
        else:
            print("Ошибочная почта")

    email = property(fget=get_email, fset=set_email)


# k = UserMail('belosnezhka', 'prince@wait.you')
# print(k.email)  # prince@wait.you
# k.email = [1, 2, 3]  # Ошибочная почта
# k.email = 'prince@still@.wait'  # Ошибочная почта
# k.email = 'prince@still.wait'
# print(k.email)  # prince@still.wait


class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, money):
        if isinstance(money, int) and money >= 0:
            self.total_cents = money * 100 + self.cents
        else:
            print("Error dollars")

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, money):
        if isinstance(money, int) and 0 <= money < 100:
            self.total_cents = (self.total_cents // 100) * 100 + money
        else:
            print("Error cents")

    def __str__(self):
        return f"Ваше состояние составляет {self.total_cents // 100} долларов {self.total_cents % 100} центов"


# Bill = Money(101, 99)
# print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
# print(Bill.dollars, Bill.cents)  # 101 99
# Bill.dollars = 666
# print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
# Bill.cents = 12
# print(Bill)  # Ваше состояние составляет 666 долларов 12 центов


class Person:

    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old

    def set_old(self, value):
        self.__old = value

    old = property(get_old, set_old)


# p = Person('Vlad', 26)
#
# print(p.get_old())
#
# p.set_old(35)
#
# print(p.get_old())
# print(p.old)
#
# p.old = 45
#
# print(p.old)


class Person1:

    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, value):
        self.__old = value

    @old.deleter
    def old(self):
        del self.__old


p = Person1('Lesia', 25)

print(p.old, p.__dict__)

p.old = 35

print(p.old, p.__dict__)

del p.old

print(p.__dict__)

p.old = 25

print(p.old, p.__dict__)
