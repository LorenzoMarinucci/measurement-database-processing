import numpy as np
from matplotlib import pyplot as plt
from pandas import DataFrame
from scipy import stats

from processing.constants.dataset import DatasetColumns


# Plot each measurement evolution
def plot_timeseries(df: DataFrame) -> None:
    pass
    _plot_measurement(df, DatasetColumns.G_POA.value)
    _plot_measurement(df, DatasetColumns.AIR_TEMP.value)
    _plot_measurement(df, DatasetColumns.WIND_SPEED.value)
    _plot_measurement(df, DatasetColumns.HUMIDITY.value)
    _plot_measurement(df, DatasetColumns.DECLINATION.value)
    _plot_measurement(df, DatasetColumns.POWER.value)

    _plot_day_averages(df)
    _plot_hourly_averages(df)


def _plot_day_averages(df: DataFrame):
    pass
    day = df.groupby([df.index.year, df.index.month, df.index.day]).mean()

    _plot_aggregate(day, DatasetColumns.G_POA.value, 'daily')
    _plot_aggregate(day, DatasetColumns.AIR_TEMP.value, 'daily')
    _plot_aggregate(day, DatasetColumns.WIND_SPEED.value, 'daily')
    _plot_aggregate(day, DatasetColumns.HUMIDITY.value, 'daily')
    _plot_aggregate(day, DatasetColumns.DECLINATION.value, 'daily')
    _plot_aggregate(day, DatasetColumns.POWER.value, 'daily')


def _plot_hourly_averages(df: DataFrame) -> None:
    pass
    hour = df.groupby([df.index.year, df.index.month,
                      df.index.day, df.index.hour]).mean()

    _plot_aggregate(hour, DatasetColumns.G_POA.value, 'hourly')
    _plot_aggregate(hour, DatasetColumns.AIR_TEMP.value, 'hourly')
    _plot_aggregate(hour, DatasetColumns.WIND_SPEED.value, 'hourly')
    _plot_aggregate(hour, DatasetColumns.HUMIDITY.value, 'hourly')
    _plot_aggregate(hour, DatasetColumns.DECLINATION.value, 'hourly')
    _plot_aggregate(hour, DatasetColumns.POWER.value, 'hourly')


def _plot_measurement(df: DataFrame, column: str) -> None:
    title = "{} variable evolution".format(column)
    df[column].plot(title=title, ylabel=column, style='.', linestyle='none', ms=3)
    plt.show()


def _plot_aggregate(df: DataFrame, column: str, period: str) -> None:
    title = "{} variable {} mean evolution".format(column, period)
    df[column].plot(title=title, ylabel=column, style='.', linestyle='none', ms=10)
    plt.show()


def plot_boxes(df: DataFrame) -> None:
    pass
    _plot_measurement_box(df, DatasetColumns.G_POA.value)
    _plot_measurement_box(df, DatasetColumns.AIR_TEMP.value)
    _plot_measurement_box(df, DatasetColumns.WIND_SPEED.value)
    _plot_measurement_box(df, DatasetColumns.HUMIDITY.value)
    _plot_measurement_box(df, DatasetColumns.POWER.value)


def _plot_measurement_box(df: DataFrame, column: str) -> None:
    title = "{} variable boxplot".format(column)
    df[column].plot(
        kind='box',
        title=title,
        ylabel=column,
        showmeans=True,
        meanprops={"marker": "o",
                   "markerfacecolor": "white",
                   "markeredgecolor": "black",
                   "markersize": "10"},
        flierprops={"marker": "o",
                    "markerfacecolor": "white",
                    "markeredgecolor": "black",
                    "markersize": "5"},
    )
    plt.show()


def plot_correlations(df: DataFrame) -> None:
    pass
    _plot_power_measurement_correlation(df, DatasetColumns.G_POA.value)
    _plot_power_measurement_correlation(df, DatasetColumns.AIR_TEMP.value)
    _plot_power_measurement_correlation(df, DatasetColumns.WIND_SPEED.value)
    _plot_power_measurement_correlation(df, DatasetColumns.HUMIDITY.value)

    _extra_correlations(df)


def _extra_correlations(df: DataFrame) -> None:
    pass

    copy = df.copy()

    g_poa_squared = 'g_poa_squared'
    g_poa_wind = 'g_poa_wind'
    g_poa_temp = 'g_poa_temp'

    copy[g_poa_squared] = copy[DatasetColumns.G_POA.value] ** 2
    copy[g_poa_wind] = copy[DatasetColumns.G_POA.value] * \
        copy[DatasetColumns.WIND_SPEED.value]
    copy[g_poa_temp] = copy[DatasetColumns.G_POA.value] * \
        copy[DatasetColumns.AIR_TEMP.value]

    _plot_power_measurement_correlation(copy, g_poa_squared)
    _plot_power_measurement_correlation(copy, g_poa_wind)
    _plot_power_measurement_correlation(copy, g_poa_temp)


def _plot_power_measurement_correlation(df: DataFrame, column: str) -> None:
    correlation = df[column].corr(df[DatasetColumns.POWER.value])
    title = "Correlation index: {}".format(round(correlation, 4))
    df.plot.scatter(x=column, y=DatasetColumns.POWER.value,
                    c="DarkBlue", s=1, title=title)
    plt.show()


def plot_beyond_sdvs(df: DataFrame, sdv: int) -> None:
    pass
    _plot_measurements_beyond(df, sdv, DatasetColumns.G_POA.value)
    _plot_measurements_beyond(df, sdv, DatasetColumns.AIR_TEMP.value)
    _plot_measurements_beyond(df, sdv, DatasetColumns.HUMIDITY.value)
    _plot_measurements_beyond(df, sdv, DatasetColumns.WIND_SPEED.value)


def _plot_measurements_beyond(df: DataFrame, sdv: int, column: str) -> None:
    mask = (np.abs(stats.zscore(df[column])) > sdv)

    beyond = df[mask]
    inside = df[~mask]

    print(beyond.count())
    print(inside.count())

    title = "{} variable outliers".format(column)
    beyond[column].plot(label="outliers", ylabel=column,
                        style='o', linestyle='none', color="Red", ms=2)
    inside[column].plot(label="standard", ylabel=column,
                        style='o', linestyle='none', color="Blue", ms=2)
    plt.title(title)
    plt.legend()
    plt.show()
