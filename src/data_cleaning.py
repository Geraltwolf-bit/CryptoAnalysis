import pandas as pd
from datetime import datetime, timedelta
import numpy as np

def classify_fgi_value(value):
    #convert Fear & Greed Index numericals to classfication strings:
    if value >= 75:
        return "Extreme Greed"
    elif value >= 55:
        return "Greed"
    elif value >= 45:
        return "Neutral"
    elif value >= 25:
        return "Fear"
    else:
        return "Extreme Fear"
    
def clean_fear_greed_data(fgi_data):
    if not fgi_data or 'data' not in fgi_data:
        print("No valid data to clean")
        return None
    try:
        data_list = fgi_data['data']
        df = pd.DataFrame(data_list)
        df['value'] = pd.to_numeric(df['value'], error = 'coerce')
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit = 's')
        df.rename(columns = {
            'value': 'fgi_value',
            'timestamp': 'date',
            'value_classification': 'fgi_classification'
        }, inplace = True)

        df['fgi_classification'] = df['fgi_value'].apply(classify_fgi_value)

        df = df[['date', 'fgi_value', 'fgi_classification']]
        df['date'] = df['date'].dt.date

        df = df.dropna()

        print(f"FGI data cleaned: {len(df)} records")
        return df
    
    except Exception as e:
        print(f"Error cleaning FGI data: {e}")
        return None
    
def clean_sp500_data(sp500_data):
    if not sp500_data or 'data' not in sp500_data:
        print("No valid data to clean")
        return None
    try:
        df = sp500_data.copy()
        df['Date'] = pd.to_datetime(df['Date']).dt.date
        df.rename(columns = {
            'Date': 'date',
            'Close': 'sp500_close'
        }, inplace = True)

        df = df[['date', 'sp500_close']]

        df = df.dropna()
        print(f"S&P 500 data cleaned: {len(df)} records")
        return df
    except Exception as e:
        print(f"Error cleaning inflation data: {e}")
        return None

def clean_inflation_data(inflation_data):
    try:
        df = pd.DataFrame([inflation_data])
        df['date'] = pd.to_datetime(df['date']).dt.date
        print("Inflation data cleaned!")
        return df
    except Exception as e:
        print(f"Error cleaning inflation data: {e}")
        return None

def merge_all_data(fgi_clean, sp500_clean, inflation_clean):
    try:
        merged_df = fgi_clean
        if sp500_clean is not None:
            merged_df = pd.merge(merged_df, sp500_clean, on = 'date', how = 'left')
        if inflation_clean is not None:
            merged_df = pd.merge(merged_df, inflation_clean, on = 'date', how = 'left')
        if 'sp500_close' in merged_df.columns:
            merged_df['sp500_close'] = merged_df['sp500_close'].fillna(method = 'ffill')
        return merged_df
    except Exception as e:
        print(f"Error merging data: {e}")
        return None