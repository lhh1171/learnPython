# def plus(a, b):
#     return a + b
#
#
# sub = lambda a, b: a - b
#
#
# def ops(f, a, b):
#     return f(a, b)
#
#
# print(type(plus), type(sub))
# print(ops(sub, 1, 2))
# print(ops(lambda a, b: a * b, 4, 2))

# ===================================
b=100
def incr():
    a=0
    def _():
        nonlocal a
        global b
        a+=1
        return a
    return _

i1=incr()
i2=incr()
print(i1())
print(i2())
print(i1())
print(i1())
print(i1())
print(i1())
print(i1())

