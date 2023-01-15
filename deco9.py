class Pro:
    def __init__(self,path):
        self.__path=path
    def __call__(self, *args, **kwargs):
        return "========"+self.__path("")
    def xxx(self,path2):
        def _(*args):
            # print("'''''''''",*args)
            return "+++++++"+path2(args[0],args[1])+",name"+args[1]
        return _



class Person:
    @Pro
    def xx1(self):
        return "xx1"

    @xx1.xxx
    def xx2(self,name):
        return "xx2"+name


p=Person()
print(p.xx1())
print(p.xx2("xxxx"))
