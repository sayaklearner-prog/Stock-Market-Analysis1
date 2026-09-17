import yfinance as yf
import pandas as pd


def download_stock_data(
    symbol: str,
    start_date: str,
    end_date: str
) -> pd.DataFrame:

    data = yf.download(
        symbol,
        start=start_date,
        end=end_date,
        auto_adjust=True,
        progress=False
    )

    if data.empty:
        raise ValueError(
            f"No market data found for {symbol}"
        )

    # yfinance can return MultiIndex columns
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    required_columns = [
        "Open",
        "High",
        "Low",
        "Close",
        "Volume"
    ]

    missing = [
        column
        for column in required_columns
        if column not in data.columns
    ]

    if missing:
        raise ValueError(
            f"Missing columns for {symbol}: {missing}"
        )

    data = data[required_columns].copy()

    data.dropna(inplace=True)

    data.index = pd.to_datetime(data.index)

    return data
