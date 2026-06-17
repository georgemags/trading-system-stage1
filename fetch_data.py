# Loading stocks from yfinance year to date
# using trys examine data for errors including NaNs and missing dates

# importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import holidays

# stocks that are being researched
symbols = ['AAPL', 'MSFT', 'GOOGL', 'NVDA', 'RKLB', 'AMD', 'JPM', 'AVGO', 'META', 'TSM']

# for loop that pulls the stock data as well as checks for NaN in dataset and checks for missing business dates (excluding weekends and US holidays)

for symbol in symbols:
    try:
        stock_data = yf.download(symbol, period='1y')
        nan_count = pd.isnull(stock_data['Close'][symbol]).sum()
        start_date = stock_data.index.min()
        end_date = stock_data.index.max()
        all_weekdays = pd.bdate_range(start=start_date, end=end_date)
        us_holidays = holidays.US(years=[start_date.year, end_date.year])
        valid_business_days = all_weekdays.difference(pd.to_datetime(list(us_holidays.keys())))
        missing_dates = valid_business_days.difference(stock_data.index)
        missing_dates_list = missing_dates.strftime('%Y-%m-%d').tolist()
        

        stock_data['daily_return'] = stock_data['Close'].pct_change() * 100
        stock_data.to_csv(f'{symbol}_data.csv')
        print(f"Saved {symbol} data")
        
        if nan_count > 0:
            print(f'There are {nan_count} missing values in close column')
        print(f'Missing Business Dates: {missing_dates_list}')
    except Exception as e:
        print(f"Failed to download {symbol}: {e}")
