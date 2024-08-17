from prorco.functions import get_factors, get_num_type, get_prime_factors
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


def test_get_num_type():
    number = 1
    assert get_num_type(number) == NumberType.NONE

    number = 2
    assert get_num_type(number) == NumberType.PRIME

    number = 4
    assert get_num_type(number) == NumberType.COMP

    number = 5
    assert get_num_type(number) == NumberType.PRIME
