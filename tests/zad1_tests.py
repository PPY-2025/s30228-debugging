from main import factorial

def test_factorial_zero():
    assert factorial(0) is 1

def test_factorial_three():
    assert factorial(3) is 6

def test_factorial_five():
    assert factorial(5) is 120