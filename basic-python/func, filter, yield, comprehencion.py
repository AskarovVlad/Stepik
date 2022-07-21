def gen():
    for i in list(range(3)):
        yield i


s = gen()
print(next(s))
print(next(s))

a = [-1, -2, -3, 0, 1, 2, 3]
b = list(map(abs, a))
print(b)


def f(x):
    return x > 10
a = [0, 1, 2, 10, 11, 20, 100]
a1 = [0, 1, 2, 10, 11, 20, '', None, 100]
b = list(filter(f, a))
c = list(filter(None, a1))
print(b)
print(c)
a = [100, 200, 300]
b = ['q', 'w', 'e']
c = 'asd'
rez = zip(a, b, c)
# print(list(rez))
# for t1, t2, t3 in zip(a, b, c):
#     print(t1, t2, t3)
col1, col2, col3 = zip(*rez)
print(col1, col2, col3)
