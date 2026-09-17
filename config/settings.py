from dataclasses import dataclass


@dataclass
class Settings:
    start_date: str = "2020-01-01"
    end_date: str = "2026-01-01"

    initial_capital: float = 100_000.0

    short_ma: int = 20
    long_ma: int = 50
    trend_ma: int = 200

    rsi_period: int = 14

    macd_fast: int = 12
    macd_slow: int = 26
    macd_signal: int = 9

    bollinger_period: int = 20
    bollinger_std: float = 2.0

    atr_period: int = 14

    transaction_cost: float = 0.001
    slippage: float = 0.0005

    risk_free_rate: float = 0.06


settings = Settings()
