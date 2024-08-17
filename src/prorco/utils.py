import sys
from typing import Any

from prorco.functions import get_factors, get_num_type, get_prime_factors
from prorco.type import InfoType, NumberType


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
            n_type: NumberType = get_num_type(info)
            match n_type:
                case NumberType.PRIME:
                    print("The number is prime.")
                case NumberType.COMP:
                    print("The number is composite.")
                case NumberType.NONE:
                    print("The number is neither prime nor composite.")
        case InfoType.FACTORS:
            # info is int here
            info: int
            factors: list[int] = get_factors(info)
            factors = list(map(str, factors))
            print(", ".join(factors))
        case InfoType.PFACTORS:
            # info is int here
            info: int
            pfactors: list[int] = get_prime_factors(info)
            pfactors = list(map(str, pfactors))
            print(", ".join(pfactors))
