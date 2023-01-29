import sys
from asyncio.events import AbstractEventLoop
from typing import Any, Generic, TypeVar

if sys.version_info >= (3, 9):
    from types import GenericAlias

__all__ = ("Queue", "PriorityQueue", "LifoQueue", "QueueFull", "QueueEmpty")

class QueueEmpty(Exception): ...
class QueueFull(Exception): ...

_T = TypeVar("_T")

class Queue(Generic[_T]):
    if sys.version_info >= (3, 11):
        def __init__(self, maxsize: int = 0) -> None: ...
    else:
        def __init__(self, maxsize: int = 0, *, loop: AbstractEventLoop | None = ...) -> None: ...

    def _init(self, maxsize: int) -> None: ...
    def _get(self) -> _T: ...
    def _put(self, item: _T) -> None: ...
    def _format(self) -> str: ...
    def qsize(self) -> int: ...
    @property
    def maxsize(self) -> int: ...
    def empty(self) -> bool: ...
    def full(self) -> bool: ...
    async def put(self, item: _T) -> None: ...
    def put_nowait(self, item: _T) -> None: ...
    async def get(self) -> _T: ...
    def get_nowait(self) -> _T: ...
    async def join(self) -> None: ...
    def task_done(self) -> None: ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, type: Any) -> GenericAlias: ...

class PriorityQueue(Queue[_T]): ...
class LifoQueue(Queue[_T]): ...
