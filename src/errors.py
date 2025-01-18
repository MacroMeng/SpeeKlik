"""定义SpeeKlik会抛出的异常"""


class SpeeKlikError(Exception):
    """SpeeKlik的所有错误的基类"""
    pass


class InvalidScriptError(SpeeKlikError):
    """当脚本无效时抛出的错误"""
    pass


class LineBeginError(InvalidScriptError):
    """当脚本的某一行以无效字符开头时抛出的错误"""
    pass


class InvalidKeyError(InvalidScriptError):
    """当脚本的某一行包含无效的按键时抛出的错误"""
    pass


class InvalidMouseError(InvalidScriptError):
    """当脚本的某一行包含无效的鼠标点击时抛出的错误"""
    pass


class InvalidParamError(InvalidScriptError):
    """当脚本的某一行包含无效的参数时抛出的错误"""
    pass


class InvalidDelayError(InvalidParamError):
    """当脚本的某一行包含无效的延迟时抛出的错误"""
    pass


class InvalidClickPosError(InvalidParamError):
    """当脚本的某一行包含无效的鼠标点击位置时抛出的错误"""
    pass


class InvalidMouseCLickType(InvalidParamError):
    """当脚本的某一行包含无效的鼠标点击类型时抛出的错误"""
    pass
