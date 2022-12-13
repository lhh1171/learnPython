a = input("please input a str:")
print("ssss", 12, "cc", a)
a = 123
b = 123
print(id(a), id(b))
print(hex(id(a)), hex(id(b)))
del a
del b

# ================================================


# 整数，浮点数，布尔
a = 123
a = 1.1
a = True
# 普通串
a = "abc\n"
# 没有特殊符号
a = r"aaa\n"
# askii串
a = b"adsfaf"
# unicode串
a = u"小于"
a = """
aaa
    bbb
        ccccc
 """
print(a)

# ================================================

# 转类型
a = 1
b = "1"
print(a+int(b))
a=1
b=True
print(a+b)

# 运算符过多自己补充
# （算术运算符
# 比较（关系）运算符
# 赋值运算符
# 逻辑运算符
# 位运算符
# 成员运算符
# 身份运算符
# 运算符优先级）
# https://www.runoob.com/python/python-operators.html
