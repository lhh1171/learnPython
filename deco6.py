class XXX():
    def __call__(self, *args, **kwargs):
        def _():
            return "====="+args[0]()
        return _

@XXX()
def test():
    return "test"


print(test())