def main_func():
    def inner_func():
        print('Hello World')
    return inner_func
a = main_func()
