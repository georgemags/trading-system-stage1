# Trading System Stage 1: Data Pipeline

## Overview
A Python script that fetches historical stock data from yfinance, calculates daily returns, and validates data quality.

## What It Does
- Downloads 1 year of daily OHLCV (Open, High, Low, Close, Volume) data for 10 stocks
- Calculates daily percentage returns
- Validates data for missing values (NaN) in Close prices
- Checks for missing trading dates (excluding weekends and US holidays)
- Saves clean data to CSV files

## Stocks Included
AAPL, MSFT, GOOGL, NVDA, RKLB, AMD, JPM, AVGO, META, TSM

## Requirements
pandas
yfinance
holidays
matplotlib

## Installation
```bash
pip install pandas yfinance holidays matplotlib
```

## Usage
```bash
python fetch_data.py
```

The script will:
1. Download data for each stock
2. Print validation results (NaN count, missing dates)
3. Save each stock's data as `{SYMBOL}_data.csv`

## Output Files
- `AAPL_data.csv`, `MSFT_data.csv`, etc. - Stock data with Close, High, Low, Open, Volume, and daily_return columns

## Error Handling
If a stock fails to download, the script logs the error and continues with the next stock.
