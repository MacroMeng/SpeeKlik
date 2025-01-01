"""MouseClick和MouseEvents类"""
from collections.abc import Callable
from dataclasses import dataclass
from typing import Iterable


@dataclass(order=False, frozen=True, unsafe_hash=True)
class KeyClick:
    """一个dataclass，用于记录键盘点击和间隔事件，从而运行键盘脚本"""
    key: str
    delay: float  # 单位为秒


@dataclass(order=False, frozen=True, unsafe_hash=True)
class MouseClick:
    """一个dataclass，用于记录鼠标点击和间隔事件，从而运行鼠标脚本"""
    x: int
    y: int
    delay: float  # 单位为秒


class MouseKeyEvents:
    """一个用于记录所有鼠标/键盘事件来驱动鼠标脚本的类"""
    def __init__(self, events: Iterable[MouseClick | KeyClick] | None = None):
        if events is None:
            events = []
        self.events = list(events)

    def add_event(self, pos: MouseClick | KeyClick):
        """添加一个鼠标/键盘事件"""
        self.events.append(pos)

    def run_all(self, caller: Callable[[MouseClick | KeyClick], None]):
        """使用提供的函数运行所有鼠标/键盘事件"""
        for event in self.events:
            caller(event)

    def __repr__(self):
        key_lists_str = str(self.events)
        return f"{self.__class__.__name__}({key_lists_str})"

    @staticmethod
    def _single_to_string(event: MouseClick | KeyClick):
        if isinstance(event, MouseClick):
            return f"({event.x}, {event.y}, delay: {event.delay}s)"
        elif isinstance(event, KeyClick):
            return f"({event.key!r}, delay: {event.delay}s)"

    def __str__(self):
        res = ";".join(self._single_to_string(event) for event in self.events)
        return res
