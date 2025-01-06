import requests

STOCK = "TSLA"  # Stock ticker symbol
API_KEY = "9ZLZ5FCJ8XKKE2CS"  # Replace with your Alpha Vantage API key

# Define parameters for the Alpha Vantage API
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY
}

# Request stock data
url = "https://www.alphavantage.co/query"
response = requests.get(url, params=parameters)
data = response.json()

# Check if the response contains the "Time Series (Daily)" data
if "Time Series (Daily)" in data:
    # Get the daily time series data
    time_series = data["Time Series (Daily)"]
    dates = list(time_series.keys())

    # Get the two most recent trading days
    yesterday = dates[0]
    day_before_yesterday = dates[1]

    # Get the closing prices
    yesterday_close = float(time_series[yesterday]['4. close'])
    day_before_yesterday_close = float(time_series[day_before_yesterday]['4. close'])

    # Calculate the percentage change
    percent_change = ((yesterday_close - day_before_yesterday_close) / day_before_yesterday_close) * 100

    # Check if the percentage change is 5% or more
    if abs(percent_change) >= 5:
        print("Get News")
        change_direction = "🔺" if percent_change > 0 else "🔻"
        print(f"{STOCK}: {change_direction}{abs(percent_change):.2f}%")
    else:
        print(f"No significant change: {percent_change:.2f}%")
else:
    print("Error: Could not fetch 'Time Series (Daily)' data. Please check your API key and parameters.")
