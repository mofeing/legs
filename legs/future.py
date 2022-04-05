from typing import Callable


def passthrough(x, *args):
    def f(*args):
        return

    return f


class Future:
    def __init__(self, fn, *args, **kwargs):
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    def __add__(self, rhs) -> Future:
        return Future(object.__add__, self, rhs)

    def __iadd__(self, rhs) -> Future:
        return Future(object.__iadd__, self, rhs)
