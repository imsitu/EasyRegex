# EasyRegex

EasyRegex allows you to describe regular expressions using short English
phrases. The library translates those phrases into patterns from the
[regex](https://pypi.org/project/regex/) module and gives you a familiar
interface for compiling and matching strings.

## Installation

Install the package from PyPI:

```bash
pip install easyregex
```

## Usage

```python
from easyregex import EasyRegex

# Create the helper
er = EasyRegex()

# Build a regex pattern from an English description
pattern = er.compile("start of string one or more digits end of string")

# Use the compiled pattern just like a normal regex.Pattern
print(bool(pattern.fullmatch("123")))  # True
```

Words that are not recognised as keywords are treated literally, so you
can freely mix plain text with the provided tokens.

## Development

This project uses a basic `setup.py` and can be built with standard
Python packaging tools. The only runtime dependency is the `regex`
package.
