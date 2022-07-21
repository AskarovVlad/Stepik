# class Mark:
#     def __init__(self, value):
#         self.value = value
#         self.index = 0
#
#     def __iter__(self):
#         print('call iter Mark')
#         return self
#
#     def __next__(self):
#         print('call next Mark')
#         if self.index >= len(self.value):
#             self.index = 0
#             raise StopIteration
#         value = self.value[self.index]
#         self.index += 1
#         return value


# m = Mark([1, 2, 3, 4, 5])


class Student:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __getitem__(self, item):
        return self.marks[item]

    def __iter__(self):
        print('call iter Student')
        self.index = 0
        return iter(self.marks)

    def __next__(self):
        print('call next Student')
        if self.index >= len(self.marks):
            self.index = 0
            raise StopIteration
        value = self.marks[self.index]
        self.index += 1
        return value


s = Student('Vlad', 'Ask', [1, 2, 3, 4, 5])
print(s.marks)
for el in s:
    print(el)


# class Iterable:
#     MAX_VALUE = 5
#
#     def __init__(self):
#         self.current_value = 0
#
#     def __next__(self):
#         if self.current_value < self.MAX_VALUE:
#             self.current_value += 1
#             return self.current_value
#         raise StopIteration
#
#
# class CustomIterator:
#     def __iter__(self):
#         return Iterable()
#
#
# c = CustomIterator()
# for i in c:
#     print(i)
