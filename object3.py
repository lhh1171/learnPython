class MyType(type):
    def __new__(cls, *args, **kwargs):
        print(cls, "|", args, "|", kwargs)
        return super().__new__(cls,*args,**kwargs)

    def __call__(self, *args, **kwargs):
        print("abc", args)
        obj = self.__new__(self)
        self.__init__(obj, args[0])
        return obj


class Person(metaclass=MyType):
    def __new__(cls, *args, **kwargs):
        print("new")
        return super().__new__(cls)

    def __init__(self, id):
        print("init")
        self.__id = id

    def dis(self):
        print(self.__id)


p = Person(12)
p.dis()
