import skscript_interpreter as si
import mouse_event as me
from tk_calls import MouseClickButtons


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
    "M|L": me.MouseClick(None, None, MouseClickButtons.LEFT, None),  # 单个参数的鼠标指令
    "M|L|(1, 1)": me.MouseClick(1, 1, MouseClickButtons.LEFT, None),  # 多个参数的鼠标指令
    "M|M|delay=1": me.MouseClick(None, None, MouseClickButtons.MIDDLE, 1.),  # delay项+无坐标
    "M|R|(1, 1)|delay=1": me.MouseClick(1, 1, MouseClickButtons.RIGHT, 1.),  # delay项+有坐标
    "M|L|delay=0.5": me.MouseClick(None, None, MouseClickButtons.LEFT, 0.5),  # delay项为浮点数
}


def test_predef():
    for text, expected in predef_suits.items():
        res = si.solve_predef(text)
        assert res == expected


def test_key():
    for text, expected in key_suits.items():
        res = si.solve_key(text)
        assert res == expected


def test_mouse():
    for text, expected in mouse_suits.items():
        res = si.solve_mouse(text)
        assert res == expected
