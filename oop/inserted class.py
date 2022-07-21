class Women:
    title = 'обьект класса для поля title'
    photo = 'обьект класса для поля photo'

    def __init__(self, user, psw):
        self._user = user
        self._psw = psw
        self.meta = self.Meta(user + '@' + psw)

    class Meta:
        ordering = ['id']

        def __init__(self, access):
            self._access = access


w = Women('root', '12345')
print(w.__dict__)
print(w.meta.__dict__)
    
