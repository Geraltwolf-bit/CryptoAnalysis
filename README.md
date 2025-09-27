THE PROBLEM:

Retail investors often lose money on crypto, because they buy when the market is in a state of "greed" (prices are high) and sell when the market is in "fear" (prices are low).

There are a lot of sources that show the crypto "Fear & Greed Index":

https://coinmarketcap.com/charts/fear-and-greed-index/

Trouble is, Fear & Greed Index only shows people's sentiment and doesn't answer if the low/high price is justified or not.


THE SOLUTION:

To help people make better decisions, I built an interactive dashboard that squares the crypto "Fear & Greed Index" with real economy indicators: S&P 500 Index (stock market health) and inflation rate.

The dashboard shows in real time if a crash - Extreme Fear - is a bad time to sell or good. If S&P 500 is high and inflation is low, it means that economy is strong and crypto will bounce back. It's a buying opportunity!

If the price is high - Extreme Greed - but S&P 500 is low and inflation is high, it means rising crypto is driven by something irrelevant, like a social media hype, and is, in fact, a bubble that is about to pop. Time to sell!

The insights provided by the dashboard:

|         Crypto Sentiment      | S&P 500 Index  | Inflation |             Interpretation          |
|-------------------------------|----------------|-----------|-------------------------------------|
| 🟩 Extreme Fear  (low price)  | 📈  Rising     | 📉  Low   | Fear is irrational      - buy       |
| 🟥 Extreme Greed (high price) | 📉  Falling    | 📈  High  | High price is a bubble  - sell      |
| 🟥 Extreme Fear  (low price)  | 📉  Falling    | 📈  High  | Low price is justified  - don't buy |
| 🟩 Extreme Greed (high price) | 📈  Rising     | 📉  Low   | High price is justified - buy       |


Data:

|         Data                  |       Purpose       |      Source        |     Extraction method                     | URL / code
|-------------------------------|---------------------|--------------------|-------------------------------------------|------|
| Crypto "Fear & Greed Index"   | Crypto sentiment    | www.alternative.me | requests.get(url)                         | https://api.alternative.me/fng/
| S&P 500 Index                 | Economy indicator   | YahooFinance       | yfinance library: | yfinance.Ticker("^GSPC")|
| Inflation rate                | Economy indicator   | World Bank         | requests.get(url)                         | https://api.worldbank.org/v2/country/US/indicator/FP.CPI.TOTL.ZG?format=json |


Tools:
1) Python & Pandas: API integration and data transformation.
2) PostgreSQL: data storage.
3) Tableau: interactive dashboard.


THE CONCLUSION:

This real-time pipeline collects crypto fear&greed index and economic indicators via APIs, cleans the data, storages it in PostgreSQL, and shows the user if crypto sentiment is justified by real economy indicators, and therefore, whether it should be acted upon or not.
