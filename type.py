print(type(type(1)))

Person = type("Person", (object,), {"x": 99, "dis": lambda self: print(self.x)})
p = Person()
p.dis()


class Stu(object, metaclass=type):
    x = 100

    def dis(self):
        print(self.x)


s = Stu()
s.dis()
