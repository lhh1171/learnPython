c=compile("2*3","","eval")
print(eval(c))

c=compile("print('hello')","","single")
exec(c)

c=compile("""
for i in range(5):
    print(i)
""","","exec")

exec(c)

c=compile("""


x=99
for i in range(5):
    print(i)
""","yyy.py","exec")

print(c.co_firstlineno)

def xxx():
    pass
print(xxx.__code__.co_code)