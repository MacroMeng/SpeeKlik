import os
from functools import partial
from tkinter import *
from tkinter import messagebox
from tkinter import Frame as OldFrame
from tkinter.filedialog import askopenfilename
from tkinter.ttk import *

import mouse_funcs as mf
import skscript_interpreter as si


# 常量
VERSION = "v0.9.1 Alpha 072"
ICON_S_PATH = "../img/icon.ico"
DEFAULT_FONT = ("Microsoft YaHei UI", 12, "normal")
COLOUR_OF_LEVELS = ["#ffffff", "#f4f4f4"]

# TK主窗口设置
main = Tk()
main.title(f"SpeeKlik {VERSION}")
main.iconbitmap(ICON_S_PATH)
main.geometry("800x600")
main.resizable(False, False)

# 变量、配置、专用函数
script_now = None


def load_script():
    global script_now

    filename = askopenfilename(title="加载一个脚本文件...", filetypes=[("SpeeKlik脚本", "*.sks")])
    if not filename:
        return
    script_now = si.solve_from_file(filename)
    details_file_loaded["text"] = f"已加载：{os.path.basename(filename)}"
    details_file_clear["state"] = "normal"


def clear_script():
    global script_now
    script_now = None
    details_file_loaded["text"] = "未加载脚本"
    details_file_clear["state"] = "disabled"


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
details = OldFrame(main, bg=COLOUR_OF_LEVELS[0])
details.grid(row=0, column=0, padx=20, pady=20, sticky=W + E, ipadx=202)
details_title = Label(details, text="SpeeKlik仪表盘",
                      font=("Microsoft YaHei UI", 20, "bold"), background=COLOUR_OF_LEVELS[0])
details_title.grid(row=0, column=0, columnspan=1, padx=5, pady=5, sticky=W)
details_version = Label(details, text=VERSION, font=DEFAULT_FONT, background=COLOUR_OF_LEVELS[0])
details_version.grid(row=0, column=1, padx=5, pady=5, sticky=E)
details_file = OldFrame(details, bg=COLOUR_OF_LEVELS[1])
details_file.grid(row=1, column=0, padx=20, pady=20, sticky=W, ipady=120)
details_file_title = Label(details_file, text="加载的脚本",
                           font=("Microsoft YaHei UI", 16, "bold"), background=COLOUR_OF_LEVELS[1])
details_file_title.grid(row=0, column=0, padx=5, pady=2, sticky=W)
details_file_loaded = Label(details_file, text="未加载脚本", font=DEFAULT_FONT, background=COLOUR_OF_LEVELS[1])
details_file_loaded.grid(row=1, column=0, padx=5, pady=2, sticky=W)
details_file_look = Button(details_file, text="查看脚本操作(Coming S∞n)", state="disabled")
details_file_look.grid(row=2, column=0, padx=5, pady=2, sticky=W)
details_file_add = Button(details_file, text="加载一个脚本", command=load_script)
details_file_add.grid(row=3, column=0, padx=5, pady=2, sticky=W)
details_file_clear = Button(details_file, text="清除已加载脚本", command=clear_script, state="disabled")
details_file_clear.grid(row=4, column=0, padx=5, pady=2, sticky=W)


main.mainloop()
