import gc
from pprint import pprint


def aaa():
    pass


pprint(aaa.__dict__)


class Person:
    pass

p=Person()
# 会报错
# Person.__dict__["xxx"]=111
pprint(Person.__dict__)

pprint(p.__dict__)

print(gc.get_referents(Person.__dict__))
gc.get_referents(Person.__dict__)[0]["xxx"]=lambda x,y:x+y
print(Person.__dict__["xxx"](1, 2))

