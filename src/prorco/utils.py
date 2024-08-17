from typing import Any

from prorco.functions import is_prime
from prorco.type import InfoType


def parse_input(input_: str) -> int:
    """Parse input and do related things."""

    try:
        int(input_)
    except ValueError:
        print("Please type a valid integer.")
        exit(1)
    else:
        return int(input_)


def show_info(info_type: InfoType, info: Any) -> None:
    """Print info to the screen."""

    match info_type:
        case InfoType.IS_PRIME:
            # info is int here
            info: int
            if is_prime(info):
                print("The number is prime.")
            else:
                print("The number is composite.")
        case InfoType.FACTORS:  # for both prime and compositefactors
            # info is list[int] here
            info: list[int]
            factors = list(map(str, info))
            print(", ".join(factors))
