class ParamHook:
    def __get__(self, instance, owner):
        print("get", instance, owner)
        return instance.__name

    def __set__(self, instance, value):
        print("set", instance, value)
        instance.__name = value

    def __delete__(self, instance):
        print("del", instance)
        del instance.__name



class Person:
    name = ParamHook()

    def xxx(self):
        pass

p = Person()
p.name="xxx"
print(p.name)
del p.name