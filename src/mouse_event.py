"""MouseClick和MouseEvents类"""
import collections
from collections.abc import Callable
from dataclasses import dataclass
from typing import Iterable, override


@dataclass(order=False, frozen=True, unsafe_hash=True)
class KeyClick:
    """一个dataclass，用于记录键盘点击和间隔事件，从而运行键盘脚本"""
    key: str
    delay: float  # 单位为秒


@dataclass(order=False, frozen=True, unsafe_hash=True)
class MouseClick:
    """一个dataclass，用于记录鼠标点击和间隔事件，从而运行鼠标脚本"""
    x: int | None
    y: int | None
    delay: float  # 单位为秒


class MouseKeyEvents(collections.UserList):
    """一个用于记录所有鼠标/键盘事件来驱动鼠标脚本的类"""
    def __init__(self, events: Iterable[MouseClick | KeyClick] | None = None):
        if events is None:
            events = []
        super().__init__(events)

    def run_all(self, caller: Callable[[MouseClick | KeyClick], None]):
        """使用提供的函数运行所有鼠标/键盘事件"""
        for event in self.data:
            caller(event)

    @override
    def __repr__(self):
        key_lists_str = ", ".join(self.data)
        return f"{self.__class__.__qualname__}({key_lists_str})"

    @staticmethod
    def _single_to_string(event: MouseClick | KeyClick):
        if isinstance(event, MouseClick):
            return f"(CLICK {event.x}, {event.y}, delay: {event.delay}s)"
        elif isinstance(event, KeyClick):
            return f"(PRESS {event.key!r}, delay: {event.delay}s)"

    @override
    def __str__(self):
        res = ">".join(self._single_to_string(event) for event in self.data)
        return res
