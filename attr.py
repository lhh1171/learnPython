class Person:
    def __setattr__(self, key, value):
        print("set--",key,value)
        self.__dict__[key]=value
    def __getattribute__(self, item):
        if item=="__dict__":
            print("xxxx",item)
        else:
            print("__getattribute__",item)
        return super().__getattribute__(item)
    def __getattr__(self, item):
        return self.__dict__[item]

p=Person()
p.xxx=111
print("=========================")
print(p.xxx)
# 这个属性不存在走__getattribute__，存在走__getattr__