from src.math_operation import add, subtract


def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0  