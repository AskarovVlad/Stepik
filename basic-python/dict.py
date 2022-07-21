import os

city = {'moskow': 495,
        'piter': 195,
        'ural': 295}
q = dict.fromkeys(['a', 'b', 'c'], 100)
print(city, q)
print(q.setdefault('d'))  #
print(q)
print(q.get('e'), 'not key in dict q')
print(q)

print(os.getcwd())  # в какой мы сейчас директории
s = 'I love Python'
i = 0
while s[i] != 't':
    print(s[i], end='')
    i += 1

for i in s:
    if i == ' ':
        continue
    print(i, end='')
print('123')


def extenllist(val, lists=[]):
    lists.append(val)
    return lists
 

list1 = extendlist(10)
list2 = extendlist(123, [])
list3 = extendlist('a')
print(list1, list2, list3)

list1.extend('123123123')
print(list1)
nums = [1, 2, 5, 10, 3, 100, 9, 24]
nums = [el for el in nums if el >= 5]
print(nums)
print(list(zip([1, 2, 3], ['apple', 'grape', 'orange'], ['x', 2, True])))
