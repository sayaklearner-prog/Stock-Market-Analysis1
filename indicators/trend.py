import pandas as pd


def add_trend_indicators(
    df: pd.DataFrame
) -> pd.DataFrame:

    data = df.copy()

    close = data["Close"]

    data["SMA20"] = (
        close.rolling(20).mean()
    )

    data["SMA50"] = (
        close.rolling(50).mean()
    )

    data["SMA200"] = (
        close.rolling(200).mean()
    )

    data["EMA20"] = (
        close.ewm(
            span=20,
            adjust=False
        ).mean()
    )

    data["EMA50"] = (
        close.ewm(
            span=50,
            adjust=False
        ).mean()
    )

    return data
