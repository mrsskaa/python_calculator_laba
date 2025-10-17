import pytest
from src.calculator_E3 import calculate
from src.errrors import ExtraneousError, EmptyError, JointOperandsError, BadInputError, BadDigit, NotDigitError


def test_cool():
    assert calculate('2+2') == 4.0
    assert calculate('6.5-1.3') == 5.2
    assert calculate('1.2*1,2') == 1.44
    assert calculate('2/2') == 1.0
    assert calculate('-5/-2') == 2.5
    assert calculate('3//2') == 1.0
    assert calculate('3%2') == 1.0
    assert calculate(' 2            + 2 - 5// 2 * 3       % 8 /3') == 2.0
    assert calculate('-2+2') == 0.0
    assert calculate('20/5%3+5/4') == 2.25
    assert calculate('+5//2+4%8/5+-8') == -5.2
    assert calculate('-5.2+3//8%10') == -5.2
    assert calculate('2*2*2/2//2%2') == 0.0

def test_errors():
    with pytest.raises(ZeroDivisionError):
        calculate('1/0')

    with pytest.raises(ExtraneousError):
        calculate('tralaleylotralala')

    with pytest.raises(EmptyError):
        calculate('')

    with pytest.raises(JointOperandsError):
        calculate('1**2')

    with pytest.raises(BadInputError):
        calculate('2+2+')

    with pytest.raises(NotDigitError):
        calculate('10.+2')

    with pytest.raises(BadDigit):
        calculate('1.5//1.5')