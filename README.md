# Py-Typewriter-SSE

[![PyPI version](https://badge.fury.io/py/py-typewriter-sse.svg)](https://badge.fury.io/py/py-typewriter-sse)

[**English**](./README.md) | [**中文**](README_cn.md)

---

<div id="py-typewriter-sse-en"></div>

A simple and flexible Python library for simulating a natural typewriter effect in the terminal.

## Features

- **Easy to Use**: Achieve a typewriter effect with just a single line of code.
- **Natural Simulation**: More realistic effects through random delays and punctuation pauses.
- **Highly Flexible**: Provides a low-level generator, allowing you to fully customize the output behavior.

## Installation

```bash
pip install py-typewriter-sse
```

## Usage

### Quick Start

The easiest way is to use the `typewrite()` function:

```python
import typewriter

story = "Once upon a time, in a kingdom far, far away...\neverything was so peaceful."
typewriter.typewrite(story)
```

### Advanced Usage (Using the Generator)

For more flexible control, you can use the `generate_typewriter_flow()` generator:

```python
import time
import typewriter

text = "This is a more advanced usage."

flow = typewriter.generate_typewriter_flow(text, base_delay=0.1)

for char, delay in flow:
    print(char, end='', flush=True)
    time.sleep(delay)
print()
```
### Supports 'char' (Default) and 'word' modes. The 'word' mode supports Chinese word segmentation for a more realistic effect.
```python
    text_sample_cn = "你好，世界！这是一个基于Jieba分词的打字机效果模拟。它能让中文输出更自然、流畅。"
    text_sample_en = "Hello, world! This is a typewriter effect simulation."

    print("--- Mode: 'char' (Default character mode) ---")
    flow_char = typewriter.generate_typewriter_flow(text_sample_cn, base_delay=0.03)
    for char, delay in flow_char:
        print(char, end="", flush=True)  # flush=True ensures immediate output
        time.sleep(delay)
    print("\n")  # Newline

    print("--- Mode: 'word' (Jieba word segmentation) Fast (multiple words combined, suitable for long text) ---")
    try:
        flow_word = typewriter.generate_typewriter_flow(text_sample_cn, base_delay=0.03, mode="word")
        for word, delay in flow_word:
            print(word, end="", flush=True)
            time.sleep(delay)
        print("\n")
    except ImportError as e:
        print(f"\nError: {e}")

    print("--- Mode: 'word' (Jieba word segmentation) Slow (word by word) ---")
    try:
        flow_word = typewriter.generate_typewriter_flow(
            text_sample_cn, base_delay=0.03, mode="word", max_chunk_size=1, min_chunk_size=1
        )
        for word, delay in flow_word:
            print(word, end="", flush=True)
            time.sleep(delay)
        print("\n")
    except ImportError as e:
        print(f"\nError: {e}")

    print("--- English text in 'word' mode ---")
    # Jieba also handles English and numbers well
    try:
        flow_en_word = typewriter.generate_typewriter_flow(text_sample_en, base_delay=0.03, mode="word")
        for word, delay in flow_en_word:
            print(word, end="", flush=True)
            time.sleep(delay)
        print("\n")
    except ImportError as e:
        print(f"\nError: {e}")
```

## Contributing

Issues and Pull Requests are welcome!

## License

This project is licensed under the [MIT License](LICENSE).


## License (`LICENSE`)



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