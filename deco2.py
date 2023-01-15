def xxx(name):
    def _a(f):
        def _b(**kwargs):
            f(name=name,**kwargs)
        return _b
    return _a

@xxx(name="python")
def test(**kwargs):
    for k in kwargs:
        print(k,kwargs[k])

test(x=11,y="yyyy")