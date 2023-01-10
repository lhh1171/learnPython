import x1

print(x1.__dict__)

x1.__dict__["xxx"] = 111
print(x1.__dict__["xxx"])

x1.__dict__["xxx"] = lambda x, y: x + y
print(x1.__dict__["xxx"](1, 3))

from x1 import x2

x2.__dict__["xxx"] = lambda x, y: x + y
print(x2.__dict__["xxx"](1, 3))
