# Overview
This Python script provides a simple tool to analyze the price movement of Bitcoin (BTC) in relation to USDT and gives a recommendation whether to Buy or Sell based on recent price data.

# Requirements
- Python 3.x
- 'requests' library (install via 'pip install requests')

# Usage

1. API KEYS: Before running the script, make sure to replace the placeholder 'API KEY HERE' and 'API SECRET HERE' with your actual Binance API key and secret in the 'main()' function. **(Never share that with anyone!)**
2. Run the script: Execute the 'main()' function in the script. This will fetch the latest candle data for BTC to USDT pair from Binance API, calculate the price difference between the last two hours, and provide a recommendation to Buy or Sell based on the price movement.
3. Output: The script will print "Buy" or "Sell" based on the calculated price difference and also save the candle data to a CSV file named 'stored_data_info.csv'. (Feel free to modify the name to your desire.)

# Functions

- 'get_candle_data(symbol, interval, limit)': Fetches candlestick data for a specified trading pair (symbol), time interval and limit from the Binance API.
- 'calculate_price_difference(candle_data)': Calculates the difference between the closing prices of the last two hours.
- 'format_timestamp(timestamp)':Formats the timestamp from miliseconds to a human-readable format.
- 'save_data(data, filename)':Saves the candlestick data to a CSV file for further examination.

