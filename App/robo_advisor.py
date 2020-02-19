# app/robo_advisor.py

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="OOPS")
#SYMBOL = "TSLA"
SYMBOL =input("Please enter a company NYSE symbol: ")

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={SYMBOL}&interval=5min&outputsize=full&apikey={API_KEY}"
print("URL: ", request_url)

#request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey={API_KEY}"

#SYMBOL = input("Enter a company's symbol: ")

response = requests.get(request_url)
print(type(response))
print(response.status_code)
print(type(response.text))

## FIGURE OUT HOW TO LOOP THIS SO IF A USER ENTERS AN INVALID SYMBOL THEY JUST TRY AGAIN
while True:
    SYMBOL =input("Please enter a company NYSE symbol: ")
    if "Error Message" in response.text:
    print("Oops, couldn't find that symbol, please try a new one.")
        break
   
    else:
        selected_ids.append(selected_id)

parsed_response = json.loads(response.text)
print(type(parsed_response))
#print(parsed_response)




#breakpoint()

##ADD TO READ.ME HOW TO SETUP API KEY












print("-------------------------")
print("SELECTED SYMBOL: ", SYMBOL)
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print("LATEST DAY: 2018-02-20")
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")