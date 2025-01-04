import mouse_event as me


def solve_from_file(fn: str) -> me.MouseKeyEvents:
    """从文件中解析鼠标/键盘事件"""
    with open(fn, "r") as f:
        lines = f.readlines()
    events = me.MouseKeyEvents
