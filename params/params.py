from enum import Enum


class ConsoleParams(Enum):
    FILENAME: str = "-f"
    DAY_START: str = "-ds"
    DAY_END: str = "-de"
    HOUR_START: str = "-hs"
    HOUR_END: str = "-he"
    STANDARD_DEVIATION: str = "-sd"
