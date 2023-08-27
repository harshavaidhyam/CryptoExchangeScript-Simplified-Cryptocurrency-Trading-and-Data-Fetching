import ccxt
import ta
import schedule
import pandas as pd
import time
import bybit

# Initialize the Bybit exchange instance
exchange_id = 'bybit'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': 'YOUR_API_KEY',    # Replace with your actual API key
    'secret': 'YOUR_API_SECRET'  # Replace with your actual API secret
})

# Fetch and display the order book for ETH/USD
orderbook = exchange.fetch_order_book('ETH/USD')
print("Order Book for ETH/USD:")
print(orderbook)

# Fetch and display the account balance for ETH
balance = exchange.fetch_balance()
print("\nAccount Balance:")
print("ETH Balance:", balance['total']['ETH'])

# Schedule data fetching using the schedule library
def fetchData():
    print("\nFetching OHLCV Data")
    bars = exchange.fetch_ohlcv('BTC/USD', timeframe='1m', limit=8)
    df = pd.DataFrame(bars[:-1], columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    print(df)

# Schedule data fetching at regular intervals
schedule.every().seconds.do(fetchData)
while True:
    schedule.run_pending()
    time.sleep(3)


# Place a market buy order for ETH/USD
print("\nPlacing Market Buy Order for ETH/USD")
order = exchange.create_market_buy_order('ETH/USD', 0.00007)
print("Order Placed:", order)

# Initialize the Bybit API client
client = bybit.bybit(test=True, api_key="mRTGtG2rvXph3Cpew8", api_secret="ZaihafeWFHaVx2quEZ9TGLSf5IoH6iHBo9d8")


# Set leverage for the BTCUSD trading pair
print("\nSetting Leverage for BTCUSD")
print(client.Positions.Positions_saveLeverage(symbol="BTCUSD", leverage="14").result())


# Place a market sell order for the ETHUSD trading pair
print("\nPlacing Market Sell Order for ETHUSD")
print(client.Order.Order_new(side="Sell", symbol="ETHUSD", order_type="Market", qty=0.0446, time_in_force="GoodTillCancel").result())


