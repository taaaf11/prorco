from prorco.type import NumberType


def get_factors(number: int) -> list[int]:
    """Returns a list of factors of given number."""

    factors = [1, number]
    for n in range(2, number):
        if number % n == 0:
            factors.append(n)
    factors = sorted(factors)
    return factors


def get_prime_factors(number: int) -> list[int]:
    """Returns a list of prime factors of given number."""

    factors = get_factors(number)
    pfactors = []
    for factor in factors:
        if get_num_type(factor) == NumberType.PRIME:
            pfactors.append(factor)
    return pfactors


def get_num_type(number: int) -> NumberType:
    """Returns whether given number is prime, composite or none."""

    n_type: NumberType

    match number:
        case 1:
            n_type = NumberType.NONE
        case 2:
            n_type = NumberType.PRIME
        case _:
            factors = get_factors(number)
            n_type = NumberType.PRIME if len(factors) == 2 else NumberType.COMP
    return n_type
