from collections.abc import Callable
from dataclasses import dataclass


@dataclass(order=False, frozen=True, unsafe_hash=True)
class MouseClick:
    """一个dataclass，用于记录鼠标点击和间隔事件，从而运行鼠标脚本"""
    x: int
    y: int
    delay: float  # 单位为秒


class MouseEvents:
    def __init__(self, events: list[MouseClick] | None = None):
        if events is None:
            events = []
        self.events = events

    def add_MouseClick(self, pos: MouseClick):
        self.events.append(pos)

    def run_all(self, caller: Callable[[MouseClick], None]):
        for event in self.events:
            caller(event)

    def __repr__(self):
        key_lists_str = str(self.events)
        return f"{self.__class__.__name__}({key_lists_str})"

    def __str__(self):
        res = ";".join(f"({event.x}, {event.y}, delay: {event.delay}s)" for event in self.events)
        return res
