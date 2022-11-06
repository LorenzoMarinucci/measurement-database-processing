from pandas import DataFrame


def saveData(df: DataFrame, description: DataFrame) -> None:
    # Save dataframe. Ignore datetime
    df.to_csv("processedData.csv", index=False)

    # Save description
    with open("description.txt", "w") as file:
        file.write(description.to_string())
