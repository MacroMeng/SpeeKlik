"""在主程序外定义的窗口需要的函数"""
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

import pyautogui as pag


WEBSITE_ADDR = "https://github.com/MacroMeng/SpeeKlik"


<<<<<<< Updated upstream
def select_safety(ok: bool):
    """设置pyautogui.FAILSAFE值（用于在tkinter窗口中设置）"""
    pag.FAILSAFE = ok


=======
>>>>>>> Stashed changes
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
