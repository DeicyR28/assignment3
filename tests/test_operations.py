import pytest   
from app.operations import addition, division, multiplication, substraction
from typing import Union

Number = Union[int, float]

@pytest.mark.parametrize(
    "a, b, expected",
    [ 
        (2, 2, 4),
        (0, 0, 0),
        (-1, 1, 0 ),
        (2.5, 3.5, 6.0),
        (-2.5, 3.5, 1.0),
    ],
    ids= [ 
        "add_two_positive_integers",
        "add_two_zeros",
        "add_negative_and_positive_integer",
        "add_two_positive_floats",
        "add_negative_float_and_positive_float",
    ]
)
def test_addition(a: Number, b: Number, expected: Number) -> None:

    result = addition(a,b)

    assert result == expected, f"Expected addition({a}, {b}) to be expected{expected}, but got {result}" 

  
def test_substraction():
    assert substraction(1,1) == 0

def test_multiplication():
    assert multiplication(1,1) == 1

def test_division_positive():
    assert division(1,1) == 1

def test_division_by_zero():
    """Test division by zero."""
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        division(1, 0)
