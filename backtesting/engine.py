import pandas as pd


class BacktestEngine:

    def __init__(
        self,
        initial_capital: float = 100_000,
        transaction_cost: float = 0.001,
        slippage: float = 0.0005
    ):

        self.initial_capital = initial_capital
        self.transaction_cost = transaction_cost
        self.slippage = slippage

    def run(
        self,
        df: pd.DataFrame
    ) -> pd.DataFrame:

        data = df.copy()

        # Market returns
        data["Market_Return"] = (
            data["Close"].pct_change()
        )

        # Strategy returns
        data["Strategy_Return"] = (
            data["Position"] *
            data["Market_Return"]
        )

        # Position changes
        data["Trade"] = (
            data["Position"]
            .diff()
            .abs()
            .fillna(0)
        )

        # Trading costs
        total_cost = (
            self.transaction_cost +
            self.slippage
        )

        data["Trading_Cost"] = (
            data["Trade"] *
            total_cost
        )

        # Net strategy return
        data["Net_Strategy_Return"] = (
            data["Strategy_Return"] -
            data["Trading_Cost"]
        )

        # Equity curve
        data["Strategy_Equity"] = (
            1 +
            data["Net_Strategy_Return"]
            .fillna(0)
        ).cumprod()

        data["Buy_Hold_Equity"] = (
            1 +
            data["Market_Return"]
            .fillna(0)
        ).cumprod()

        # Capital
        data["Strategy_Capital"] = (
            data["Strategy_Equity"] *
            self.initial_capital
        )

        data["Buy_Hold_Capital"] = (
            data["Buy_Hold_Equity"] *
            self.initial_capital
        )

        return data
