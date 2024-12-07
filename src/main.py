from functools import partial

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

import tk_calls as tc
<<<<<<< Updated upstream


VERSION = "v0.9.0 Alpha 023"
ICON_S_PATH = "../img/icon.ico"
=======
from src.tk_calls import MouseClickButtons
from tk_calls import MouseClickButtons as MCBt
import mouse_funcs as mf


# 常量
VERSION = "v0.9.0 Alpha 056"
ICON_S_PATH = "../img/icon.ico"
DEFAULT_FONT = ("Microsoft JhengHei", 12, "normal")
DELAY_FROM_TO = (0., 60.)
SAFEDEALY_FROM_TO = (0., 5.)
CLICKTIMES_FROM_TO = (1, 100000000000)
>>>>>>> Stashed changes

main = Tk()
main.title(f"SpeeKlik {VERSION}")
main.iconbitmap(ICON_S_PATH)
main.geometry("800x600")
main.resizable(False, False)

<<<<<<< Updated upstream
=======
# 变量与配置
mouse_click_button = ""
mouse_delay = 0.
mouse_safedelay = 0.
click_times = 0

>>>>>>> Stashed changes
# 打开时的提示框
open_tip_box = messagebox.Message(icon=messagebox.INFO,
                                  message=f"欢迎使用 SpeeKlik（速击）（版本{VERSION}）！",
                                  detail="SpeeKlik 是一个开源，免费，无限制的鼠标/键盘控制器（也称连点器）。\n"
                                         "我（们）将这个项目托管在 GitHub 上，如果你有能力，请加入我们，让它变得更好！\n"
                                         "地址：https://github.com/MacroMeng/SpeeKlik",
                                  title="Welcome")
open_tip_box.show()

<<<<<<< Updated upstream
=======

def mouse_click_button_select(_):
    """因为要使用变量所以必须定义在main里，太悲惨了"""
    global mouse_click_button, mouse_click_button_choice
    mouse_click_button = mouse_click_button_choice.get()


def mouse_delay_modified(_):
    """因为要使用变量所以必须定义在main里，太悲惨了"""
    global mouse_delay
    from_, to = DELAY_FROM_TO
    if (now := float(mouse_delay_choose.get())) > from_:
        mouse_delay = from_
        return
    elif now < to:
        mouse_delay = to
        return
    mouse_delay = now


def mouse_safedelay_modified(_):
    """因为要使用变量所以必须定义在main里，太悲惨了"""
    global mouse_safedelay
    from_, to = SAFEDEALY_FROM_TO
    if (now := float(mouse_safedelay_choose.get())) < from_:
        mouse_safedelay = from_
        return
    elif now > to:
        mouse_safedelay = to
        return
    mouse_safedelay = now


def mouse_clicktimes_modified(_):
    """因为要使用变量所以必须定义在main里，太悲惨了"""
    global click_times
    from_, to = CLICKTIMES_FROM_TO
    if (now := int(mouse_clicktimes_choose.get())) < from_:
        click_times = from_
        return
    elif now > to:
        click_times = to
        return
    click_times = now


def mouse_start_command():
    global mouse_delay, mouse_safedelay, click_times
    # mf.click_with_delay(None,
    #                     None,
    #                     mouse_delay,
    #                     click_times,
    #                     mouse_safedelay,
    #                     tc.button_in_pag(MouseClickButtons(mouse_click_button_choice.get())))
    mf.pag.PAUSE = mouse_safedelay
    mf.pag.click(button=tc.button_in_pag(MouseClickButtons(mouse_click_button)),
                 x=None, y=None, clicks=click_times,
                 interval=mouse_delay)


>>>>>>> Stashed changes
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

<<<<<<< Updated upstream
=======
# 鼠标功能区: 鼠标按钮选择
mouse_click_button_label = Label(mouse_widget, text="鼠标按钮|Mouse Button", font=DEFAULT_FONT)
mouse_click_button_label.grid(row=0, column=0, padx=5, pady=5)
mouse_click_button_choice = Combobox(mouse_widget,
                                     font=DEFAULT_FONT,
                                     values=(MCBt.LEFT.value, MCBt.MIDDLE.value, MCBt.RIGHT.value))
mouse_click_button_choice.grid(row=0, column=1, padx=(275, 5), pady=5, ipadx=50)
mouse_click_button_choice.bind("<<ComboboxSelected>>", mouse_click_button_select)

# 鼠标功能区: 延迟选择
mouse_delay_label = Label(mouse_widget, text="点击延迟|Click Delay   (s)", font=DEFAULT_FONT)
mouse_delay_label.grid(row=1, column=0, padx=5, pady=5)
mouse_delay_choose = Spinbox(mouse_widget,
                             from_=DELAY_FROM_TO[0],
                             to=DELAY_FROM_TO[1],
                             increment=0.01,
                             font=DEFAULT_FONT)
mouse_delay_choose.grid(row=1, column=1, padx=(275, 5), pady=5, ipadx=50)
mouse_delay_choose.bind("<ButtonRelease-1>", mouse_delay_modified)
mouse_safedelay_label = Label(mouse_widget, text="安全延迟|Safe Delay     (s)", font=DEFAULT_FONT)
mouse_safedelay_label.grid(row=2, column=0, padx=5, pady=5)
mouse_safedelay_choose = Spinbox(mouse_widget,
                                 from_=SAFEDEALY_FROM_TO[0],
                                 to=SAFEDEALY_FROM_TO[1],
                                 increment=0.01,
                                 font=DEFAULT_FONT)
mouse_safedelay_choose.grid(row=2, column=1, padx=(275, 5), pady=5, ipadx=50)
mouse_clicktimes_label = Label(mouse_widget, text="点击次数|Click Times    (s)", font=DEFAULT_FONT)
mouse_clicktimes_label.grid(row=3, column=0, padx=5, pady=5)
mouse_clicktimes_choose = Spinbox(mouse_widget,
                                  from_=CLICKTIMES_FROM_TO[0],
                                  to=CLICKTIMES_FROM_TO[1],
                                  increment=1,
                                  font=DEFAULT_FONT)
mouse_clicktimes_choose.grid(row=3, column=1, padx=(275, 5), pady=5, ipadx=50)
mouse_clicktimes_choose.bind("<ButtonRelease-1>", mouse_clicktimes_modified)

# 鼠标主功能区
mouse_start = Button(mouse_widget, text="[[[RUN]]]", command=mouse_start_command)
mouse_start.grid(row=4, column=1, padx=(375, 5), pady=5, ipadx=50, ipady=10)


>>>>>>> Stashed changes
main.mainloop()
