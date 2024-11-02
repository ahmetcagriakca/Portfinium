from abc import ABC, abstractmethod
import pandas as pd
import yfinance as yf

# Mapping of asset codes to ticker symbols
TICKER_MAP = {
    "GOLD": "GC=F",
    "SILVER": "SI=F"
}

# Helper function to get ticker symbol for an asset
def get_ticker_symbol(asset):
    if asset.startswith("IST:"):
        return asset.replace("IST:", "") + ".IS"
    elif asset.startswith("CURRENCY:"):
        return asset.replace("CURRENCY:", "") + "=X"
    return TICKER_MAP.get(asset)

# Strategy Pattern for fetching stock data
class StockDataStrategy(ABC):
    @abstractmethod
    def get_data(self, asset, date):
        pass

class YahooFinanceStockDataStrategy(StockDataStrategy):
    def get_data(self, asset, date):
        ticker = get_ticker_symbol(asset)
        if not ticker:
            print(f"Invalid asset code: {asset}")
            return None
        try:
            stock = yf.Ticker(ticker)
            date_obj = pd.to_datetime(date, format='%d-%m-%Y')
            data = stock.history(start=date_obj, end=date_obj + pd.Timedelta(days=1))
            if data.empty:
                print(f"No data available for asset {asset} on {date}")
                return None
            return data
        except Exception as e:
            print(f"Error fetching data for {asset} on {date}: {e}")
            return None

# Strategy Pattern for fetching asset price
class PriceStrategy(ABC):
    @abstractmethod
    def get_price(self, asset, date):
        pass

class StockPriceStrategy(PriceStrategy):
    def __init__(self, stock_data_strategy: StockDataStrategy):
        self.stock_data_strategy = stock_data_strategy

    def get_price(self, asset, date):
        data = self.stock_data_strategy.get_data(asset, date)
        if data is None:
            return 0
        return data.iloc[0]["Close"]

class PreciousMetalPriceStrategy(PriceStrategy):
    def __init__(self, stock_data_strategy: StockDataStrategy):
        self.stock_data_strategy = stock_data_strategy

    def get_price(self, asset, date):
        spot_price = StockPriceStrategy(self.stock_data_strategy).get_price(asset, date)
        if spot_price == 0:
            return 0
        usd_price = StockPriceStrategy(self.stock_data_strategy).get_price("CURRENCY:USDTRY", date)
        if usd_price == 0:
            print(f"Failed to fetch USD/TRY exchange rate for asset {asset}.")
            return 0
        return (spot_price / 31.1035) * usd_price

# Context class to use the appropriate strategy
class PriceContext:
    def __init__(self, strategy: PriceStrategy):
        self._strategy = strategy

    def get_price(self, asset, date):
        return self._strategy.get_price(asset, date)

# Function to get asset price at a given date
def get_price_at_date(asset, date):
    stock_data_strategy = YahooFinanceStockDataStrategy()
    if asset in ["GOLD", "SILVER"]:
        strategy = PreciousMetalPriceStrategy(stock_data_strategy)
    else:
        strategy = StockPriceStrategy(stock_data_strategy)
    context = PriceContext(strategy)
    return context.get_price(asset, date)
