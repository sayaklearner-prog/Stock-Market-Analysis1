import pandas as pd


def add_volume_indicators(
    df: pd.DataFrame,
    period: int = 20
) -> pd.DataFrame:

    data = df.copy()

    data["Volume_SMA"] = (
        data["Volume"]
        .rolling(period)
        .mean()
    )

    data["Volume_Ratio"] = (
        data["Volume"] /
        data["Volume_SMA"]
    )

    return data
