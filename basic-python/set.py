a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
# a.update(b)
print(a)
c = a.intersection(b)   # елементы которые есть и в б и в а
print(c)
d = a.union(b)
print(d)
e = b.difference(a)     # елементы которые есть в б но не пренадлежат а
print(e)
e.discard(5)    # удаляет ел, но еслли его нет, то ошибку не выбивает
print(e)
a.symmetric_difference_update(b)    # изменяет само множество, елементы которые есть в б и в а но нет в обох
print(a)
a.difference_update(b)  # вычитает из а елементы которые есть в б
print(a)
