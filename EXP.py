class MyExp(Exception):
    def __init__(self,msg):
        super().__init__(msg)

try:
    # raise MyExp("错误")
    pass
except MyExp as err:
    print(err)
else:
    print("没错")
finally:
    print("关闭资源")