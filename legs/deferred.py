class Deferred(object):
    """Wraps an object whose value will be computed eventually."""

    __slots__ = ()

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        pass

    def __repr__(self) -> str:
        return f"Delayed({repr(self....)})"