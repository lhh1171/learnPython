
def yyy(xf):
    def _():
        print("++++++++")
        xf()
        print("++++++++")
    return _

def xxx(f):
    def _():
        print("======")
        f()
        print("------")
    return _

@yyy
@xxx
@xxx
def test():
    print("test")

test()