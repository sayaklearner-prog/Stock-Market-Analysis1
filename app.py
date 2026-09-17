from config.settings import settings

from analysis.stock_analyzer import (
    StockAnalyzer
)

from visualization.charts import (
    plot_price_and_moving_averages,
    plot_strategy_performance,
    plot_rsi
)


def main():

    symbol = "RELIANCE.NS"

    analyzer = StockAnalyzer(
        initial_capital=settings.initial_capital,
        transaction_cost=settings.transaction_cost,
        slippage=settings.slippage,
        risk_free_rate=settings.risk_free_rate
    )

    print(
        f"\nAnalyzing {symbol}..."
    )

    data, metrics = analyzer.analyze(
        symbol=symbol,
        start_date=settings.start_date,
        end_date=settings.end_date
    )

    # -----------------------------
    # Performance report
    # -----------------------------

    print("\n" + "=" * 60)

    print(
        f"STOCK ANALYSIS: {symbol}"
    )

    print("=" * 60)

    for metric, value in metrics.items():

        if isinstance(value, float):

            if (
                "Return" in metric
                or "CAGR" in metric
                or "Volatility" in metric
                or "Drawdown" in metric
                or "Rate" in metric
            ):

                print(
                    f"{metric:<30}"
                    f"{value:.2%}"
                )

            else:

                print(
                    f"{metric:<30}"
                    f"{value:.2f}"
                )

        else:

            print(
                f"{metric:<30}"
                f"{value}"
            )

    # -----------------------------
    # Charts
    # -----------------------------

    plot_price_and_moving_averages(
        data,
        symbol
    )

    plot_strategy_performance(
        data,
        symbol
    )

    plot_rsi(
        data,
        symbol
    )


if __name__ == "__main__":
    main()
