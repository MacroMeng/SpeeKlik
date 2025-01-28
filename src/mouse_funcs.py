"""为主程序main()提供处理鼠标/键盘的函数"""
import functools
from enum import Enum
from tkinter import messagebox
from typing import Callable

import pyautogui as pag

WEBSITE_ADDR = "https://github.com/MacroMeng/SpeeKlik"


class MouseClickButtons(Enum):
    LEFT = "左键|L"
    MIDDLE = "中键|M"
    RIGHT = "右键|R"


def select_safety(ok: bool):
    """设置pyautogui.FAILSAFE值（用于在tkinter窗口中设置）"""
    pag.FAILSAFE = ok


def about_speeklik(version: str, special: str = ""):
    about_box = messagebox.Message(icon=messagebox.INFO,
                                   message=f"SpeeKlik（速击）{special}\n版本{version}",
                                   detail="SpeeKlik，一个开源，免费，无限制的鼠标/键盘控制器。\n"
                                          "项目地址：https://github.com/MacroMeng/SpeeKlik",
                                   title="关于SpeeKlik")
    about_box.show()


def get_special_version_str(version: str):
    v_list = version.split()
    if len(v_list) == 1:
        return ""
    elif len(v_list) == 3:
        return v_list[1] + "版"


def open_website():
    import webbrowser
    webbrowser.open(WEBSITE_ADDR, new=1)


def safe_pause_val_wrapper(new_safe_delay: float):
    """一个装饰器，可以在被装饰的函数内部重写pyautogui.PAUSE。"""
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


def click_with_delay(x: int | None, y: int | None,
                     delay: float, times: int,
                     safe_delay: float = 0.05,
                     button: str = pag.LEFT):
    """重复点击指定次数次，间隔指定秒"""
    @safe_pause_val_wrapper(safe_delay)
    def work():
        pag.click(x, y, clicks=times, interval=delay, button=button)

    work()
