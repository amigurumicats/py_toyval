# py_toyval

## requirements
python >= 3.8

## example
```
from toyval import validate

validate(1, int)  # => True
validate("hoge", str)  # => True
validate([1, 2, 3], list)  # => True
validate({"a": 1, 10: "b"}, dict)  # => True
validate((1, "a", None), tuple)  # => True
validate(True, bool)  # => True
validate(None, None)  # => True

validate(1, bool)  # => False
validate(None, str)  # => False
```

```
from typing import List, Dict, Tuple
from toyval import validate

validate([1, 2, 3], List[int])  # => True
validate([1, 2, 3], List[str])  # => False
validate({"a": 1, "b": 2}, Dict[str, int])  # => True
validate({"a": 1, "b": 2}, Dict[int, str])  # => False
validate((1, "a"), Tuple[int, str])  # => True
validate((1, "a"), Tuple[int, ...])  # => False
```

```
from typing import NamedTuple
from toyval import validate

class Point(NamedTuple):
    x: int
    y: int

validate(Point(x=1, y=2), Point)  # => True
validate((1, "a"), Point)  # => False
```
