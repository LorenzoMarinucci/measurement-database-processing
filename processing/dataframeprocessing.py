from datetime import datetime, timedelta
from typing import Optional

import pandas as pd

from processing.constants.datasetConstants import DatasetColumns, DefaultValues
from processing.constants.filesConstants import FilesConstants
from processing.describe import describe_dataframe
from processing.plots import plot_timeseries, plot_boxes, plot_correlations, plot_beyond_sdvs
from processing.save import saveData


def process_dataset(
        filename: str,
        hour_start: Optional[str],
        hour_end: Optional[str],
        day_start: Optional[str],
        day_end: Optional[str],
        sdv: Optional[int]
) -> None:
    # Load the pandas dataframe
    df = pd.read_csv(
        FilesConstants.DATASET_BASE_DIRECTORY.value + '/' + filename
    ).astype(float).dropna()

    # Append column with formatted python date (more info about conversion can be found in readme file)
    df[DatasetColumns.DATETIME.value] = df[DatasetColumns.DATENUM.value].apply(
        lambda matlab_datenum:
        pd.to_datetime(
            datetime.fromordinal(
                int(matlab_datenum)) + timedelta(days=matlab_datenum % 1) - timedelta(days=366)
        )
    )

    # Set datetime column as index, improves filtering.
    df = df.set_index(DatasetColumns.DATETIME.value)

    # Set default values
    day_start = day_start if (day_start is not None) else pd.Timestamp.min
    day_end = day_end if (day_end is not None) else pd.Timestamp.max
    hour_start = hour_start if (
            hour_start is not None
    ) else DefaultValues.MIN_HOURS.value
    hour_end = hour_end if (
            hour_end is not None
    ) else DefaultValues.MAX_HOURS.value
    sdv = sdv if (sdv is not None) else 3

    # Filter dataframe by days and time.
    filtered_df = df.loc[day_start:day_end].between_time(hour_start, hour_end)

    # Dataframe info
    description = describe_dataframe(filtered_df)
    print(description)

    # Plots
    plot_timeseries(filtered_df)
    plot_boxes(filtered_df)
    plot_correlations(filtered_df)
    plot_beyond_sdvs(filtered_df, sdv)

    # Save data
    saveData(filtered_df, description)

