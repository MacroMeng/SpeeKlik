import mouse_event as me
import errors as e
from mouse_event import MouseClickButtons as MCBt
import log


def solve_from_file(fn: str) -> me.MouseKeyEvents:
    """从文件中解析鼠标/键盘事件"""
    log.log.debug(f"开始解析{fn}")
    with open(fn, "r") as f:
        lines = f.readlines()
    events = me.MouseKeyEvents()
    for line in lines:
        match line[0].strip():
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
    """解析一行键盘命令，返回一个KeyClick对象"""
    log.log.debug(f"开始解析键盘命令行{line}")
    if line[:2] != "K|":
        log.log.error(f"错误的行起始: {line[:2]}应为“K|”")
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
                log.log.error(f"错误的键盘符号：{arg_key}")
                raise e.InvalidParamError(f'The first argument of key command Line "{line}" '
                                          f'must be a char or a hex number start with "U+".')
    except ValueError as exc:
        log.log.error(f"不能解析键盘符号：{args[0]}")
        raise e.InvalidParamError(f'The first argument of key command line "{line}" '
                                  f'is not a valid hex of Unicode. Read the documents '
                                  f'at .../SpeeKlik/doc/script_writing.md for more information.') \
            from exc
    except IndexError as exc:
        log.log.error(f"不能通过索引获取args（{args}）的值。")
        raise e.InvalidParamError(f'The key command line "{line}" has no arguments.') \
            from exc
    try:
        match args[1:]:
            case []:
                delay = 0.0
            case [str(delay_str)]:
                delay = float(delay_str[6:])
            case _:
                log.log.error(f"match-case没有捕捉到的值：{args[1:]}")
                raise e.InvalidParamError(f'The key command line "{line}" has too many/less arguments.')
    except ValueError as exc:
        log.log.error(f"不能解析延迟时间的args值：{args}")
        raise e.InvalidParamError(f'The second argument of key command line "{line}" '
                                  f'is not a valid float.') \
            from exc

    return me.KeyClick(key, delay)


def solve_mouse(line: str) -> me.MouseClick:
    """解析一行鼠标命令，返回一个MouseClick对象"""
    if line[:2] != "M|":
        raise e.LineBeginError(f"Invalid line: {line}")
    line = line[2:]
    args = line.split("|")
    try:
        match args[0]:
            case "L":
                button = MCBt.LEFT
            case "M":
                button = MCBt.MIDDLE
            case "R":
                button = MCBt.RIGHT
            case _:
                log.log.error(f"错误的鼠标键位：{args[0]}")
                raise e.InvalidParamError(f'The first argument of mouse command line "{line}" '
                                          f'must be one of "L", "M", "R".')
    except IndexError as exc:
        log.log.error(f"不能通过索引获取args（{args}）的值。")
        raise e.InvalidParamError(f'The mouse command line "{line}" has no arguments.') \
            from exc
    try:
        match args[1:]:
            case []:
                x = None
                y = None
                delay = None
            case [str(pos_str)] if "," in pos_str:
                x, y = eval(pos_str)
                if not isinstance(x, int) and isinstance(y, int):
                    log.log.error(f"不能解析的鼠标坐标：{args[1:]}")
                    raise e.InvalidParamError(f'The second argument of mouse command line "{line}" '
                                              f'is not a valid position.')
                delay = None
            case [str(pos_str), str(delay_str)]:
                x, y = eval(pos_str)
                if not isinstance(x, int) and isinstance(y, int):
                    raise e.InvalidParamError(f'The second argument of mouse command line "{line}" '
                                              f'should be a valid position.')
                delay = float(delay_str[6:])
            case [str(delay_str)]:
                x = None
                y = None
                try:
                    delay = float(delay_str[6:])
                except ValueError as exc:
                    log.log.error(f"不能解析延迟时间：{args[1:]}")
                    raise e.InvalidParamError(f'The delay argument of mouse command line "{line}" '
                                              f'is not a valid float.') \
                        from exc
            case _:
                raise e.InvalidParamError(f'The mouse command line "{line}" has too many/less arguments.')
    except ValueError as exc:
        log.log.error(f"不能解析鼠标坐标或延迟时间的args值：{args}")
        raise e.InvalidParamError(f'The second argument of mouse command line "{line}" '
                                  f'is not a valid float.') \
            from exc

    return me.MouseClick(x, y, button, delay)


def solve_predef(line: str) -> me.Environment:
    """解析一行预定义字符串"""
    if line[:2] != "@|":
        raise e.LineBeginError(f"Invalid line: {line}")
    line = line[2:]
    args = line.split("|")
    definitions = {}
    for arg in args:
        try:
            k, v = arg.split("=")
            v = eval(v)
        except (SyntaxError, NameError) as exc:
            log.log.error(f"不能解析预定义键-值对：{arg}")
            raise e.InvalidParamError(f'The value of predefine command line "{line}" '
                                      f'is not a valid Python expression.') \
                from exc
        except ValueError as exc:
            log.log.error(f"未找到预定义键-值对：{arg}")
            raise e.InvalidParamError(f'The value of predefine command line "{line}" '
                                      f'is not a valid Python expression.') \
                from exc
        definitions[k] = v
    try:
        return me.Environment(**definitions)
    except ValueError as exc:
        log.log.error(f"预定义键-值对不符合要求：{definitions}")
        raise e.InvalidParamError(f'The predefine command line "{line}" '
                                  f'has invalid arguments.') \
            from exc
