import sys
from argparse import ArgumentParser

from prorco.utils import parse_input, show_info
from prorco.type import InfoType


def cli():
    number = input("Enter a number. ")
    number = parse_input(number)

    show_info(InfoType.IS_PRIME, number)


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
        show_info(InfoType.IS_PRIME, number)
    if args.f:
        number = args.f
        show_info(InfoType.FACTORS, number)
    if args.pf:
        number = args.pf
        show_info(InfoType.PFACTORS, number)
