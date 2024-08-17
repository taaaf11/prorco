from prorco.functions import get_factors, get_prime_factors, is_prime
from prorco.type import NumberType


def test_get_factors():
    number = 20

    test_data = get_factors(number)
    accurate_data = [1, 2, 4, 5, 10, 20]

    assert test_data == accurate_data


def test_get_prime_factors():
    number = 20
    
    test_data = get_prime_factors(number)
    accurate_data = [2, 5]

    assert test_data == accurate_data


def test_is_prime():
    number = 1
    assert is_prime(number) == NumberType.NONE

    number = 2
    assert is_prime(number) == NumberType.PRIME

    number = 4
    assert is_prime(number) == NumberType.COMP

    number = 5
    assert is_prime(number) == NumberType.PRIME
