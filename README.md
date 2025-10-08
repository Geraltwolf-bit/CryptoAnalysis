THE PROBLEM:

People often lose money on crypto, because they follow the crypto Fear & Greed Index:

![Crypto Fear & Greed Index](images/dashboard.png)


It assumes that Fear is an undervalued market and buying opportunity, while Greed means crypto market is a bubble. The message is clear and easy to follow, the only problem is that it is often wrong.

Not every crash is a buying opportunity and not every raise is a bubble. But Fear & Greed Index can't tell that, because it's based on crypto price, Google searches, and social media hype and doesn't take into account real economy indicators, like inflation and stock market. That is why it is so unreliable and people lose so big.


THE SOLUTION:

To help people make better decisions, I built an interactive dashboard that squares the crypto Fear & Greed Index with real economy indicators: S&P 500 Index (stock market value) and inflation rate.

The dashboard shows in real time if Index is justified or not.

For example:

- If Fear goes along stock market crash and inflation is high, buying is not recommended. But if stock market is rising and inflation is low, Fear is indeed a buying opportunity. Buy now!
- If Greed goes along rising stock market and inflation is low, it's safe to buy. But if stock market is falling and inflation is high, Greed is a bubble. Time to sell!

THE INSIGHTS:

|    Crypto Sentiment   | S&P 500 Index  | Inflation |  Insight    |
|-----------------------|----------------|-----------|-------------|
| 🟩 Fear  (low price)  | 📈  Rising    | 📉  Low   | Buy now!    |
| 🟥 Fear  (low price)  | 📉  Falling   | 📈  High  | Don't buy!  |
| 🟩 Greed (high price) | 📈  Rising    | 📉  Low   | Safe to buy |
| 🟥 Greed (high price) | 📉  Falling   | 📈  High  | Sell now!   |


THE DATA:

|         Data                  |       Purpose       |      Source        |     Extraction method                     | URL / code
|-------------------------------|---------------------|--------------------|-------------------------------------------|------|
| Crypto "Fear & Greed Index"   | Crypto sentiment    | www.alternative.me | requests.get(url)                         | https://api.alternative.me/fng/
| S&P 500 Index                 | Economy indicator   | YahooFinance       | yfinance library  | yfinance.Ticker("^GSPC")|
| Monthly inflation rate        | Economy indicator   | World Bank         | requests.get(url)                         | https://api.stlouisfed.org/fred/series/observations?series_id=CPIAUCSL&api_key={}&file_type=json |


THE LOGIC:
1) Crypto "Fear & Greed Index" is obtained directly.
   
2) S&P 500 Index is obtained directly, but this data is noisy. To smooth the noise, I use Simple Moving Average to calculate the "Rising/Falling" trend.
   
3) Monthly inflation rate is not obtained directly. Instead, World Bank provides Consumer Price Index (CPI) for each month.

Monthly inflation rate is calculated by formula:
- Monthyl Inflation rate = ((Current month CPI / Previous month CPI) - 1) * 100

Then, Monthly Inflation rate is annualized by formula:
- Annualized inflation = ((1 + Monthly Inflation rate / 100) ** 12 - 1) * 100

To find if Annualized inflation is "High", "Moderate", or "Low", I compare it to the Central Bank target annual inflation, which is 2%:
- if Annulized inflation <= 2%, inflation is "Low".
- if Annulized inflation <= 5%, inflation is "Moderate".
- if Annualized inflation > 5%, inflation is "High".


THE TOOLS:
1) Python & Pandas: API integration and data transformation.
2) Docker & PostgreSQL: data storage.
3) Streamlit: interactive dashboard.


THE CONCLUSION:

This real-time pipeline collects data via APIs, analyses it, and shows the user if the crypto Fear & Greed Index is justified by real economy indicators, and therefore, whether it should be acted upon or not.
