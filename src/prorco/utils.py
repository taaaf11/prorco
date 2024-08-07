def parse_input(input_: str) -> int:
    """Parse input and do related things."""

    try:
        int(input_)
    except ValueError:
        print("Please type a valid integer.")
        exit(1)
    else:
        return int(input_)


def show_info(is_prime: bool) -> None:
    """Print info about the number to the screen."""

    if is_prime:
        print("The number is prime.")
    else:
        print("The number is composite.")
