def prime_factors(number: int) -> list[int]:
    """Returns a list of prime factors of a number."""

    pf = [1, number]
    for n in range(2, number):
        if number % n == 0:
            pf.append(n)
    return pf


def is_prime(number: int) -> bool:
    """Returns whether given number is prime."""

    is_n_prime: bool

    match number:
        case 1:
            is_n_prime = False
        case 2:
            is_n_prime = True
        case _:
            pf: list[int] = prime_factors(number)
            is_n_prime = len(pf) == 2

    return is_n_prime
