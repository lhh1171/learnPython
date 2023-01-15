def xxx():
    print("0000")
    a=yield 11
    print("xxx1",a)
    a = yield 12
    print("xxx2", a)
    a = yield 13
    print("xxx3", a)
    yield 14

try:
    x=xxx()
    a=next(x)
    print("ret:",a)
    a=x.send("a")
    print("ret:",a)
    a=x.send("a")
    print("ret:",a)
    a=x.send("a")
    print("ret:",a)
    a = x.send("a")
    print("ret:", a)
    a = x.send("a")
    print("ret:", a)
    next(x)
    next(x)
    next(x)
except StopIteration as err:
    print("xxxxx")
    print(err)