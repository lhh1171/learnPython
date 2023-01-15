def mystaticmethod(mth):
    def _(arg):
        mth(arg)

    return _


def clmethod(mth):
    def _(arg):
        mth(Person, arg)

    return _


class Person:
    @mystaticmethod
    def xxx(a):
        print("xxx", a)

    @clmethod
    def zzz(cls, c):
        print(cls, c)

Person.xxx(12)
Person.zzz(12)
