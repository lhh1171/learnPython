import _collections_abc
import abc
import os
class clos():
    def __init__(self, thing):
        self.thing = thing
    def __enter__(self):
        return self.thing
    def __exit__(self, *exc_info):
        self.thing.close()

class sssp():
    def __init__(self, *exceptions):
        self._exceptions = exceptions

    def __enter__(self):
        pass

    def __exit__(self, exctype, excinst, exctb):
        return exctype is not None and issubclass(exctype, self._exceptions)

class Res:
    def __init__(self,name):
        self.__name=name
    def dis(self):
        print(self.__name)

def xxx():
    print("关闭了")

with sssp(Exception),clos(Res()) as r:
    r.dis()
    os.remove('data.py')
    raise Exception("错了")

r.dis()
print("yyyyy")
