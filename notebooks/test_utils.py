# test_utils.py

from utils import add, subtract

def test_addition():
    assert add(3, 5) == 8
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtraction():
    assert subtract(5, 3) == 2
    assert subtract(1, -1) == 2
    assert subtract(0, 0) == 0



