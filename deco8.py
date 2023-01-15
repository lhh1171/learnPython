import abc
import gc
from abc import ABCMeta


# 加dict
def abstractmethod(mth):
    def _(arg):
        # print("加dict")
        gc.get_referents(MyType.__dict__)[0]["abs" + mth.__name__] = None
        mth(arg)
    return _

class MyType(type):
    def __call__(self, *args, **kwargs):
        # 循环到最父类
        ss = self
        while ss.__base__.__name__ != 'object':
            ss = ss.__base__
        # print(MyType.__dict__)

        # 在最父类调用所有成员方法
        for k in ss.__dict__:
            f = ss.__dict__[k]
            if type(f).__name__ == "function":
                if f.__code__.co_argcount == 1:
                    f(1)
                elif f.__code__.co_argcount == 2:
                    f(1, 1)
                elif f.__code__.co_argcount == 3:
                    f(1, 1, 1)

        # 找到所有的抽象方法
        absMethods = []
        for k in MyType.__dict__:
            f = MyType.__dict__[k]
            sss = k
            if sss.startswith('abs'):
                absMethods.append(sss[3:len(sss)])
        # print(absMethods)

        bb = False
        # 匹配看看抽象方法又没有被实现
        # print(self.__dict__)
        for k in self.__dict__:
            ff = self.__dict__[k]
            if type(ff).__name__ == "function":
                for i in absMethods:
                    if i == ff.__name__:
                        bb = True
        if not bb:
            print("报错")


class Person(metaclass=MyType):
    @abstractmethod
    def xxx(b):
        pass


class Stu(Person):
    def xxxx(self):
        pass

    def xxx(b):
        print("nn", b)


p = Stu()
