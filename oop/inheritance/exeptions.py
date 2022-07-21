class Wallet:
    @classmethod
    def verify_init(cls, value):
        if not isinstance(value, str):
            raise TypeError("Неверный тип валюты")
        if len(value) != 3:
            raise NameError("Неверная длина названия валюты")
        if value != value.upper():
            raise ValueError("Название должно состоять только из заглавных букв")
        return True

    def __init__(self, currency, balance):
        if self.verify_init(currency):
            self.currency = currency
        self.balance = balance

    @staticmethod
    def validate(x, y):
        if not isinstance(y, Wallet):
            return False
        if x.currency != y.currency:
            raise ValueError("Нельзя сравнить разные валюты")
        return True

    def __eq__(self, value):
        if self.validate(self, value):
            return self.balance == value.balance
        raise TypeError(f"Wallet не поддерживает сравнение с {value}")

    def __add__(self, other):
        if self.validate(self, other):
            return Wallet(self.currency, self.balance + other.balance)
        raise ValueError("Данная операция запрещена")

    def __sub__(self, other):
        if self.validate(self, other):
            return Wallet(self.currency, self.balance - other.balance)
        raise ValueError("Данная операция запрещена")


wallet1 = Wallet('USD', 50)
wallet2 = Wallet('RUB', 100)
wallet3 = Wallet('RUB', 150)
# wallet4 = Wallet(12, 150)  # исключение TypeError('Неверный тип валюты')
# wallet5 = Wallet('qwerty', 150)  # исключение NameError('Неверная длина названия валюты')
# wallet6 = Wallet('abc', 150)  # исключение ValueError('Название должно состоять только из заглавных букв')
print(wallet2 == wallet3)  # False
# print(wallet2 == 100)  # TypeError('Wallet не поддерживает сравнение с 100')
# print(wallet2 == wallet1)  # ValueError('Нельзя сравнить разные валюты')
wallet7 = wallet2 + wallet3
print(wallet7.currency, wallet7.balance)  # печатает 'RUB 250'
# wallet2 + 45  # ValueError('Данная операция запрещена')
