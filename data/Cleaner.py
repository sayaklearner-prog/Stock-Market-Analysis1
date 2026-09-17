import pandas as pd

def clean_stock_data(data: pd.DataFrame) -> pd.DataFrame:

    df = data.copy()

    df = df.sort_index()

    df = df[~df.index.duplicated(keep="first")]

    numeric_columns = [
        "Open",
        "High",
        "Low",
        "Close",
        "Volume"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    df.dropna(
        subset=numeric_columns,
        inplace=True
    )

    df = df[
        (df["High"] >= df["Low"]) &
        (df["Volume"] >= 0)
    ]

    return df
