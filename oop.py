# class Person:
#     def __init__(self, a, b):
#         self._a = a
#         self._b = b
#
#     def dis(self):
#         print(self._a, self._b)
#
#
# p = Person(1, 2)
#
# p.xxx = lambda self, a, b: print(self._a, self._b, a, b)
#
#
# def yyy(self, a, b):
#     print("yyy", self._a, self._b, a, b)
#
#
# p.yyy = yyy
# p.uuu = "uuu"
# p.dis()
# Person.dis(p)
# p.xxx(p, 3, 4)
# p.yyy(p, 5, 6)
# print(p.uuu)

# =======================

# # 不能重载
# # 用默认值是可选参数，没有是必选参数
# def xxx(c, a=1, b=2):
#     print(c, a, b)
#
#
# # 不定参,传入类型是touple
# def yy(*c):
#     print(c)
#
#
# xxx(33, a=11, b=22)
# yy(2, 3, 4, 5)

# =======================
# 私有属性
class Person:
    def __init__(self, a, b):
        self.__a = a
        self._b = b

    def dis(self):
        print(self.__a, self._b)

    @property
    def b(self):
        return self._b


p = Person(1, 2)
print(p._b)

# 强制取出来
print(p._Person__a)

# print(p.__a)
