def service(path):
    def _a(f):
        def _b(**kwargs):
            x=path.split("/", 3)
            f(a=x[2],b=x[3], **kwargs)

        return _b

    return _a


@service(path="/xxxx/a1/a2")
def doGet(**req):
    for k in req:
        print(k, req[k])

doGet(x=11,y="yyyy")
