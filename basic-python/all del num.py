# n = int(input('Введите число: '))
n = 15
i = 1
lst = []
while i * i <= n:
    if n % i == 0:
        lst.append(i)
        if i != n // i:
            lst.append(n // i)
    i += 1
lst.sort()
print(lst)
s = """qwertyuiop[]asdfghjkl'zxcvbnm,.///1234567890-=+_(*&^%$#@!);:"<>?"""
s1 = {i: s.count(i) for i in s}
print(s1)
print(len(s))
print(len(set(s)))
s2 = set(s)
print(eval("''.join(s2)"))
