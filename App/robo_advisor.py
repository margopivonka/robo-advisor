# app/robo_advisor.py

import csv
import datetime
import json
import os

from dotenv import load_dotenv
import requests

load_dotenv() #> loads contents of the .env file into the script's environment


#
# INFO INPUTS
#

api_key = os.environ.get("ALPHAVANTAGE_API_KEY") # "demo"
#print(api_key)

def get_response(symbol):
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    return parsed_response

def transform_response(parsed_response):
    tsd = parsed_response["Time Series (Daily)"]

    rows = []
    for date, daily_prices in tsd.items():
        row = {
            "timestamp": date, 
            "open": float(daily_prices["1. open"]),
            "high": float(daily_prices["2. high"]),
            "low": float(daily_prices["3. low"]),
            "close": float(daily_prices["4. close"]),
            "volume": float(daily_prices["5. volume"])
        }
        rows.append(row)

    return rows


def write_to_csv(rows, csv_filepath):
    csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

    with open(csv_filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    return True


def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

if __name__ == "__main__":
    time_now = datetime.datetime.now()


#
# INFO INPUTS
#

symbol = input("Please enter an NYSE company ticker symbol: ")

parsed_response = get_response(symbol)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

rows = transform_response(parsed_response)


latest_close = rows[0]["close"]
high_prices = [row["high"] for row in rows]
low_prices = [row["low"] for row in rows]
recent_high = max(high_prices)
recent_low = min(low_prices)

#
# RECOMMENDATION CRITERIA
#

if float(latest_close) <= 1.20*float(recent_low):
    recommendation = "BUY"
    reason = "This stock is under-priced, and you should buy as much as you can now!"
elif (float(latest_close) > 1.20*float(recent_low)) and (float(latest_close) <= 1.40*float(recent_low)):
    recommendation = "MAYBE BUY"
    reason = "This stock may be under-priced; do some research or buy a limited amount."
elif float(latest_close) >= 1.40*float(recent_low):
    recommendation = "DO NOT BUY"
    reason = "This stock is over-priced and you should not buy it."
#
# WRITE TO CSV FILE
#

csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

write_to_csv(rows, csv_filepath)

#
# DISPLAY RESULTS
#

formatted_time_now = time_now.strftime("%Y-%m-%d %H:%M:%S")
formatted_csv_filepath = csv_filepath.split("../")[0]



print("-------------------------")
print("SELECTED SYMBOL: MSFT")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: " + recommendation)
print("BECAUSE: " + reason)
print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_filepath}")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
