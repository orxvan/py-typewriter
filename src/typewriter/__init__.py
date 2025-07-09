# src/typewriter/__init__.py

import random
import sys
import time
from collections.abc import Generator
from typing import Tuple

# 定义公共 API，当用户 `from typewriter import *` 时只会导入这些
__all__ = ["typewrite", "generate_typewriter_flow"]
__version__ = "0.1.0"  # 初始版本号


def generate_typewriter_flow(text: str, base_delay: float = 0.05) -> Generator[Tuple[str, float], None, None]:
    """
    生成一个模拟打字机效果的字符流。

    这个函数是一个生成器，它不直接打印或休眠。
    它会 yield (产出) 一个元组，包含 (下一个字符, 建议的延迟时间)。
    这为你提供了最大的灵活性，可以自定义如何“消费”这个字符流。

    :param text: 要处理的文本。
    :param base_delay: 基础延迟时间（秒）。一个字符的平均延迟时间。
    :return: 一个产出 (字符, 延迟时间) 的生成器。

    用法:
        >>> flow = generate_typewriter_flow("Hello!")
        >>> for char, delay in flow:
        ...     print(char, end='')
        ...     time.sleep(delay)
    """
    for char in text:
        # 如果是标点符号，停顿时间更长，模拟思考或换气
        if char in [",", "，", ".", "。", "!", "！", "?", "？", "…"]:
            delay = base_delay * 8
        else:
            # 增加随机性，使效果更自然
            delay = base_delay + random.uniform(-0.02, 0.02)
            # 确保延迟不会是负数
            delay = max(0.01, delay)

        yield char, delay


def typewrite(text: str, delay: float = 0.05, end: str = "\n") -> None:
    """
    以打字机效果直接在终端打印文本。

    这是一个高级、易于使用的函数，封装了生成和打印的整个过程。

    :param text: 要打印的文本。
    :param delay: 每个字符之间的平均延迟时间（秒）。
    :param end: 文本打印完毕后追加的字符，默认为换行符。

    用法:
        >>> typewrite("你好，世界！")
    """
    flow_generator = generate_typewriter_flow(text, base_delay=delay)

    for char, sleep_time in flow_generator:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(sleep_time)

    sys.stdout.write(end)
    sys.stdout.flush()
