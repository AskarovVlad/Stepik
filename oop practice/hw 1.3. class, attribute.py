# class TravelBlog:
#     total_blogs = 0
#
#     def __init__(self, name, days):
#         self.name = name
#         self.days = days
#         TravelBlog.total_blogs += 1
#
# tb1 = TravelBlog('Франция', 6)
# tb2 = TravelBlog('Италия', 5)


class TravelBlog:
    total_blogs = 0

    @classmethod
    def count_blog(cls):
        cls.total_blogs += 1

    def __init__(self, name, days):
        self.name = name
        self.days = days
        self.count_blog()

tb1 = TravelBlog('Франция', 6)
tb2 = TravelBlog('Италия', 5)
print(TravelBlog.total_blogs)


class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'

p1 = Person()
print(hasattr(p1, 'job'))  # job class property, not instance
