import pytest
from typing import Any, Dict, List, NamedTuple, Optional, Tuple, TypedDict, Union
from toyval import validate
from dataclasses import dataclass


def test_validate_1():
    assert validate(1, int)
    assert validate(1.0, float)
    assert validate(0.1, float)
    assert validate("hoge", str)
    assert validate([1, 2, 3], list)
    assert validate({"a": 1, 10: "b"}, dict)
    assert validate((1, "a", None), tuple)
    assert validate(True, bool)
    assert validate(False, bool)
    assert validate(None, None)
    assert validate(None, type(None))

def test_validate_2():
    assert not validate(1.0, int)
    assert not validate("a", int)
    assert not validate([1, 2, 3], int)
    assert not validate(["a","b","c"], int)
    assert not validate({"a": 1, 10: "b"}, int)
    assert not validate((1, "a", None), int)
    assert not validate(None, int)

    assert not validate(1, float)
    assert not validate("a", float)
    assert not validate([1, 2, 3], float)
    assert not validate(["a","b","c"], float)
    assert not validate((1, "a", None), float)
    assert not validate(True, float)
    assert not validate(None, float)

    assert not validate(1, str)
    assert not validate(0.1, str)
    assert not validate([1, 2, 3], str)
    assert not validate({"a": 1, 10: "b"}, str)
    assert not validate((1, "a", None), str)
    assert not validate(True, str)
    assert not validate(None, str)

    assert not validate(1, list)
    assert not validate(0.1, list)
    assert not validate("hoge", list)
    assert not validate({"a": 1, 10: "b"}, list)
    assert not validate((1, "a", None), list)
    assert not validate(True, list)
    assert not validate(None, list)

    assert not validate(1, dict)
    assert not validate(0.1, dict)
    assert not validate("hoge", dict)
    assert not validate([1, 2, 3], dict)
    assert not validate((1, "a", None), dict)
    assert not validate(True, dict)
    assert not validate(None, dict)

    assert not validate(1, tuple)
    assert not validate(0.1, tuple)
    assert not validate("hoge", tuple)
    assert not validate([1, 2, 3], tuple)
    assert not validate({"a": 1, 10: "b"}, tuple)
    assert not validate(True, tuple)
    assert not validate(None, tuple)

    assert not validate(1, bool)
    assert not validate(0.1, bool)
    assert not validate("hoge", bool)
    assert not validate([1, 2, 3], bool)
    assert not validate({"a": 1, 10: "b"}, bool)
    assert not validate((1, "a", None), bool)

    assert not validate(1, None)
    assert not validate(0.1, None)
    assert not validate("hoge", None)
    assert not validate([1, 2, 3], None)
    assert not validate({"a": 1, 10: "b"}, None)
    assert not validate(True, None)
    assert not validate((1, "a", None), None)

def test_validate_3():
    assert validate([1, "a", None], List)
    assert validate([1, "a", None], List[Any])
    assert validate([1, 2, 3], List[int])
    assert validate([1.0, 2.0, 3.0], List[float])
    assert validate(["a", "b", "c"], List[str])
    assert validate([[1, 2], [3], []], List[List[int]])
    assert validate([{"a": 1, 10: "b"}, {}], List[dict])
    assert validate([{"a": 1, "b": 2}, {}], List[Dict[str, int]])
    assert validate([None, None, None], List[None])

    assert not validate(1, List)
    assert not validate(1, List[Any])
    assert not validate(1, List[int])
    assert not validate(["a", "b", "c"], List[int])
    assert not validate([1, 2, 3], List[str])

def test_validate_4():
    assert validate({"a": 1, 10: "b"}, Dict)
    assert validate({"a": 1, 10: "b"}, Dict[Any, Any])
    assert validate({"a": 1, "b": 1}, Dict[str, int])
    assert validate({"a": 1, "b": 1}, Dict[Any, int])
    assert validate({"a": 1, "b": 1}, Dict[str, Any])
    assert validate({"a": [1, 2, 3], "b": [4, 5, 6]}, Dict[str, List[int]])

    assert not validate([1, 2, 3], Dict)
    assert not validate((1, 2, 3), Dict)
    assert not validate({"a": 1, 10: "b"}, Dict[str, int])
    assert not validate({"a": 1, 10: "b"}, Dict[Any, int])
    assert not validate({"a": 1, 10: "b"}, Dict[str, Any])
    assert not validate({"a": [1, 2, 3], "b": [3, 4, "5"]}, Dict[str, List[int]])

def test_validate_5():
    assert validate((1,), Tuple[int])
    assert validate((1, 2), Tuple[int, int])
    assert validate((1, 2, 3), Tuple[int, int, int])
    assert validate((1,), Tuple[int, ...])
    assert validate((1, 2), Tuple[int, ...])
    assert validate((1, 2, 3), Tuple[int, ...])
    assert validate((1, "a"), Tuple[int, str])
    assert validate([(1, "a"), (2, "b")], List[Tuple[int, str]])
    assert validate({"a": (1, 2), "b": (3, 4)}, Dict[str, Tuple[int, int]])

    assert not validate(("a",), Tuple[int])
    assert not validate(("a",), Tuple[int, ...])
    assert not validate((1,), Tuple[str])
    assert not validate((2,), Tuple[str, ...])
    assert not validate((1, 2), Tuple[int])
    assert not validate(("a", "b"), Tuple[str])
    assert not validate(("a", 1), Tuple[int, str])
    assert not validate([(1, "a"), (2, "b"), None], List[Tuple[int, str]])
    assert not validate([(1, "a"), (2, -1)], List[Tuple[int, str]])
    assert not validate({"a": (1, 2), "b": (3, 4, 5)}, Dict[str, Tuple[int, int]])

def test_validate_6():
    assert validate(None, Optional[int])
    assert validate(1, Optional[int])
    assert validate(None, Optional[str])
    assert validate("a", Optional[str])
    assert validate(None, Optional[List[int]])
    assert validate([1, 2, 3], Optional[List[int]])
    assert validate([1, 2, None], List[Optional[int]])
    assert validate({"a": 1, "b": None}, Dict[str, Optional[int]])

    assert not validate("a", Optional[int])
    assert not validate(1, Optional[str])
    assert not validate(1, Optional[List[int]])
    assert not validate("a", Optional[List[int]])
    assert not validate(["a", "b", "c"], Optional[List[int]])
    assert not validate(None, List[Optional[int]])
    assert not validate([1, 2, "a"], List[Optional[int]])
    assert not validate(None, Dict[str, Optional[int]])
    assert not validate({"a": 1, "b": "bbb"}, Dict[str, Optional[int]])

def test_validate_7():
    assert validate(1, Union[int, str])
    assert validate("a", Union[int, str])
    assert validate(None, Union[List[int], None])
    assert validate([1, 2, 3], Union[List[int], None])
    assert validate([1, 2, "a"], List[Union[int, str]])
    assert validate([1, 2, 3], List[Union[int, str]])
    assert validate(["a", "b", "c"], List[Union[int, str]])
    assert validate({"a": 1, "b": None}, Dict[str, Union[int, None]])

    assert not validate(None, Union[int, str])
    assert not validate((1, "a"), Union[int, str])
    assert not validate(["a", "b", "c"], Union[List[int]])
    assert not validate(None, List[Union[int]])
    assert not validate([1, 2, "a"], List[Union[int]])
    assert not validate(None, Dict[str, Union[int]])
    assert not validate({"a": 1, "b": "bbb"}, Dict[str, Union[int]])

def test_validate_9():
    class TestNT1(NamedTuple):
        x: int
        y: int

    class TestNT2(NamedTuple):
        name: str
        point: TestNT1

    assert validate(TestNT1(x=1, y=2), TestNT1)
    assert validate((1, 2), TestNT1)
    assert validate(TestNT2(name="a", point=TestNT1(x=1, y=2)), TestNT2)
    assert validate(TestNT2(name="a", point=(1, 2)), TestNT2)
    assert validate(("a", TestNT1(x=1, y=2)), TestNT2)
    assert validate(("a", (1, 2)), TestNT2)

    assert not validate(None, TestNT1)
    assert not validate(("a", 1), TestNT1)
    assert not validate(TestNT1(x=1, y="a"), TestNT1)
    assert not validate(TestNT2(name=1, point=TestNT1(x=1, y=2)), TestNT2)
    assert not validate(TestNT2(name="a", point=TestNT1(x=1, y="a")), TestNT2)

def test_validate_9():
    class TestTD1(TypedDict):
        x: int
        y: int

    class TestTD2(TypedDict):
        name: str
        point: TestTD1

    assert validate(TestTD1(x=1, y=2), TestTD1)
    assert validate(TestTD1({"x": 1, "y": 2}), TestTD1)
    assert validate({"x": 1, "y": 2}, TestTD1)
    assert validate(TestTD2({"name": "a", "point": TestTD1(x=1, y=2)}), TestTD2)
    assert validate(TestTD2({"name": "a", "point": {"x": 1, "y": 2}}), TestTD2)

    assert not validate(None, TestTD1)
    assert not validate({"x": 1, "y": "a"}, TestTD1)
    assert not validate(TestTD1({"x": 1, "y": "a"}), TestTD1)
    assert not validate(TestTD2({"name": 1, "point": TestTD1({"x": 1, "y": 2})}), TestTD2)
    assert not validate(TestTD2({"name": "a", "point": (1, 2)}), TestTD2)

def test_validate_10():
    @dataclass
    class TestDC1:
        x: int
        y: int

    @dataclass
    class TestDC2:
        name: str
        point: TestDC1

    assert validate(TestDC1(x=1, y=2), TestDC1)
    assert validate(TestDC2(name="a", point=TestDC1(x=1, y=2)), TestDC2)

    assert not validate(None, TestDC1)
    assert not validate((1, 2), TestDC1)
    assert not validate(TestDC1(x=1, y="a"), TestDC1)
    assert not validate(TestDC2(name=1, point=TestDC1(x=1, y=2)), TestDC2)
    assert not validate(TestDC2(name="a", point=(1, 2)), TestDC2)
