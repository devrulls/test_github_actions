import pytest
from main import add, divide, multiplication


def test_add_two_numbers():
    assert add(5, 10) == 15


def test_divide_two_numbers():
    assert divide(30, 3) == 10


def test_multiplication_two_numbers():
    assert multiplication(30, 0) == 0


def test_add_two_none():
    with pytest.raises(TypeError):
        add(None, None)
