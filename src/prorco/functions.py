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
    pfactors = [factor for factor in factors if is_prime(factor)]
    return pfactors


def is_prime(number: int) -> bool:
    """Returns whether given number is prime."""

    is_n_prime: bool

    match number:
        case 1:
            is_n_prime = False
        case 2:
            is_n_prime = True
        case _:
            factors = get_factors(number)
            is_n_prime = len(factors) == 2

    return is_n_prime
