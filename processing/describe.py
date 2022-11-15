import pandas as pd
from pandas import DataFrame

from processing.constants.datasetConstants import DatasetColumns


def describe_dataframe(df: DataFrame) -> DataFrame:
    describe = df[
        df.columns.difference([DatasetColumns.DATETIME.value, DatasetColumns.DATENUM.value])
    ].describe()

    describe.loc['var'] = describe.loc['std'] ** 2

    return describe
