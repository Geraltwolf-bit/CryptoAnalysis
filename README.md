THE PROBLEM:

People often lose money on crypto, because they buy when the market is in a state of "greed" (prices are high) and sell when the market is in "fear" (prices are low).

There are a lot of sources that show the crypto "Fear & Greed Index", like https://alternative.me/crypto/fear-and-greed-index/:

![Crypto Fear & Greed Index](images/dashboard.png)

Trouble is, Fear & Greed Index only shows market's sentiment and doesn't answer if the low/high price is justified or not.


THE SOLUTION:

To help people make better decisions, I built an interactive dashboard that squares the crypto "Fear & Greed Index" with real economy indicators: S&P 500 Index (stock market health) and inflation rate.

The dashboard shows in real time if a crash - Extreme Fear - is a bad time to sell or good. If S&P 500 is high and inflation is low, it means that economy is strong and crypto will bounce back. It's a buying opportunity!

If the price is high - Extreme Greed - but S&P 500 is low and inflation is high, it means rising crypto is driven by something irrelevant, like a social media hype, and is, in fact, a bubble that is about to pop. Time to sell!

Insights:

|         Crypto Sentiment      | S&P 500 Index  | Inflation |             Interpretation          |
|-------------------------------|----------------|-----------|-------------------------------------|
| 🟩 Extreme Fear  (low price)  | 📈  Rising    | 📉  Low   | Fear is irrational      - buy       |
| 🟥 Extreme Greed (high price) | 📉  Falling   | 📈  High  | High price is a bubble  - sell      |
| 🟥 Extreme Fear  (low price)  | 📉  Falling   | 📈  High  | Low price is justified  - don't buy |
| 🟩 Extreme Greed (high price) | 📈  Rising    | 📉  Low   | High price is justified - buy       |


Data:

|         Data                  |       Purpose       |      Source        |     Extraction method                     | URL / code
|-------------------------------|---------------------|--------------------|-------------------------------------------|------|
| Crypto "Fear & Greed Index"   | Crypto sentiment    | www.alternative.me | requests.get(url)                         | https://api.alternative.me/fng/
| S&P 500 Index                 | Economy indicator   | YahooFinance       | yfinance library  | yfinance.Ticker("^GSPC")|
| Monthly inflation rate        | Economy indicator   | World Bank         | requests.get(url)                         | https://api.stlouisfed.org/fred/series/observations?series_id=CPIAUCSL&api_key={}&file_type=json |


LOGIC:
1) Crypto "Fear & Greed Index" is obtained directly.
   
2) S&P 500 Index is obtained directly, but the "Rising/Falling" trend is calculated using Simple Moving Average.
   
3) Monthly inflation rate is not obtained directly. Instead, World Bank provides Consumer Price Index (CPI) for each month. Monthly inflation rate is calculated by formula:

Monthyl Inflation rate = ((Current month CPI / Previous month CPI) - 1) * 100

Then, Monthly Inflation rate is annualized by formula:

Annualized inflation = ((1 + Monthly Inflation rate / 100) ** 12 - 1) * 100

Then, Annualized inflation is compared to the Central Bank target annual inflation, which is 2%:
- if Annulized inflation > 2%, inflation is "High".
- if Annualized inflation <= 2%, inflation is "Low".


Tools:
1) Python & Pandas: API integration and data transformation.
2) PostgreSQL: data storage.
3) Streamlit: interactive dashboard.


THE CONCLUSION:

This real-time pipeline collects crypto fear&greed index and economic indicators via APIs, cleans the data, storages it in PostgreSQL, and shows the user if crypto sentiment is justified by real economy indicators, and therefore, whether it should be acted upon or not.
