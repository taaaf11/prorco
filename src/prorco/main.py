import sys
from argparse import ArgumentParser

from prorco.functions import get_factors, is_prime
from prorco.utils import parse_input, show_info


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
    parser.add_argument("-f", type=int, help="Show prime factors of the number.")

    args = parser.parse_args()

    if args.n:
        number = args.n
        show_info(is_prime(number))
    if args.f:
        number = args.f
        factors = get_factors(number)
        factors = [str(_) for _ in factors]
        print(f"The prime factors of given number are: {', '.join(factors)}")
