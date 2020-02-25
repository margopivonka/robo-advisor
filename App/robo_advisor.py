# app/robo_advisor.py

import requests
import json
import os
import csv
import datetime as dt
from dotenv import load_dotenv

load_dotenv()

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)


API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="OOPS")
SYMBOL = input("Please enter a company NYSE symbol: ")
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={SYMBOL}&interval=5min&outputsize=full&apikey={API_KEY}"
execution_time = dt.datetime.now()
response = requests.get(request_url)


if "1" "2" "3" "4" "5" "6" "7" "8" "9" "0" in SYMBOL:
    print("----------------------------")    
    print("Whoops, please enter a valid company symbol that does not contain numerical values.")
    print("----------------------------")
    exit()
    
if "Error Message" in response.text:
    print("----------------------------")
    print("Whoops, that symbol does not exist. Please try another one.")
    print("----------------------------")
    exit()



parsed_response = json.loads(response.text)
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
tsd = parsed_response["Time Series (Daily)"]
dates = list(tsd.keys()) 
latest_day = dates[0]
latest_close = parsed_response["Time Series (Daily)"]["2020-02-19"]["4. close"]


high_prices = []

for date in dates:
    high_price =tsd[date]["2. high"] 
    high_prices.append(float(high_price))
recent_high = max(high_prices)


low_prices = []

for date in dates:
    low_price =tsd[date]["3. low"] 
    low_prices.append(float(low_price))
recent_low = min(low_prices)


csv_file_path = os.path.join(os.path.dirname(__file__),"..","data","prices.csv")
csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]


with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader()
    
    for date in dates:
        daily_prices = tsd[date]
        writer.writerow({
        "timestamp":date,
        "open":daily_prices["1. open"],
        "high":daily_prices["2. high"],
        "low":daily_prices["3. low"],
        "close":daily_prices["4. close"],
        "volume":daily_prices["5. volume"]
    })


close_price = daily_prices["4. close"]


if float(close_price) <= 1.20*float(recent_low):
    recommendation = "BUY"
    reason = "This stock is under-priced, and you should buy it now!"
elif (float(close_price) > 1.20*float(recent_low)) and (float(close_price) <= 1.40*float(recent_low)):
    recommendation = "MAYBE BUY"
    reason = "This stock may be under-priced, do some research or buy a limited amount."
elif float(close_price) >= 1.40*float(recent_low):
    recommendation = "DO NOT BUY"
    reason = "This stock is not under-priced. I do not recommend that you buy any of it."



print("-------------------------")
print("SELECTED SYMBOL: ", SYMBOL)
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: ", execution_time.strftime("%Y-%m-%d %I:%M %p"))
print("-------------------------")
print("LAST REFRESHED: ", last_refreshed)
print("LATEST DAY: ", latest_day)
print(f"LATEST CLOSE: ", to_usd(float(latest_close)))
print(f"RECENT HIGH: ", to_usd(float(recent_high)))
print("RECENT LOW: ", to_usd(float(recent_low)))
print("-------------------------")
print("RECOMMENDATION: ", recommendation)
print("RECOMMENDATION REASON: ", reason)
print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}...")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")

