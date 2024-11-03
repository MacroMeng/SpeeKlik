"""为主程序main()提供处理鼠标/键盘的函数"""
import functools
from typing import Callable

import pyautogui as pag


def safe_pause_val_wrapper(new_safe_delay: float):
    """一个装饰器，可以在被装饰的函数内部重写pyautogui.DELAY。"""
    def do_wrap(to_wrap: Callable):
        @functools.wraps(to_wrap)
        def wrapper(*args, **kwargs):
            org = pag.PAUSE
            pag.PAUSE = new_safe_delay
            try:
                to_wrap(*args, **kwargs)
            finally:
                pag.PAUSE = org
        return wrapper
    return do_wrap


def click_with_delay(x: int, y: int,
                     delay: float, times: int,
                     safe_delay: float = 0.05):
    """重复点击指定次数次，间隔指定秒"""
    @safe_pause_val_wrapper(safe_delay)
    def work():
        for i in range(times):  # 在给定的次数内循环点击
            pag.moveTo(x, y, duration=delay)
            pag.click()  # 使用safe_pause_val_wrapper设定延迟

    work()
