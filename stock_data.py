import yfinance as yf
import matplotlib.pyplot as plt
#Download Reliance Stock Data from Yahoo Finance
ticker = "RELIANCE.NS"
stock = yf.download(
    ticker,
    start="2024-01-01",
    end="2025-01-01"
)
#Calculating Moving Averages
stock["MA20"] = stock[("Close",ticker)].rolling(20).mean()
stock["MA50"] = stock[("Close",ticker)].rolling(50).mean()
#Calculating Daily Returns
stock["Daily Return"] = stock[("Close",ticker)].pct_change()
print(stock["Daily Return"].head())
print("Average Daily Return:")
print(f"Average Daily Return: {stock['Daily Return'].mean()*100:.4f}%")
stock["Signal"] = 0

stock.loc[stock["MA20"] > stock["MA50"], "Signal"] = 1

stock.loc[stock["MA20"] < stock["MA50"], "Signal"] = -1
print(
    stock[
        ["MA20","MA50","Signal"]
    ].tail(20)
)
print("Highest Price:")
print(f"Highest Price: {stock[('High',ticker)].max():.2f}")

print("Lowest Price:")
print(f"Lowest Price: {stock[('Low',ticker)].min():.2f}")

print("Average Volume:")
print(f"Average Volume: {stock[('Volume',ticker)].mean():.0f}")

#show buy and sell counts
buy_signals = (stock["Signal"] == 1).sum()
sell_signals = (stock["Signal"] == -1).sum()
print(f"Buy Signals: {buy_signals}")
print(f"Sell Signals: {sell_signals}")

plt.figure(figsize=(12,5))
plt.plot(stock[("Close",ticker)], label="Close Price")
plt.plot(stock["MA20"], label="20-Day MA")
plt.plot(stock["MA50"], label="50-Day MA")
plt.title("Reliance Stock Analysis")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.savefig("reliance_analysis.png")
plt.show()