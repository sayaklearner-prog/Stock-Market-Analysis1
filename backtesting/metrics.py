import numpy as np
import pandas as pd


def calculate_max_drawdown(
    equity: pd.Series
) -> float:

    peak = equity.cummax()

    drawdown = (
        equity / peak
    ) - 1

    return drawdown.min()


def calculate_metrics(
    df: pd.DataFrame,
    risk_free_rate: float = 0.06
) -> dict:

    returns = (
        df["Net_Strategy_Return"]
        .dropna()
    )

    equity = df["Strategy_Equity"]

    total_return = (
        equity.iloc[-1] - 1
    )

    days = (
        df.index[-1] -
        df.index[0]
    ).days

    years = days / 365.25

    if years > 0:

        cagr = (
            equity.iloc[-1]
            ** (1 / years)
        ) - 1

    else:

        cagr = np.nan

    annualized_volatility = (
        returns.std() *
        np.sqrt(252)
    )

    daily_rf = (
        risk_free_rate / 252
    )

    excess_returns = (
        returns - daily_rf
    )

    if returns.std() != 0:

        sharpe = (
            excess_returns.mean() /
            returns.std()
        ) * np.sqrt(252)

    else:

        sharpe = np.nan

    negative_returns = (
        returns[returns < 0]
    )

    downside_deviation = (
        negative_returns.std() *
        np.sqrt(252)
    )

    if downside_deviation != 0:

        sortino = (
            excess_returns.mean() *
            252 /
            downside_deviation
        )

    else:

        sortino = np.nan

    max_drawdown = calculate_max_drawdown(
        equity
    )

    if max_drawdown != 0:

        calmar = (
            cagr /
            abs(max_drawdown)
        )

    else:

        calmar = np.nan

    winning_returns = (
        returns[returns > 0]
    )

    losing_returns = (
        returns[returns < 0]
    )

    gross_profit = winning_returns.sum()

    gross_loss = abs(
        losing_returns.sum()
    )

    if gross_loss > 0:

        profit_factor = (
            gross_profit /
            gross_loss
        )

    else:

        profit_factor = np.nan

    trade_days = (
        returns[returns != 0]
    )

    if len(trade_days) > 0:

        win_rate = (
            len(winning_returns) /
            len(trade_days)
        )

    else:

        win_rate = np.nan

    number_of_trades = int(
        df["Trade"].sum()
    )

    buy_hold_return = (
        df["Buy_Hold_Equity"].iloc[-1]
        - 1
    )

    return {

        "Total Return": total_return,

        "CAGR": cagr,

        "Annualized Volatility":
            annualized_volatility,

        "Sharpe Ratio": sharpe,

        "Sortino Ratio": sortino,

        "Maximum Drawdown":
            max_drawdown,

        "Calmar Ratio": calmar,

        "Win Rate": win_rate,

        "Profit Factor": profit_factor,

        "Number of Trades":
            number_of_trades,

        "Buy & Hold Return":
            buy_hold_return
    }
