from abc import abstractmethod
from typing import Callable, TypeVar
from typing_extensions import ParamSpec

T = TypeVar("T")
P = ParamSpec("P")


class Executor:
    @abstractmethod
    def submit(fn: Callable[P, T], *args: P.args, **kwargs: P.kwargs) -> Future[T]:
        pass
