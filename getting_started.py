from backtesting import Backtest, Strategy
from backtesting.test import GOOG
import pandas as pd
from backtesting.lib import crossover
import talib
import os

getKlineFileNames = False
symbol = 'BTCBUSD'
if getKlineFileNames:
    path = './kline_data'
    for (root, dirs, file) in os.walk(path):
        for f in file:
            print(f)

#path to binance csv data
binanceCSVData = './kline_data/BTCBUSD/5_minute/5_minute_btcbusd_1_Aug_2022_to_1_Nov_2022.csv'

#column names for setting it to dataframe headers
columnNames = ['Kline_open', 'Open', 'High', 'Low', 'Close', 'Volume', 'Kline_close', 'Quote_asset_volume', 'Number_of_trades',
               'Taker_buy_base_asset_volume', 'Take_buy_quote_asset_volume', 'ignore']

#setting column names to dataframe while reading csv data
df = pd.read_csv(binanceCSVData, names=columnNames, header=None, parse_dates=True)

#converting unix time stamp in first column to datetime
df['Kline_open'] = pd.to_datetime(df['Kline_open'], unit='ms')

#setting the date time as the index column
df.set_index('Kline_open', inplace=True)

class RsiOcillator(Strategy):
    upper_bound = 70
    lower_bound = 30

    def init(self):
        self.rsi = self.I(talib.RSI, self.data.Close, 14)

    def next(self):
        if crossover(self.rsi, self.upper_bound):
            self.position.close()

        elif crossover(self.lower_bound, self.rsi):
            self.buy()


#binance commision Fee = 0.040%
#To convert it to value to be used by Backtest we divide Fee by 100

commisionValue = 0.040 / 100
leverage = 0
money = 10_000

# isStop = False
isStop = False

if(not isStop):
    bt = Backtest(df, RsiOcillator, cash=money, commission=commisionValue)

    stats = bt.run()
    print(stats)

    bt.plot()

# print (df)





















