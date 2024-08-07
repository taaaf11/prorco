from prorco.functions import get_factors, is_prime


def test_get_factors():
    number = 20

    test_data = get_factors(number)
    accurate_data = [1, 2, 4, 5, 10, 20]

    assert test_data == accurate_data


def test_is_prime():
    number = 1
    assert is_prime(number) == False

    number = 2
    assert is_prime(number) == True

    number = 4
    assert is_prime(number) == False

    number = 5
    assert is_prime(number) == True
