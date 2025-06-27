# filename: plot_ytd_stock_gains.py

import matplotlib.pyplot as plt
import yfinance as yf

# Define the stock tickers
tickers = ['NVDA', 'TSLA']

# Define the start and end dates for the current year
start_date = '2025-01-01'
end_date = '2025-06-27'

# Download the historical data for the given date range
data = yf.download(tickers, start=start_date, end=end_date, auto_adjust=False)

# Use 'Close' column for calculations
ytd_gains = (data['Close'].iloc[-1] - data['Close'].iloc[0]) / data['Close'].iloc[0] * 100

# Plot the data
plt.figure(figsize=(10, 6))
ytd_gains.plot(kind='bar')
plt.title('YTD Stock Gains for NVDA and TSLA (2025)')
plt.xlabel('Ticker')
plt.ylabel('Percent Gain (%)')
plt.xticks(rotation=0)
plt.tight_layout()

# Save the plot to a file
plt.savefig('ytd_stock_gains.png')
plt.show()