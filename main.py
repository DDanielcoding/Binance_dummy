import requests
import json
import csv
import os
from datetime import datetime

# Function to get candle data from the Binance API
def get_candle_data(symbol, interval, limit):
    url = f"https://api.binance.com/api/v1/klines?symbol={symbol}&interval={interval}&limit={limit}"
    api_response = requests.get(url)
    return json.loads(api_response.text)

# Function to calculate the difference between the last two hour's closing prices
def calculate_price_difference(candle_data):
    last_close = float(candle_data[-1][4])  # Closing price of the last hour
    previous_close = float(candle_data[-2][4])  # Closing price of the hour before last
    return last_close - previous_close

# Function to format the timestamp
def format_timestamp(timestamp):
    return datetime.utcfromtimestamp(timestamp / 1000).strftime('%H:%M %d.%m.%Y')

# Function to save data to CSV file
def save_data(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close Time'])
        for row in data:
            formatted_row = [
                format_timestamp(row[0]), # Format Open time
                row[1], # Open
                row[2], # High
                row[3], # Low
                row[4], # Close
                row[5], # Volume
                format_timestamp(row[6]) # Format close time
            ]
            writer.writerow(formatted_row)

# Main function
def main():
    api_key = 'API KEY HERE'
    api_secret = 'API SECRET HERE'
    symbol = 'BTCUSDT'  # Bitcoin to USDT
    interval = '1h'  # 1 hour interval
    limit = 2  # last 2 hour of data

    # Fetch candle data
    candle_data = get_candle_data(symbol, interval, limit)

    # Calculate price difference
    price_difference = calculate_price_difference(candle_data)

    # Print out Buy or Sell based on price difference
    if price_difference < 0:
        print("Buy")
    else:
        print("Sell")

    # Save data to CSV file
    filename = 'stored_data_info.csv'
    if not os.path.exists(filename):
        save_data(candle_data, filename)
        print(f"Data saved to {filename}")
    else:
        print("File already exists. Skipping save.")

if __name__ == "__main__":
    main()