from functools import partial

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

import tk_calls as tc


VERSION = "v0.9.0 Alpha 023"
ICON_S_PATH = "../img/icon.ico"

main = Tk()
main.title(f"SpeeKlik {VERSION}")
main.iconbitmap(ICON_S_PATH)
main.geometry("800x600")
main.resizable(False, False)

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
                       command=partial(tc.about_speeklik,
                                       VERSION,
                                       tc.get_special_version_str(VERSION)),
                       accelerator="About SpeeKlik")
menu_about.add_command(label="打开该项目的GitHub网页↗",
                       command=tc.open_website,
                       accelerator="Open SpeeKlik's GitHub Page↗")

func_nb = Notebook(padding=5)
mouse_widget = Frame(main)
kb_widget = Frame(main)
func_nb.add(mouse_widget, text="鼠标")
func_nb.add(kb_widget, text="键盘")
func_nb.pack(padx=5, pady=5, fill=BOTH, expand=True)

main.mainloop()
