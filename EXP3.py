from contextlib import suppress, closing


class Res:
    def __init__(self,name):
        self.__name=name
    def dis(self):
        print(self.__name)

# 不写enter exit
with suppress(Exception),closing(Res("xxx"))  as r:
    r.dis()
    raise Exception("错了")
    print("xxxxxx")
print("yyyyy")