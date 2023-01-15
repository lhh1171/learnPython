x = 10
expr = \
"""
for i in range(x):
    print(i)
"""

exec (expr,{'x':eval("x*2")})
