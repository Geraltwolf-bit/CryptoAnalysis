#The S&P 500 is a stock market index that shows the performance of 500 large companies listed on US stock exchanges.
#It's an indicator of how economy does.

import requests
import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd
import json

def get_fear_greed_index():
    #fetch the current Crypto & Fear Index data in json
    url = "https://api.alternative.me/fng/"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def get_sp500_data(days = 30):
    #fetch S&P500 data for the specified number of days and return Pandas DataFrame with historical data:
    try:
        #get S&P 500 data
        sp500 = yf.Ticker("^GSPC")
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)

        #get historical data
        hist_data = sp500.history(start = start_date, end = end_date)

        #reset index to make Date a column
        hist_data.reset_index(inplace = True)

        print(f"S&P 500 data fetched successfully! ({len(hist_data)} days)")
        return hist_data[['Date', 'Close']]
    except Exception as e:
        print(f"Error fetching S&P 500 data: {e}")
        return None
    
def get_inflation_data():
    #for now, return cock inflation data since FRED API requires registration:
    today = datetime.now().date()
    mock_inflation = 3.2
    print("Using mock inflation data (replace with FRED API)")
    return {'date': today, 'inflation_rate': mock_inflation}

def test_data_extraction():
    fgi_data = get_fear_greed_index()
    if fgi_data:
        print(f"Latest FGI: {fgi_data['data'][0]['value']} - {fgi_data['data'][0]['value_classification']}")
    #test S&P500 data

    sp500_data = get_sp500_data(days = 7)
    if sp500_data is not None:
        print(f"S&P 500 sample: {sp500_data.head(2)}")
    
    #test inflation data
    inflation_data = get_inflation_data()
    print(f"Inflation rate: {inflation_data['inflation_rate']}%")

    if __name__ == '__main__':
        test_data_extraction()