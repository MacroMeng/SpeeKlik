"""为主程序main()提供处理鼠标/键盘的函数"""
import functools
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from typing import Callable, Any

import pyautogui as pag

import mouse_event as me

WEBSITE_ADDR = "https://github.com/MacroMeng/SpeeKlik"
DEFAULT_FONT = ("Microsoft YaHei UI", 12, "normal")


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


def report_bug():
    import webbrowser
    import os

    msg = messagebox.Message(title="你目前要做的事……",
                             icon=messagebox.QUESTION,
                             message="完成以下步骤来向我们提供详细信息！我们会非常谢谢你的！",
                             detail=f"1. 我们会打开两个窗口，一个是浏览器，一个是文件管理器。首先点开资源管理器。\n"
                                    f"2. 选中{'、'.join(f'LOG{i}.log' for i in range(1, 5 + 1))}这几个文件，复制。\n"
                                    f"3. 打开刚才出现的浏览器窗口，划到到最下面的“附件”，粘贴。\n"
                                    f"4. 详细填写其他的部分。打红色星星的地方必须填写。\n"
                                    f"5. 点击“提交”按钮。\n"
                                    f"严重的提醒：我们建议先在互联网上搜索一番，说不定有人解决了呢qwq！\n"
                                    f"或者还可以@作者的B站（可能不会立马回复）！")
    webbrowser.open("https://github.com/MacroMeng/SpeeKlik/issues/new?template=bugs.yml")
    os.system(r"explorer.exe ..\logs")
    msg.show()


def help_github():
    def github_err():
        gh_helper = Toplevel()
        gh_helper.title("GitHub，我***")
        gh_helper.geometry("900x180")
        gh_helper.resizable(False, False)
        Label(gh_helper,
              text="尝试在B站搜索，或是尝试以下软件：\n"
                   "Watt Toolkit(https://apps.microsoft.com/detail/9MTCFHS560NG?hl=zh-cn&gl=CN&ocid=pdpshare)(WIN);\n"
                   "或者在你的host文件中添加以下行(此方法提供的文字可能即将过时或无法使用）：\n"
                   "199.232.69.194  github.global.ssl.fastly.net\n"
                   "140.82.112.4 github.com\n"
                   "151.101.1.6 github.global.ssl.fastly.net\n"
                   "185.199.108.153 assets-cdn.github.com\n"
                   "185.199.109.153 assets-cdn.github.com",
              font=DEFAULT_FONT).pack()
        gh_helper.mainloop()

    def need_login():
        nl_helper = Toplevel()
        nl_helper.title("GitHub，我***")
        nl_helper.geometry("600x150")
        nl_helper.resizable(False, False)
        Label(nl_helper,
              text="没事的，至少你比上面那位哥们儿好，打开了GitHub！\n"
                   "让我来告诉你！你需要一个邮箱（没有的话，试一下Outlook或者上网冲浪）\n"
                   "然后，点击下方链接Create an account，填上Email（邮箱）、\n"
                   "Password（密码）、Username（用户名，只能是英文+数字+减号）\n"
                   "然后点击Create an account，完成一个人类检测、填写验证码\n"
                   "（发到你的邮箱了呢），然后你就能登录GitHub了！\n",
              font=DEFAULT_FONT).pack()
        nl_helper.mainloop()

    helper = Toplevel()
    helper.title("帮助")
    helper.geometry("400x80")
    helper.resizable(False, False)
    helper.iconbitmap("../img/help.ico")
    Label(helper, text="你遇到了什么问题？", font=DEFAULT_FONT).grid(
        row=0, column=0, columnspan=1, padx=5, pady=5)
    Button(helper, text="不能打开GitHub.com！", command=github_err).grid(
        row=1, column=0, padx=5, pady=5
    )
    Button(helper, text="GitHub好像要让我登录？", command=need_login).grid(
        row=1, column=1, padx=5, pady=5
    )
    helper.mainloop()
