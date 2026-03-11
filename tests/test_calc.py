# Parameterization

import pytest
from src.calculator import Calculator

@pytest.mark.parametrize("num1, num2, exp_result", [(50, 20, 30), (50, 40, 10), (-50, 20, -70)])
def test_difference(num1, num2, exp_result):
    calci = Calculator(num1, num2)
    result = calci.calc_diff()
    assert result == exp_result
