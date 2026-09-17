import matplotlib.pyplot as plt


def plot_price_and_moving_averages(
    df,
    symbol
):

    plt.figure(figsize=(15, 7))

    plt.plot(
        df.index,
        df["Close"],
        label="Close"
    )

    plt.plot(
        df.index,
        df["SMA20"],
        label="SMA 20"
    )

    plt.plot(
        df.index,
        df["SMA50"],
        label="SMA 50"
    )

    plt.plot(
        df.index,
        df["SMA200"],
        label="SMA 200"
    )

    plt.title(
        f"{symbol} - Price Analysis"
    )

    plt.xlabel("Date")
    plt.ylabel("Price")

    plt.legend()
    plt.grid(alpha=0.3)

    plt.tight_layout()
    plt.show()


def plot_strategy_performance(
    df,
    symbol
):

    plt.figure(figsize=(15, 7))

    plt.plot(
        df.index,
        df["Strategy_Equity"],
        label="Strategy"
    )

    plt.plot(
        df.index,
        df["Buy_Hold_Equity"],
        label="Buy & Hold"
    )

    plt.title(
        f"{symbol} - Strategy Performance"
    )

    plt.xlabel("Date")
    plt.ylabel("Growth of ₹1")

    plt.legend()
    plt.grid(alpha=0.3)

    plt.tight_layout()
    plt.show()


def plot_rsi(df, symbol):

    plt.figure(figsize=(15, 5))

    plt.plot(
        df.index,
        df["RSI"],
        label="RSI"
    )

    plt.axhline(
        70,
        linestyle="--",
        label="Overbought"
    )

    plt.axhline(
        30,
        linestyle="--",
        label="Oversold"
    )

    plt.axhline(
        50,
        linestyle=":",
        label="Neutral"
    )

    plt.title(
        f"{symbol} - RSI"
    )

    plt.legend()
    plt.grid(alpha=0.3)

    plt.tight_layout()
    plt.show()
