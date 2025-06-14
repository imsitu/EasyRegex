# EasyRegex

EasyRegex is a tiny helper that converts simple English phrases into
Python regular expressions using the `regex` module. It is not a full
natural language parser but handles a useful subset of common patterns.

```python
from easyregex import EasyRegex

er = EasyRegex()
pattern = er.compile("start of string one or more digits end of string")
print(bool(pattern.fullmatch("123")))  # True
```

Unknown words are treated literally so phrases can mix literals with the
provided keywords.
