class Vector:

    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item):
        if 0 <= item < len(self.values):
            return self.values[item]
        else:
            raise IndexError('Индекс за границами нашей коллекции')

    def __setitem__(self, key, value):
        if 0 <= key < len(self.values):
            self.values[key] = value
        else:
            raise IndexError('Индекс за границами нашей коллекции')

    def __delitem__(self, key):
        if 0 <= key < len(self.values):
            del self.values[key]
        else:
            raise IndexError('Индекс за границами нашей коллекции')


v1 = Vector(1, 2, 3, True, False)
print(v1)

v1[2] = 4
print(v1)


# Разряженный массив

class Vector1:

    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item):
        if 0 <= item < len(self.values):
            return self.values[item]
        else:
            raise IndexError('Индекс за границами нашей коллекции')

    def __setitem__(self, key, value):
        if 0 <= key < len(self.values):
            self.values[key-1] = value
        elif key > len(self.values):
            diff = key - len(self.values)
            self.values.extend([0] * diff)
            self.values[key-1] = value
        elif key < 0:
            k = len(self.values) + key
            self.values[k] = value
        else:
            raise IndexError('Индекс за границами нашей коллекции')

    def __delitem__(self, key):
        if 0 <= key < len(self.values):
            del self.values[key]
        else:
            raise IndexError('Индекс за границами нашей коллекции')

v10 = Vector1(10, 20, 30, True, False)
print(v10)

v10[2] = 40
print(v10)

v10[10] = 100
print(v10)

v10[-20] = 99
print(v10)

print()
