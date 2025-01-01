# 如何编写SpeeKlik脚本

> 本条目将指导你编写SpeeKlik脚本的操作。你可以将编写好的脚本导入到SpeeKlik中运行，或是将它发送给别人。

> [警告]!运行脚本前应该确保这个脚本没有恶意。我们不承担有不仔细阅读此条目引发的所有责任。!

## 主要外观

SpeeKlik脚本看起来如下所示：

```
@|default_delay=0.05|failsafe=True|
K|0|delay=0|
M|L|
M|L|
```

## 预定义

预定义是以`@`开头的行。这类行的格式如下：（使用`regex`）

```
@|((\S)+=(\S+)|)+
```

使用人类友好文字，表达如下：

```
@|多个(变量名(字符)=变量值)
```

参考“主要外观”中的例子，`default_delay`与`forever`分别是“变量名”，而`0.05`与`True`分别是变量的值。

在SpeeKlik中，可用的变量值有：

- `default_delay`指定了默认的间隔。此选项会在命令没有指定`delay`时使用。若没有指定，命令也没有指定`delay`，则SpeeKlik会报错。
- `safe_delay`指定了安全间隔。这个选项会覆盖`pyautogui.PAUSE`，详细信息可以在[pyautogui的文档](https://pyautogui.readthedocs.io/en/latest/index.html?highlight=failsafe#fail-safes)中找到。
- `failsafe`指定`pyautogui.FAILSAFE`的值。详细信息同样参考上面的链接。

## 命令

命令是如如下定义的行：

```
[KM]|(\S+)
```
