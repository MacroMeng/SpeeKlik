import src.skscript_interpreter as si
from ..src import mouse_event as me
from ..src.tk_calls import MouseClickButtons


predef_suits = {
    "@|failsafe=True": me.Environment(failsafe=True),  # 单个参数的预定义
    "@|default_delay=0.05|failsafe=True|safe_delay=0.01":
        me.Environment(default_delay=0.05, failsafe=True, safe_delay=0.01),  # 多个参数的预定义
}
key_suits = {
    "K|1": me.KeyClick("1", 0.0),  # 单个参数的键盘指令
    "K|1|delay=1": me.KeyClick("1", 1.),  # delay项为整数
    "K|1|delay=0.5": me.KeyClick("1", 0.5),  # delay项为浮点数
}
mouse_suits = {
    "M|L": me.MouseClick(None, None, MouseClickButtons.LEFT, 0.0),  # 单个参数的鼠标指令
}
