# app/robo_advisor.py

import requests
import json
import os
from dotenv import load_dotenv
import datetime as dt

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)


load_dotenv()




API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="OOPS")

SYMBOL =input("Please enter a company NYSE symbol: ")

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={SYMBOL}&interval=5min&outputsize=full&apikey={API_KEY}"

response = requests.get(request_url)

parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]


tsd = parsed_response["Time Series (Daily)"]

#breakpoint()


dates = list(tsd.keys()) #TODO: assumes first day is on top, but consider sorting to ensure
latest_day = dates[0]
latest_close = parsed_response["Time Series (Daily)"]["2020-02-19"]["4. close"]
recent_high = parsed_response["Time Series (Daily)"]["2020-02-19"]["2. high"]
recent_low = parsed_response["Time Series (Daily)"]["2020-02-19"]["3. low"]


## TODO: ADD TO READ.ME HOW TO SETUP API KEY







#
# Print time data was requested
#

execution_time = dt.datetime.now()


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
#print("RECOMMENDATION: BUY!")
#print("RECOMMENDATION REASON: TODO")
#print("-------------------------")
#print("HAPPY INVESTING!")
#print("-------------------------")