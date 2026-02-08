import pytest   
from app.operations import operations
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

    result = operations.addition(a,b)

    assert result == expected, f"Expected addition({a}, {b}) to be expected{expected}, but got {result}" 


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),
        (0, 0, 0),
        (-5, -3, -2),
        (10.5, 5.5, 5.0),
        (-10.5, -5.5, -5.0),
    ],
    ids=[
        "substract_smaller_positive_integer_from_larger",
        "substract_two_zeros",
        "substract_negative_integer_from_negative_integer",
        "substract_two_positive_floats",
        "substract_two_negative_floats",
    ]
)
def test_substraction(a: Number, b: Number, expected: Number) -> None:

    result = operations.substraction(a, b)
    assert result == expected, f"Expected substraction({a}, {b}) to be {expected}, but got {result}"



@pytest.mark.parametrize(
    "a, b, expected",    
    [
        (6, 3, 2.0),
        (-6, -3, 2.0),
        (6.0, 3.0, 2.0),
        (-6.0, 3.0, -2.0),
        (0, 5, 0.0),

    ],
        ids=[
        "divide_two_positive_integers",
        "divide_two_negative_integers",
        "divide_two_positive_floats",
        "divide_negative_float_by_positive_float",
        "divide_zero_by_positive_integer",
    ]
)
def test_division(a: Number, b: Number, expected: float) -> None: 
    result = operations.division (a, b)
    assert result == expected, f"expected division {a}, {b} to be {expected}, but got {result}"

@pytest.mark.parametrize(
    "a, b, expected", 
    [ 
        (6, 3, 2.0),
        (-6,-3, 2.0),
        (6.0, 3.0, 2.0),
        (-6.0, 3.0,-2.0),
        (0, 5, 0.0),
],
ids=[
    "divide_two_positive_integers",
    "divide_two_negative_integers",
    "divide_two_positive_floats",
    "divide_negative_float_by_positive_float",
    "divide_zero_by_positive_integer",
]
)
def test_division_positive(a: Number, b: Number, expected: float) -> None:
    result = operations.division(a, b)
    assert result == expected, f"Expected division{a}, {b} to be {expected}, but got {result}"


@pytest.mark.parametrize(
   "a, b",
    [ 
        (1,0),
        (-1,0),
        (0,0),
    ],
    ids=[ 
        "divide_positive_dividend_by_zero",
        "divide_negative_dividend_by_zero",
        "divide_zero_by_zero",
    ]     
)
def test_division_by_zero(a: Number, b: Number) -> None:

    with pytest.raises(ValueError, match="Division by zero is not allowed.") as excinfo:
        operations.division(a, b)
    
    assert "Division by zero is not allowed." in str(excinfo.value), \
        f"Expected error message 'Division by zero is not allowed.', but got '{excinfo.value}'"
