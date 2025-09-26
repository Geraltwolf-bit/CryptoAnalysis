THE PROBLEM:

Retail investors often lose money on crypto, because they buy when the market is in a state of "greed" (prices are high) and sell when the market is in "fear" (prices are low).


THE SOLUTION:

To help people make better decisions, I built an interactive dashboard that squares the "Crypto Fear & Greed Index" with real economy indicators: S&P 500 Index (stock market health) and Inflation Rate.

The dashboard shows in real time if, for example, a recent crash is a bad time to sell or good. If S&P 500 is high and Inflation is low, economy is strong and crypto will bounce back, so that crash is a buying opportunity.

It will also show if a rising crypto is driven by real growth or somethig irrelevant, like a social media hype. If S&P 500 is low and Inflation is high, it is a bubble that is about to pop. Time to sell!

The insights provided by the dashboard:

|         Crypto Sentiment      | S&P 500 Trend | Inflation |             Interpretation              |
|-------------------------------|---------------|-----------|-----------------------------------------|
| 🟩 Extreme Fear  (low price)  | 📈  Rising     | 📉  Low   | Fear is irrational      - buy           |
| 🟥 Extreme Greed (high price) | 📉  Falling    | 📈  High  | High price is a bubble  - sell          |
| 🟥 Extreme Fear  (low price)  | 📉  Falling    | 📈  High  | Low price is justified  - don't buy     |
| 🟩 Extreme Greed (high price) | 📈  Rising     | 📉  Low   | High price is justified - buy           |

Tools:
1) Python & Pandas: API integration and data transformation.
2) PostgreSQL: data storage.
3) Tableau: interactive dashboard.

This real-time pipeline collects crypto prices and economic indicators via APIs, cleans the data, storages it in PostgreSQL, and shows the user if the change in crypto price is influenced by herd mentality (people panicking / being manipulated into overestimating a currency) or real economy changes.
