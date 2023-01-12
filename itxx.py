class XXX:
    def __init__(self,num):
        self.__num=num
    def __iter__(self):
        print("====")
        return self
    def __next__(self):
        self.__num+=1
        if self.__num>=6:
            print("报错")
            raise StopIteration
        return self.__num

# x=XXX(0)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# 一直遍历遇见raise结束
for i in XXX(0):
    print(i)