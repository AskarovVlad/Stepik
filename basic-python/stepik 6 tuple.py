# cities = tuple(input().split())
# clear_cities = (city for city in cities if city != 'Ульяновск')
# print(*clear_cities)

# names = tuple(input().split())
# clear_names = (name.lower() for name in names if 'ва' in name or 'Ва' in name)
# print(*clear_names)

# nums = tuple(map(int, input().split()))
# clear_nums = tuple()
# for num in nums:
#     if num not in clear_nums:
#         clear_nums += (num, )
# print(*clear_nums)

# nums = tuple(map(int, input().split()))
#
# for i in range(len(nums)):
#     if nums.count(nums[i]) > 1:
#         print(i, end=' ')

# t = ((1, 0, 0, 0, 0),
#      (0, 1, 0, 0, 0),
#      (0, 0, 1, 0, 0),
#      (0, 0, 0, 1, 0),
#      (0, 0, 0, 0, 1))
#
# N = int(input())
#
# for i in t[:N]:
#     print(*i[:N])
# import sys
#
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# print(tuple(tuple(el.split()) for el in lst_in))
