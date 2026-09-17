import pandas as pd
import numpy as np


def add_bollinger_bands(
    df: pd.DataFrame,
    period: int = 20,
    std_multiplier: float = 2.0
) -> pd.DataFrame:

    data = df.copy()

    middle = (
        data["Close"]
        .rolling(period)
        .mean()
    )

    std = (
        data["Close"]
        .rolling(period)
        .std()
    )

    data["BB_MIDDLE"] = middle

    data["BB_UPPER"] = (
        middle +
        std_multiplier * std
    )

    data["BB_LOWER"] = (
        middle -
        std_multiplier * std
    )

    return data


def add_atr(
    df: pd.DataFrame,
    period: int = 14
) -> pd.DataFrame:

    data = df.copy()

    previous_close = (
        data["Close"].shift(1)
    )

    range_1 = (
        data["High"] -
        data["Low"]
    )

    range_2 = (
        data["High"] -
        previous_close
    ).abs()

    range_3 = (
        data["Low"] -
        previous_close
    ).abs()

    true_range = pd.concat(
        [range_1, range_2, range_3],
        axis=1
    ).max(axis=1)

    data["ATR"] = (
        true_range
        .rolling(period)
        .mean()
    )

    return data


def add_volatility(
    df: pd.DataFrame,
    period: int = 20
) -> pd.DataFrame:

    data = df.copy()

    data["Daily_Return"] = (
        data["Close"].pct_change()
    )

    data["Volatility"] = (
        data["Daily_Return"]
        .rolling(period)
        .std()
        * np.sqrt(252)
    )

    return data
