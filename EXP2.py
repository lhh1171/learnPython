from contextlib import suppress


class Res:
    def __init__(self,name):
        self.__name=name
    def dis(self):
        print(self.__name)
    def __enter__(self):
        print("enter----")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit----","|", exc_type,"|", exc_val,"|",  exc_tb)
        pass
# 在enter里面打开一个文件，在exit关闭这个文件
# try:
#     with Res("xxx") as r:
#         r.dis()
#         raise Exception("错了")
#         print("xxxxx")
# except Exception as err:
#     print(err)


with suppress(Exception), Res("xxx") as r:
    r.dis()
    raise Exception("错了")
    print("xxxxxx")
print("yyyyy")