import abc
from abc import abstractmethod, ABCMeta


class Person(metaclass=ABCMeta):
    @abc.abstractmethod
    def xxx(self):
        pass


class Stu(Person):
    def xxxx(self):
        pass


if __name__ == "__main__":
    p = Stu()
