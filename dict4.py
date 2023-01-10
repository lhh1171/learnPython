from pprint import pprint


class Person:
    x = 1

    def __init__(self, id):
        self.__id = id

    def dis(self):
        print(self.__id)


p = Person(12)
p.x = 2
p.dis = lambda x: print(x + 1)
# p.dis()
pprint(p.__dict__)
pprint(Person.__dict__)
print(type(p))
print(id(Person), id(type(p)))
p.dis(2)


class Stu(Person):
    def __int__(self, id):
        super().__init__(id)


pprint(Stu.__dict__)
