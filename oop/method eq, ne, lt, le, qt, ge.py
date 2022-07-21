# __eq__ - Equal to, отвечает за ==
# __ne__ - Not equal to, отвечает за !=
# __lt__ - Less than, отвечает за <
# __le__ - Less than or equal to, отвечает за <=
# __gt__ - Greater than, отвечает за >
# __ge__ - Greater than or equal to, отвечает за >=

class ChessPlayer:
    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if isinstance(other, int):
            return self.rating == other
        if isinstance(other, ChessPlayer):
            return self.rating == other.rating
        return 'Невозможно выполнить сравнение'

    def __gt__(self, other):
        if isinstance(other, ChessPlayer):
            return self.rating > other.rating
        if isinstance(other, int):
            return self.rating > other
        else:
            return 'Невозможно выполнить сравнение'

    def __ge__(self, other):
        return self == other or self > other

    def __lt__(self, other):
        if isinstance(other, ChessPlayer):
            return self.rating < other.rating
        if isinstance(other, int):
            return self.rating < other
        return 'Невозможно выполнить сравнение'

    def __le__(self, other):
        return self == other or self < other

magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
print(magnus == 4000)
print(ian == 2789)
print(magnus == ian)
print(magnus > ian)
print(magnus < ian)
print(magnus < [1, 2])
print(magnus == ian)
print(magnus >= ian)
print(magnus <= ian)
print(magnus <= [1, 2])
print(magnus != ian)
print(magnus != [1, 2])
