# Py-Typewriter

[![PyPI version](https://badge.fury.io/py/py-typewriter.svg)](https://badge.fury.io/py/py-typewriter)

一个简单、灵活的 Python 库，用于在终端模拟自然的打字机输出效果。

## 特点

- **简单易用**: 只需一行代码即可实现打字机效果。
- **自然模拟**: 通过随机延迟和标点停顿，效果更逼真。
- **高度灵活**: 提供底层生成器，允许你完全自定义输出行为。
- **零依赖**: 无需安装任何第三方库。

## 安装

```bash
pip install py-typewriter
```

## 使用方法

### 快速上手

最简单的方式是使用 `typewrite()` 函数：

```python
import typewriter

story = "很久很久以前，在一个遥远的国度里...\n一切都显得那么宁静。"
typewriter.typewrite(story)
```

### 高级用法 (使用生成器)

如果你需要更多控制权（例如，将输出写入文件或GUI窗口），可以使用 `generate_typewriter_flow()` 生成器：

```python
import time
import typewriter

text = "这是一个更高级的用法。"

# 1. 创建生成器
flow = typewriter.generate_typewriter_flow(text, base_delay=0.1)

# 2. 自定义消费逻辑
for char, delay in flow:
    print(char, end='')
    # 在这里你可以做任何事，比如更新GUI...
    time.sleep(delay)
print() # 最后换行
```

## 贡献

欢迎提交 Issues 和 Pull Requests！

## 许可证

本项目使用 [MIT License](LICENSE)。


#### 4. 许可证 (`LICENSE`)



```text
# LICENSE

MIT License

Copyright (c) 2025 orxvan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```