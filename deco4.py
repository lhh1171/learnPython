def xxx(clz):
    class _:
        def __init__(self):
            self.obj=clz()
        def test(self):
            return "======"+clz().test()
        def test1(self):
            return "+++++"+clz().test1()
        def __call__(self, *args, **kwargs):
            return "------"
    return _

@xxx
class Test:
    def test(self):
        return "test"
    def test1(self):
        return "test1"

a=Test()
print(a.test(),a.test1(),a())