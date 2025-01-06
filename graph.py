import requests
from datetime import datetime
import matplotlib.pyplot as plt

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

# Check if the response contains the "Time Series (Daily)" data
if "Time Series (Daily)" in data:
    dis_dicts = data["Time Series (Daily)"]
    dis_dates, highs, lows = [], [], []

    for date in dis_dicts:
        dis_dates.append(datetime.strptime(date, '%Y-%m-%d'))
        highs.append(float(dis_dicts[date]['2. high']))
        lows.append(float(dis_dicts[date]['3. low']))

    # Sort the dates to ensure proper plotting
    dis_dates, highs, lows = zip(*sorted(zip(dis_dates, highs, lows)))
    print(f"HIGHS: {highs}\n LOWS: {lows}")


#     # PLOT THE HIGHS AND LOWS
#     plt.style.use('ggplot')
#     fig, ax = plt.subplots()
#     ax.plot(dis_dates, highs, c='red', alpha=0.6, label="Highs")
#     ax.plot(dis_dates, lows, c='blue', alpha=0.6, label="Lows")
#     ax.fill_between(dis_dates, highs, lows, facecolor='blue', alpha=0.15)
#
#     # FORMAT PLOT
#     ax.set_title(f"{STOCK} Daily High and Low Stock Prices", fontsize=24)
#     ax.set_xlabel('', fontsize=16)
#     fig.autofmt_xdate()
#     ax.set_ylabel("Price (USD)", fontsize=12)
#     ax.tick_params(axis='both', which='major', labelsize=10)
#     plt.ylim(min(lows), max(highs))
#     ax.legend()
#
#     # Show the plot
#     plt.show()
# else:
#     print("Error: Could not fetch 'Time Series (Daily)' data. Please check your API key and parameters.")






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

