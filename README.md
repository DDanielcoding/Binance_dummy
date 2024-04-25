# Overview
This Python script provides a simple tool to analyze the price movement of Bitcoin (BTC) in relation to USDT and gives a recommendation whether to Buy or Sell based on recent price data.

# Requirements
- Python 3.x
- 'requests' library (install via 'pip install requests')

# Functions

- 'get_candle_data(symbol, interval, limit)': Fetches candlestick data for a specified trading pair (symbol), time interval and limit from the Binance API.
- 'calculate_price_difference(candle_data)': Calculates the difference between the closing prices of the last two hours.
- 'format_timestamp(timestamp)':Formats the timestamp from miliseconds to a human-readable format.
- 'save_data(data, filename)':Saves the candlestick data to a CSV file for further examination.

