# get_div = lambda x, y: x/y if y else None
#
# print(get_div(4, 0))


# def counter_add(n):
#     def some_func(m):
#         m += n
#         return m
#     return some_func
#
# k = int(input())
# cnt = counter_add(2)
# print(cnt(k))


# def some_func(tp):
#     def transform(s):
#         return eval(f'{tp}({s})')
#     return transform
# tp = input()
# lst_in = [*map(int, input().split())]
# lst = some_func(tp)
# print(lst(lst_in))


# def func_decorator(func):
#     def wraper(*args, **kwargs):
#         print("---  some actions ---")
#         result = func(*args, **kwargs)
#         print("---  some actions ---")
#         return result
#
#     return wraper
#
#
# def some_func(title, tag):
#     print(f"title = {title}, tag = {tag}")
#     return f"<{tag}>{title}</{tag}>"
#
#
# f = func_decorator(some_func)
#
# tagged = f("python", "h1")
# print(tagged)

# def show_menu(func):
#     def wrapper(*args):
#         i = 0
#         for v in func(*args):
#             i += 1
#             print(f'{i}. {v}')
#
#     return wrapper
#
#
# @show_menu
# def get_menu(s):
#     return s.split()
#
#
# print(get_menu('Главная Добавить Удалить Выйти'))


# def sort_func(func):
#     def wrapper(*args):
#         return sorted(func(*args))
#
#     return wrapper
#
#
# @sort_func
# def get_list(s):
#     return [*map(int, s.split())]
#
# some_str = input()
# lst = get_list(some_str)
# print(*lst)
d = {}


def form(func):
    def wrapper(*args):
        global d
        d = dict(zip(*func(*args)))
        return d

    return wrapper


@form
def get_list(s1, s2):
    return s1.split(), s2.split()


some_str_1 = input()
some_str_2 = input()

get_list(some_str_1, some_str_2)

print(*sorted(d.items()))
