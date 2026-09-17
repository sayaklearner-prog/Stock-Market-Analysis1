import pandas as pd


def generate_signals(
    df: pd.DataFrame
) -> pd.DataFrame:

    data = df.copy()

    # -----------------------------
    # Trend confirmation
    # -----------------------------

    trend_condition = (
        (data["SMA20"] > data["SMA50"]) &
        (data["Close"] > data["SMA200"])
    )

    # -----------------------------
    # Momentum confirmation
    # -----------------------------

    momentum_condition = (
        (data["RSI"] > 50) &
        (data["MACD"] > data["MACD_SIGNAL"])
    )

    # -----------------------------
    # Volume confirmation
    # -----------------------------

    volume_condition = (
        data["Volume_Ratio"] > 1
    )

    # -----------------------------
    # Final signal
    # -----------------------------

    data["Signal"] = (
        trend_condition &
        momentum_condition &
        volume_condition
    ).astype(int)

    # Execute next day
    data["Position"] = (
        data["Signal"]
        .shift(1)
        .fillna(0)
    )

    return data
