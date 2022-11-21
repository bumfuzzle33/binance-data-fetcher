from binance.client import Client
from rich import print
from rich.pretty import pprint
from rich.progress import track
import time
import csv
from dotenv import dotenv_values

#data format 
# time,open,high,low,close,Volume,kline close time,quote asset volume,no. of trades,taker buy base asset volume,taker buy quote asset volume ,unused field(ignore)

config = dotenv_values(".env")

binance_api_key = config['BINANCE_API_KEY']
binance_secret_key = config['BINANCE_SECRET_KEY']

symbol = 'BTCBUSD'
fromDate = "1 Aug, 2022"
toDate = "1 Nov, 2022"
timeFrame = '5_minute'

fromDateEscaped = fromDate.replace(' ','_').replace(',','')
toDateEscaped = toDate.replace(' ','_').replace(',','')

file_path = f'/home/zoro/hahaha/backtesting/kline_data/{symbol}/{timeFrame}/'

file_name = f'{timeFrame}_btcbusd_{fromDateEscaped}_to_{toDateEscaped}.csv'





client = Client(binance_api_key,binance_secret_key)


klines = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_5MINUTE, fromDate, toDate)

csvfile = open(f'{file_path + file_name}','w',newline='')
kline_writer = csv.writer(csvfile,delimiter=',')

totalLines = len(klines)

for kline in track(klines, description='Fetching ...',):
    kline_writer.writerow(kline)



csvfile.close()
print('Finish')

