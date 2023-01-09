class Person:
    @property
    def age(self):
        return self.age
    @age.setter
p=Person()
p.age=1000