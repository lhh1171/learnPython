def mydeco(f):
    def _():
        print("++++")
        f()
        print("___")
    return _

# 装饰器
@mydeco
def xxx():
    print("xxx")

# 省略了这一句
# xxx=mydeco(xxx)
xxx()