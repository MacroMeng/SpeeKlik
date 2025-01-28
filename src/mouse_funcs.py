"""为主程序main()提供处理鼠标/键盘的函数"""
import functools
from tkinter import messagebox
from typing import Callable, Any

import pyautogui as pag

import mouse_event as me

WEBSITE_ADDR = "https://github.com/MacroMeng/SpeeKlik"


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


def failsafe_val_wrapper(new_failsafe: float) -> Callable[[Any], Any]:
    """一个装饰器，可以在被装饰的函数内部重写pyautogui.PAUSE。"""
    def do_wrap(to_wrap: Callable):
        @functools.wraps(to_wrap)
        def wrapper(*args, **kwargs):
            org = pag.FAILSAFE
            pag.FAILSAFE = new_failsafe
            try:
                to_wrap(*args, **kwargs)
            finally:
                pag.FAILSAFE = org
        return wrapper
    return do_wrap


def run(command: me.MouseKeyEvents) -> None:
    env = command.env

    @safe_pause_val_wrapper(env.safe_delay)
    @failsafe_val_wrapper(env.failsafe)
    def work():
        for event in command:
            if isinstance(event, me.MouseClick):
                button_map = {me.MouseClickButtons.LEFT: pag.LEFT,
                              me.MouseClickButtons.RIGHT: pag.RIGHT,
                              me.MouseClickButtons.MIDDLE: pag.MIDDLE}
                button = button_map[event.button]
                pag.sleep(event.delay if event.delay is not None else env.delay)
                pag.click(event.x, event.y, button=button)
            elif isinstance(event, me.KeyClick):
                pag.sleep(event.delay if event.delay is not None else env.delay)
                pag.press(event.key)
    work()
