class XX:
    pass
class YY:
    pass

class B(XX,YY):
    pass
class C(YY,XX):
    pass

# class D(B,C):
#     pass
# # order (MRO) for bases XX, YY报错，父类的继承顺序关系

# # bb继承x又继承obj,bb继承了obj又继承了y,不一致了
# class BB(XX,object,YY):
#     pass

class BBB(YY):
    pass
# BBB.__bases__=(XX,)
# 修改继承关系
BBB.__bases__+=(XX,)

print(BBB.mro())
print(BBB.__base__)
print(BBB.__bases__)
