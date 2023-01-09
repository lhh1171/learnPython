from functools import total_ordering


@total_ordering
class Person:
    def __init__(self, id):
        self.__id = id

    def __gt__(self, other):
        return self.__id > other.__id

    def __eq__(self, other):
        return self.__id == other.__id

    def __add__(self, other):
        return Person(self.__id + other.__id)

    def __str__(self):
        return str(self.__id)

    def __repr__(self):
        return "Person: " + str(self.__id)


if __name__ == "__main__":
    p = Person(12)
    p2 = Person(12)
    print(p > p2)
    print(p == p2)
    print(p + p2)
    print(str(p + p2))
    print(repr(p + p2))
