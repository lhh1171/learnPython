from pprint import pprint

# slot选择发布属性,
# 把dict发布出去，相加什么就加什么
class Person1:
    __slots__ = ['a','b','__dict__']

class Person2:
    pass

pprint(Person1.__dict__)
pprint(Person2.__dict__)

p=Person1()
p.c="xxx"