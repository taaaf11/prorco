from enum import Enum


class InfoType(Enum):
    IS_PRIME = 1
    FACTORS = 2
    PFACTORS = 3


class NumberType(Enum):
    PRIME = 1
    COMP = 2
    NONE = 3  # solely for 1
