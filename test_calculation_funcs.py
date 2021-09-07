import pytest
from calculation import add, subtract, multiply, divide


@pytest.mark.number
def test_add_func():
    assert add(7, 3) == 10
    assert add(7) == 9
    assert add(5) > 6


@pytest.mark.number
def test_multiply_func():
    assert multiply(5, 5) == 25
    assert multiply(5) == 10
    assert multiply(7) < 15


@pytest.mark.string
def test_add_strings_func():
    result = add("Hello", " World")
    assert result == "Hello World"
    assert type(result) is str
    assert "xas" not in result


@pytest.mark.string
def test_multiply_strings_func():
    assert multiply("Hello ", 3) == "Hello Hello Hello "
    result = multiply("Hello ")
    assert result == "Hello Hello "
    assert type(result) is str
    assert "Hello" in result


@pytest.mark.parametrize(
    "num1,num2,result",
    [(7, 3, 10), ("Hello", " World", "Hello World"), (10.5, 25.5, 36)],
)
def test_parametrize_add_func(num1, num2, result):
    assert add(num1, num2) == result
