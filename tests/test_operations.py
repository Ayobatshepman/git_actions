from src.operators import add, sub

def test_add():
    assert add(1,1) == 2
    assert add(2,2) == 4


def test_sub():
    assert sub(1,4) == -3
    assert sub(2,2) == 0