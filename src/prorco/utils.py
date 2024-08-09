from typing import Any

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
            if is_prime:
                print("The number is prime.")
            else:
                print("The number is composite.")
        case InfoType.FACTORS:
            # info would be a list[int] here
            info = [str(_) for _ in info]
            print(", ".join(info))
