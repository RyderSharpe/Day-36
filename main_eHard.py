import requests


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API = "9ZLZ5FCJ8XKKE2CS"

# STEP 1: Use Alpha Vantage API
my_parameters = {
    "function": "TIME_SERIES_DAILY",  # Request daily time series data
    "symbol": STOCK,  # Stock ticker symbol
    "apikey": API,  # Your API key
    "outputsize": "compact",  # Get 100 data points
    "datatype": "json"  # Response in JSON format
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

url = 'https://www.alphavantage.co/query'
r = requests.get(url, params=my_parameters)
data = r.json()
# print(data)

# Check if the response contains the "Time Series (Daily)" data
if "Time Series (Daily)" in data:
    # Get the daily time series data
    time_series = data["Time Series (Daily)"]
    dates = list(time_series.keys())
    # print(time_series)
    # print(dates)



    # Get the two most recent trading days
    yesterday = dates[0]
    day_before_yesterday = dates[1]
    # print(yesterday)
    # print(day_before_yesterday)

    # Consolidated ↓↓↓↓↓
    # print(r.json().get("Time Series (Daily)").get(list(r.json().get("Time Series (Daily)").keys())[0]))








## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

