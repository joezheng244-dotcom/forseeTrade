import yfinance as yf
import matplotlib.pyplot as plt

print("Fetching stock data...")
user_input = input("Enter the stock ticker symbol (e.g., AAPL, MSFT):")
user_date = input("Enter the data range start date (YYYY-MM-DD):")
ticker = user_input.strip().upper()

df = yf.download(ticker, start=user_date)

print(df.head())
df.Close.plot()
plt.show()

# num_Days = int(input("Enter the number of days to forecast:"))
# numData = [] 

# for i in range(len(df) - num_Days):
#     numData.append(df.Close[i: i + num_Days])
# print(numData)