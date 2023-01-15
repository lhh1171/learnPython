class XXX():
    def __init__(self,f):
        self._f=f
    def __call__(self, *args, **kwargs):
        return "====="+self._f()

@XXX
def test():
    return "test"


print(test())