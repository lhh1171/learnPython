import os
from contextlib import ContextDecorator


class suppress(ContextDecorator):
    def __init__(self, *exceptions):
        self._exceptions = exceptions

    def __enter__(self):
        print(1)

    def __exit__(self, exctype, excinst, exctb):
        print(exctype,excinst,exctb)
        print(3)
        # exctype不为空且是exctype, self._exceptions的子类返回true
        print(exctype is not None and issubclass(exctype, self._exceptions))
        return exctype is not None and issubclass(exctype, self._exceptions)


@suppress(FileNotFoundError)
def test_exception():
    print(2)
    os.remove('data.py')


test_exception()