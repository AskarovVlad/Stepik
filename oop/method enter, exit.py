class DefenerVector:
    def __init__(self, v):
        self.__v = v

    def __enter__(self):
        self.__temp = self.__v[:]  # делаем копию вектора v
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v[:] = self.__temp
        return False


v1 = [1, 2, 3]
v2 = [1, 2, 3]
try:
    with DefenerVector(v1) as dv:
        for i, v in enumerate(dv):
            dv[i] += v2[i]
except IndexError:
    print('Error!!!!!!!!!!!')
print(v1)
