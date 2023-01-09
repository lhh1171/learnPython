class Person:
    def __init__(self):
        self.__age = 111

    @property
    def age(self):
        print("get")
        return self.__age

    @age.setter
    def age(self, age):
        print("set")
        self.__age = age

    @staticmethod
    def dis(x):
        print(x)

    @classmethod
    def xxx(cls, x):
        print(cls, x)

# get && set
p = Person()
p.age = 1
p.age

# 用类直接启动方法
Person.dis(11)
Person.xxx(12)
# 很重要
if __name__ == "__main__":
    Person.xxx(23)
