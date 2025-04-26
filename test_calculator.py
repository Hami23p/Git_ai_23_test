import pytest

# Parameterized test for the add function
@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 8),
    (-1, 1, 0),
    (-1, -1, -2),
    (0, 0, 0)
])
def test_add_parameterized(calculator, a, b, expected):
    assert calculator.add(a, b) == expected

# Parameterized test for the subtract function
@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (1, 5, -4),
    (-5, -3, -2),
    (0, 0, 0)
])
def test_subtract_parameterized(calculator, a, b, expected):
    assert calculator.subtract(a, b) == expected

# Parameterized test for the multiply function
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-2, 3, -6),
    (0, 5, 0),
    (2.5, 3.5, 8.75),
    (-2.5, 4.0, -10.0)
])
def test_multiply_parameterized(calculator, a, b, expected):
    assert calculator.multiply(a, b) == expected

# Parameterized test for the divide function
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (5, 2, 2.5),
    (7, 4, 1.75),
])
def test_divide_parameterized(calculator, a, b, expected):
    assert calculator.divide(a, b) == expected

# Separate test for division by zero
def test_divide_by_zero(calculator):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(10, 0)

# Parameterized test for the power function
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 8),        # Positive exponent
    (3, 2, 9),        # Positive exponent
    (2, 0, 1),        # Exponent of zero
    (2, -2, 0.25),    # Negative exponent: 1/(2^2) = 0.25
    (10, -1, 0.1)     # Negative exponent: 1/10 = 0.1
])
def test_power_parameterized(calculator, a, b, expected):
    assert calculator.power(a, b) == pytest.approx(expected)

# Factorial function test
@pytest.mark.parametrize("n, expected", [
    (0, 1),         
    (1, 1),         
    (5, 120),       
    (10, 3628800), 
    (-1, "ValueError"),  
    (-10, "ValueError"), 
])
def test_factorial_parameterized(calculator, n, expected):
    if expected == "ValueError":
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
            calculator.factorial(n)
    else:
        assert calculator.factorial(n) == expected

# Fibonacci function test
@pytest.mark.parametrize("n, expected", [
    (0, 0),         
    (1, 1),         
    (2, 1),      
    (5, 5),         
    (10, 55),       
    (-1, "ValueError"),  
    (-10, "ValueError"), 
])
def test_fibonacci_parameterized(calculator, n, expected):
    if expected == "ValueError":
        with pytest.raises(ValueError, match="Fibonacci is not defined for negative numbers"):
            calculator.fibonacci(n)
    else:
        assert calculator.fibonacci(n) == expected

# Precise addition test with a fixed precision level
@pytest.mark.parametrize("a, b, expected", [
    (2.12345, 3.67891, {1: 5.8, 2: 5.80, 3: 5.802, 4: 5.8024}),
    (1.555, 2.555, {1: 4.1, 2: 4.11, 3: 4.110, 4: 4.1100}),
    (10.1, 0.33333, {1: 10.4, 2: 10.43, 3: 10.433, 4: 10.4333}),
])
def test_precise_add(precise_calculator, a, b, expected):
    precision = precise_calculator.precision 
    assert precise_calculator.add(a, b) == pytest.approx(expected[precision])


# Precise rounding tests for different precision levels
@pytest.mark.parametrize("a, b, expected", [
    (2.12345, 3.67891, {1: 5.8, 2: 5.80, 3: 5.802, 4: 5.8024}),
    (10.5555, 2.2222, {1: 12.8, 2: 12.78, 3: 12.778, 4: 12.7777}),
])
def test_precise_rounding(precise_calculator, a, b, expected):
    precision = precise_calculator.precision  # Get precision level from the fixture
    assert precise_calculator.add(a, b) == pytest.approx(expected[precision])
