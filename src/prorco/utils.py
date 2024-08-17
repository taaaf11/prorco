import sys
from typing import Any

from prorco.functions import is_prime
from prorco.type import InfoType


def parse_input(input_: str) -> int:
    """Parse input and do related things."""

    if not input_.isdigit():
        print("That doesn't seem a valid number.")
        sys.exit(1)
    else:
        return int(input_)


def show_info(info_type: InfoType, info: Any) -> None:
    """Print info to the screen."""

    match info_type:
        case InfoType.IS_PRIME:
            # info is int here
            info: int
            if info == 1:
                print("Neither prime nor composite!")
                sys.exit(0)
            if is_prime(info):
                print("The number is prime.")
            else:
                print("The number is composite.")
        case InfoType.FACTORS:  # for both prime and compositefactors
            # info is list[int] here
            info: list[int]
            factors = list(map(str, info))
            print(", ".join(factors))
