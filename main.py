import sys

from params.params import ConsoleParams
from processing.dataframeprocessing import process_dataset


def main() -> None:
    filename = _get_filename()
    day_start, day_end = _get_day_start_and_end()
    hour_start, hour_end = _get_hour_start_and_end()
    sdv = _get_standard_deviation()

    process_dataset(filename, hour_start, hour_end, day_start, day_end, sdv)


def _get_filename() -> str:
    try:
        filename_index = sys.argv.index(ConsoleParams.FILENAME.value)
        return sys.argv[filename_index + 1]
    except ValueError:
        raise Exception("Filename param is mandatory.") from None


def _get_day_start_and_end() -> tuple[str | None, str | None]:
    try:
        day_start_index = sys.argv.index(ConsoleParams.DAY_START.value)
        day_start = sys.argv[day_start_index + 1]
    except ValueError:
        day_start = None

    try:
        day_end_index = sys.argv.index(ConsoleParams.DAY_END.value)
        day_end = sys.argv[day_end_index + 1]
    except ValueError:
        day_end = None

    return day_start, day_end


def _get_hour_start_and_end() -> tuple[str | None, str | None]:
    try:
        hour_start_index = sys.argv.index(ConsoleParams.HOUR_START.value)
        hour_start = sys.argv[hour_start_index + 1]
    except ValueError:
        hour_start = None

    try:
        hour_end_index = sys.argv.index(ConsoleParams.HOUR_END.value)
        hour_end = sys.argv[hour_end_index + 1]
    except ValueError:
        hour_end = None

    return hour_start, hour_end


def _get_standard_deviation() -> int | None:
    try:
        sdv_index = sys.argv.index(ConsoleParams.STANDARD_DEVIATION.value)
        sdv = int(sys.argv[sdv_index + 1])
    except ValueError:
        sdv = None

    return sdv


if __name__ == '__main__':
    main()
