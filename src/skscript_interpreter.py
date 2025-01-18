import mouse_event as me
import errors as e
import re

from tk_calls import MouseClickButtons as MCBt


def solve_from_file(fn: str) -> me.MouseKeyEvents:
    """从文件中解析鼠标/键盘事件"""
    with open(fn, "r") as f:
        lines = f.readlines()
    events = me.MouseKeyEvents()
    for line in lines:
        match line[0]:
            case "K":
                new = solve_key(line)
            case "M":
                new = solve_mouse(line)
            case "@":
                new = solve_predef(line)
            case "\n" | " " | "#":
                continue
            case _:
                raise e.LineBeginError(f"Invalid line: {line}")
        events.append(new)
    return events


def solve_key(line: str) -> me.KeyClick:
    """解析一行字符串，返回一个KeyClick对象"""
    if line[:2] != "K|":
        raise e.LineBeginError(f"Invalid line: {line}")
    line = line[2:]
    args = line.split("|")
    try:
        match len(arg_key := args[0]):
            case 1:
                key = str(arg_key)
            case 6 | 7 | 8:
                key = chr(int(arg_key[2:], base=16))
            case _:
                raise e.InvalidParamError(f'The first argument of key command Line "{line}" '
                                          f'must be a char or a hex number start with "U+".')
    except ValueError as exc:
        raise e.InvalidParamError(f'The first argument of key command line "{line}" '
                                  f'is not a valid hex of Unicode. Read the documents '
                                  f'at .../SpeeKlik/doc/script_writing.md for more information.')\
              from exc
    except IndexError as exc:
        raise e.InvalidParamError(f'The key command line "{line}" has no arguments.')\
              from exc
    try:
        match args_other := args[1:]:
            case []:
                delay = 0.0
            case [delay]:
                delay = float(delay)
            case _:
                raise e.InvalidParamError(f'The key command line "{line}" has too many/less arguments.')
    except ValueError as exc:
        raise e.InvalidParamError(f'The second argument of key command line "{line}" '
                                  f'is not a valid float.')\
              from exc

    return me.KeyClick(key, delay)


def solve_mouse(line: str) -> me.MouseClick:
    """解析一行字符串，返回一个MouseClick对象"""
    if line[:2] != "M|":
        raise e.LineBeginError(f"Invalid line: {line}")
    line = line[2:]
    args = line.split("|")
    try:
        match len(arg_button := args[0]):
            case "L": button = MCBt.LEFT
            case "M": button = MCBt.MIDDLE
            case "R": button = MCBt.RIGHT
            case _:
                raise e.InvalidParamError(f'The first argument of mouse command line "{line}" '
                                          f'must be one of "L", "M", "R".')
    except IndexError as exc:
        raise e.InvalidParamError(f'The mouse command line "{line}" has no arguments.')\
              from exc
