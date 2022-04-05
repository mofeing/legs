from typing import Callable
from concurrent.futures import Executor, ProcessPoolExecutor
from pycompss.


class COMPSsExecutor(Executor):
	def submit(self, __fn: Callable[_P, _T], *args: _P.args, **kwargs: _P.kwargs) -> Future[_T]:
		return super().submit(__fn, *args, **kwargs)

	def map(self, fn: Callable[..., _T], *iterables: Iterable[Any], timeout: float | None = ..., chunksize: int = ...) -> Iterator[_T]:
		return super().map(fn, *iterables, timeout=timeout, chunksize)

	def shutdown(self, wait: bool = ..., *, cancel_futures: bool = ...) -> None:
		return super().shutdown(wait, cancel_futures=cancel_futures)
