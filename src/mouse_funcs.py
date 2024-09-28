"""为主程序main()提供处理鼠标/键盘的函数"""
import functools

import pyautogui as pag


def pause_val_wrapper(func, new_delay):
    """一个装饰器，可以在被装饰的函数内部重写pyautogui.DELAY。"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        org = pag.PAUSE
        pag.PAUSE = new_delay
        try:
            func(*args, **kwargs)
        finally:
            pag.PAUSE = org
    return wrapper


def click_with_delay(x: int, y: int, delay: float, times: int):
    """重复点击指定次数次，间隔指定秒"""
    def work():
        for i in range(times):  # 在给定的次数内循环点击
            pag.moveTo(x, y)
            pag.click()

    work = pause_val_wrapper(work, delay)  # 使用pause_val_wrapper设定延迟
    work()


def select_safety(ok: bool):
    """设置pyautogui.FAILSAFE值（用于在tkinter窗口中设置）"""
    pag.FAILSAFE = ok
