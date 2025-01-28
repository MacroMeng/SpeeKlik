"""MouseClick和MouseEvents类"""
import collections
from collections.abc import Callable
from dataclasses import dataclass
from typing import Iterable, override, TypeAlias

import mouse_funcs as mf


Records: TypeAlias = Iterable["MouseClick | KeyClick | Environment"]


@dataclass(order=False, frozen=True)
class KeyClick:
    """一个dataclass，用于记录键盘点击和间隔事件，从而运行键盘脚本"""
    key: str
    delay: float | None  # 单位为秒


@dataclass(order=False, frozen=True)
class MouseClick:
    """一个dataclass，用于记录鼠标点击和间隔事件，从而运行鼠标脚本"""
    x: int | None
    y: int | None
    button: mf.MouseClickButtons
    delay: float | None  # 单位为秒


class MouseKeyEvents(collections.UserList):
    """一个用于记录所有鼠标/键盘事件来驱动鼠标脚本的类"""
    def __init__(self, events: Records | None = None):
        if events is None:
            events = []
        self.env = {}  # 这个脚本的环境变量（预定义）
        for event in events:
            if isinstance(event, Environment):
                self.env.update(vars(event))  # 避免有多行预定义的情况下前面定义的预定义被覆盖
        self.env = Environment(**self.env)  # 转换回Environment对象
        events = [event for event in events if event is not self.env]  # 去除预定义
        super().__init__(events)

    @override
    def __repr__(self):
        key_lists_str = ", ".join(self.data)
        return f"{self.__class__.__qualname__}({key_lists_str}, env={self.env})"

    @staticmethod
    def _single_to_string(event: Records):
        if isinstance(event, MouseClick):
            return f"(CLICK {event.x}, {event.y}, delay: {event.delay}s)"
        elif isinstance(event, KeyClick):
            return f"(PRESS {event.key!r}, delay: {event.delay}s)"
        elif isinstance(event, Environment):
            return f"(ENV {event})"

    @override
    def __str__(self):
        res = ";".join(self._single_to_string(event) for event in self.data + [self.env])
        return res


@dataclass(order=False, frozen=True)
class Environment:
    """一个用于记录环境变量的类"""
    default_delay: float = 0.05
    forever: bool = False
    safe_delay: float = 0.01
    failsafe: bool = True

    def __repr__(self):
        return f"{vars(self)}"

    def __str__(self):
        vars_str = ", ".join(f"{key}={value}" for key, value in vars(self).items())
        return f"{self.__class__.__qualname__}({vars_str})"
