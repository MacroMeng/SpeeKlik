from functools import partial

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

import mouse_funcs as mf


# 常量
VERSION = "v0.9.1 Alpha 069"
ICON_S_PATH = "../img/icon.ico"
DEFAULT_FONT = ("Microsoft YaHei UI", 12, "normal")

# TK主窗口设置
main = Tk()
main.title(f"SpeeKlik {VERSION}")
main.iconbitmap(ICON_S_PATH)
main.geometry("800x600")
main.resizable(False, False)

# 变量与配置

# 打开时的提示框
open_tip_box = messagebox.Message(icon=messagebox.INFO,
                                  message=f"欢迎使用 SpeeKlik（速击）（版本{VERSION}）！",
                                  detail="SpeeKlik 是一个开源，免费，无限制的鼠标/键盘控制器（也称连点器）。\n"
                                         "我（们）将这个项目托管在 GitHub 上，如果你有能力，请加入我们，让它变得更好！\n"
                                         "地址：https://github.com/MacroMeng/SpeeKlik",
                                  title="Welcome")
open_tip_box.show()

# 窗口菜单
menu = Menu(main)
main.config(menu=menu)
menu_edit = Menu(menu, tearoff=False)
menu_about = Menu(menu, tearoff=False)
menu.add_cascade(label="编辑", menu=menu_edit)
menu.add_cascade(label="关于", menu=menu_about)
menu_edit.add_command(label="退出",
                      command=main.destroy,
                      accelerator="Exit")
menu_about.add_command(label="关于SpeeKlik",
                       command=partial(mf.about_speeklik,
                                       VERSION,
                                       mf.get_special_version_str(VERSION)),
                       accelerator="About SpeeKlik")
menu_about.add_command(label="打开该项目的GitHub网页↗",
                       command=mf.open_website,
                       accelerator="Open SpeeKlik's GitHub Page↗")

# 窗口主体
details = Frame(main)
details.grid(row=0, column=0, padx=10, pady=10)
details_title = Label(details, text="SpeeKlik仪表盘", font=("Microsoft YaHei UI", 20, "bold"))
details_title.grid(row=0, column=0, padx=5, pady=5)

main.mainloop()
