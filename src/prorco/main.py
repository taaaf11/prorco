import sys
from argparse import ArgumentParser

from prorco.functions import get_factors, get_prime_factors, is_prime
from prorco.utils import parse_input, show_info
from prorco.type import InfoType


def cli():
    number = input("Enter a number. ")
    number = parse_input(number)

    show_info(is_prime(number))


def main():
    if len(sys.argv) == 1:
        cli()
        exit(0)

    parser = ArgumentParser(
        prog="prorco",
        description="A tool to tell whether given number is prime or composite.",
    )

    parser.add_argument("-n", type=int, help="The number to check.")
    parser.add_argument("-f", type=int, help="Show factors of the number.")
    parser.add_argument("-pf", type=int, help="Show prime factors of the number.")

    args = parser.parse_args()

    if args.n:
        number = args.n
        show_info(InfoType.IS_PRIME, is_prime(number))
    if args.f:
        number = args.f
        factors: list[int] = get_factors(number)
        show_info(InfoType.FACTORS, factors)
    if args.pf:
        number = args.pf
        pfactors: list[int] = get_prime_factors(number)
        show_info(InfoType.FACTORS, pfactors)
