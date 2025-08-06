import yfinance as yf

def fetch_prices(ticker, start, end):
    data = yf.download(ticker, start=start, end=end)
    return data