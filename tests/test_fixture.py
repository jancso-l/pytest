# Fixture

import pytest
import src.calculator

@pytest.fixture()
def create_fixture():
    calc = src.calculator.Calculator(10, 50)
    return calc

def test_addition(create_fixture):
    result = create_fixture.calc_add()
    assert result == 60

def test_difference(create_fixture):
    result = create_fixture.calc_diff()
    assert result == -40

def test_multiply(create_fixture):
    result = create_fixture.calc_prod()
    assert result == 500


if __name__ == "__main__":
    pytest.main()