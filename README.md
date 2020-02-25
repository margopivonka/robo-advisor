# robo-advisor

## Installation
clone or download from [GitHub source] (https://github.com/margopivonka/robo-advisor), then navigate into the project repositiory using the command line:

```
cd robo_adivsor
```

## API Key Setup
To access stock data, you will need your own API access key. 
Go to https://www.alphavantage.co/ and apply for a personal access key.

In the .env file, paste your API key into the variable:
```
ALPHAVANAGE_API_KEY = "your API key"
```


## Environment Setup
Create and activate a new Anaconda environment:
```
conda create -n stocks-env python=3.7 #(first time only)
conda activate stocks-env
```

From within the virtual environment, install the required packages specified in the "requirements.txt" file:
```
pip install -r requirements.txt
```

From within the virtual environment, run the Python script from the command line
```
python app/robo_advisor.py
```




## Usage
Run the program:
```
python app/robo_advisor.py
```
Your command line will prompt you to enter a company's NYSE market symbol, and after doing so, it will give you a recommendation based on stock data available.

### CSV File data
After running this program, all data available from the URL for the stock symbol entered will be available in a file labeled:
```
prices.csv
```
This file is located within the
 ```
 data
 ```
folder, and can be used to take a closer look at stock prices or stock that is recommended to "maybe buy"

# HAPPY INVESTING!!! :)
