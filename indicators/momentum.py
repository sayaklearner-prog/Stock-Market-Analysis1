import pandas as pd


def add_rsi(
    df: pd.DataFrame,
    period: int = 14
) -> pd.DataFrame:

    data = df.copy()

    delta = data["Close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    average_gain = gain.rolling(
        period
    ).mean()

    average_loss = loss.rolling(
        period
    ).mean()

    rs = (
        average_gain /
        average_loss.replace(0, pd.NA)
    )

    data["RSI"] = (
        100 -
        (100 / (1 + rs))
    )

    return data


def add_macd(
    df: pd.DataFrame,
    fast: int = 12,
    slow: int = 26,
    signal: int = 9
) -> pd.DataFrame:

    data = df.copy()

    fast_ema = data["Close"].ewm(
        span=fast,
        adjust=False
    ).mean()

    slow_ema = data["Close"].ewm(
        span=slow,
        adjust=False
    ).mean()

    data["MACD"] = (
        fast_ema - slow_ema
    )

    data["MACD_SIGNAL"] = (
        data["MACD"].ewm(
            span=signal,
            adjust=False
        ).mean()
    )

    data["MACD_HISTOGRAM"] = (
        data["MACD"] -
        data["MACD_SIGNAL"]
    )

    return data
