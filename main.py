import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "9ZLZ5FCJ8XKKE2CS"
NEWS_API_KEY = "f4ee929cb5fb417090a4e3f448cc6f8e"

TWILIO_SID = "ACc956a2963c723a94bbb4a99857215767"
TWILIO_AUTH_TOKEN = "2a49ab8f71ad196b95c973250a0dce76"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function": "TIME_SERIES_DAILY",  # Request daily time series data
    "symbol": STOCK_NAME,  # Stock ticker symbol
    "apikey": STOCK_API_KEY,  # Your API key
    "outputsize": "compact",  # Get 100 data points
    "datatype": "json"  # Response in JSON format
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]


# data_list = [new_item for (key, value) in list]
data_list = [value for (key, value) in data.items()]
yesterdays_data = data_list[0]
yesterdays_closing_price = float(yesterdays_data["4. close"])
print(f"Yesterdays closing price: {yesterdays_closing_price}")

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_closing_price = float(day_before_yesterday_data["4. close"])
print(f"Day before yesterday closing price: {day_before_closing_price}")

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
# Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = float(yesterdays_closing_price) - float(day_before_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (difference / yesterdays_closing_price) * 100
print(f"Percent Difference: {diff_percent}")

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

if abs(diff_percent) > 0.001:
    print("Get News")

    news_params = {
        "apiKey": NEWS_API_KEY,
        "qinTitle": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    #TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    # Above ^

    #TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]
    print(three_articles)


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.

    #TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]


    #TODO 9. - Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            from_='+12316362985',
            body=article,
            to='MY PHONE NUMBER'
        )



#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

