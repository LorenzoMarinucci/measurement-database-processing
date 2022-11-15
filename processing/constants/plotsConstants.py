from enum import Enum
from typing import List


class PlotsConstants(Enum):
    TICKS_PER_PLOT: int = 30
    TICKS_ROTATION: int = 90
    HOUR_RANGE: List[int] = range(8, 19)  # from 8am to 18pm
