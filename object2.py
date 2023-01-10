pp = [None, ]


class Person:
    def __new__(cls, *args, **kwargs):
        if pp[0] is None:
            pp[0] = super().__new__(cls)
        return pp[0]

    def __init__(self, id):
        print("init")
        self.__id = id

    def dis(self):
        print(self.__id)


p = Person(12)
p.dis()
p1 = Person(22)
p.dis()
