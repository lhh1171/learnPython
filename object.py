a = 99


class Person:
    def __new__(cls, *args, **kwargs):
        print("new")
        return a

    def __init__(self):
        print("init")
        pass


p = Person()
print(p)
