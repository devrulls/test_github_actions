import pytest
from main import add, divide, multiplication


def test_add_two_numbers():
    assert add(5, 12) == 17


def test_divide_two_numbers():
    assert divide(30, 3) == 10


def test_multiplication_two_numbers():
    assert multiplication(30, 10) == 300


def test_add_two_none():
    with pytest.raises(TypeError):
        add(None, None)
