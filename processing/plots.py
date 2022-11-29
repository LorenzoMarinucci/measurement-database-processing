from typing import Callable
from matplotlib import use
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pandas import DataFrame
from scipy import stats

from processing.constants.datasetConstants import DatasetColumns
from processing.constants.plotsConstants import PlotsConstants

import matplotlib.dates as mdates

use('TkAgg')

# Plot each measurement evolution
def plot_timeseries(df: DataFrame) -> None:
    group_by_day = df.to_period('D')
    group_by_day = group_by_day.groupby(level=0).mean()
    days = len(group_by_day)  # number of days in the data

    _plot_measurement(df, DatasetColumns.G_POA.value, days)
    _plot_measurement(df, DatasetColumns.AIR_TEMP.value, days)
    _plot_measurement(df, DatasetColumns.WIND_SPEED.value, days)
    _plot_measurement(df, DatasetColumns.HUMIDITY.value, days)
    _plot_measurement(df, DatasetColumns.DECLINATION.value, days)
    _plot_measurement(df, DatasetColumns.POWER.value, days)

    _plot_day_averages(group_by_day, days)
    _plot_hourly_averages(df, days)


def _plot_day_averages(group_by_day: DataFrame, current_ticks: int) -> None:
    dt_fmt = mdates.DateFormatter('%d %b')

    _plot_aggregate(group_by_day, DatasetColumns.G_POA.value, 'daily', current_ticks, _build_day_locator, dt_fmt)
    _plot_aggregate(group_by_day, DatasetColumns.AIR_TEMP.value, 'daily', current_ticks, _build_day_locator, dt_fmt)
    _plot_aggregate(group_by_day, DatasetColumns.WIND_SPEED.value, 'daily', current_ticks, _build_day_locator, dt_fmt)
    _plot_aggregate(group_by_day, DatasetColumns.HUMIDITY.value, 'daily', current_ticks, _build_day_locator, dt_fmt)
    _plot_aggregate(group_by_day, DatasetColumns.DECLINATION.value, 'daily', current_ticks, _build_day_locator, dt_fmt)
    _plot_aggregate(group_by_day, DatasetColumns.POWER.value, 'daily', current_ticks, _build_day_locator, dt_fmt)


def _plot_hourly_averages(df: DataFrame, days: int) -> None:
    group_by_hour = df.to_period('H')
    group_by_hour = group_by_hour.groupby(level=0).mean()

    hours_ticks = len(PlotsConstants.HOUR_RANGE.value) * days

    dt_fmt = mdates.DateFormatter('%d %b - %H:%M')

    _plot_aggregate(group_by_hour, DatasetColumns.G_POA.value, 'hourly', hours_ticks,
                    _build_hour_locator, dt_fmt)
    _plot_aggregate(group_by_hour, DatasetColumns.AIR_TEMP.value, 'hourly', hours_ticks,
                    _build_hour_locator, dt_fmt)
    _plot_aggregate(group_by_hour, DatasetColumns.WIND_SPEED.value, 'hourly', hours_ticks,
                    _build_hour_locator, dt_fmt)
    _plot_aggregate(group_by_hour, DatasetColumns.HUMIDITY.value, 'hourly', hours_ticks,
                    _build_hour_locator, dt_fmt)
    _plot_aggregate(group_by_hour, DatasetColumns.DECLINATION.value, 'hourly', hours_ticks,
                    _build_hour_locator, dt_fmt)
    _plot_aggregate(group_by_hour, DatasetColumns.POWER.value, 'hourly', hours_ticks,
                    _build_hour_locator, dt_fmt)


def _build_day_locator(interval: int) -> mdates.DayLocator: return mdates.DayLocator(interval=interval)


def _build_hour_locator(interval: int) -> mdates.HourLocator: return mdates.HourLocator(
    byhour=PlotsConstants.HOUR_RANGE.value, interval=interval)


def _plot_measurement(df: DataFrame, column: str, current_ticks: int) -> None:
    title = "{} variable evolution".format(column)
    df[column].plot(title=title, ylabel=column, style='.', linestyle='none', ms=3)

    dtFmt = mdates.DateFormatter('%d %b')  # define the formatting
    plt.gca().xaxis.set_major_formatter(dtFmt)

    # limit xticks
    _limit_xticks(current_ticks, _build_day_locator)

    plt.grid(True)
    plt.show()


def _plot_aggregate(df: DataFrame, column: str, period: str, current_ticks: int, build_locator: Callable,
                    dt_fmt: mdates.DateFormatter) -> None:
    title = "{} variable {} mean evolution".format(column, period)

    if len(df) == 1:
        delta = pd.Timedelta(days=1)
        lims = [df.index[0] - delta, df.index[0] + delta]
    else:
        lims = [None, None]

    df[column].plot(title=title, xlabel='datetime', ylabel=column, style='.', linestyle='none', ms=10, xlim=lims,
                    x_compat=True)

    plt.gca().xaxis.set_major_formatter(dt_fmt)  # define the formatting

    # limit xticks
    _limit_xticks(current_ticks, build_locator)

    plt.grid(True)
    plt.show()


"""
    Limits the number of ticks on the x axis.
    
    currentTicks: max number of ticks required by the plot.
    buildLocator: receives an interval and creates a locator.
"""


def _limit_xticks(current_ticks: int, build_locator: Callable) -> None:
    interval = 1 if PlotsConstants.TICKS_PER_PLOT.value > current_ticks else current_ticks // PlotsConstants.TICKS_PER_PLOT.value
    plt.gca().xaxis.set_major_locator(build_locator(interval))
    plt.xticks(rotation=PlotsConstants.TICKS_ROTATION.value, fontsize='small')


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
