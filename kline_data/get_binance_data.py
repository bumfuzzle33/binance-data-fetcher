from binance.client import Client
from rich import print
from rich.pretty import pprint
from rich.progress import track
import time
import csv

#data format 
# time,open,high,low,close,Volume,kline close time,quote asset volume,no. of trades,taker buy base asset volume,taker buy quote asset volume ,unused field(ignore)


binance_api_key = 'eZhSMpuG6pfBbYOXJv4ehNvBqVcNWv1CoFuyisrTolsppLKAxT0qDQwCz1XlLkiz'
binance_secret_key = 'hLceVc9V8cycB6XAsQjxU20fmiiTmmteezKukKvJXGb1ETuWUyQGjOGURqfxsElu'

symbol = 'ETHBUSD'
fromDate = "10 Sept, 2022"
toDate = "15 Oct, 2022"

fromDateEscaped = fromDate.replace(' ','_').replace(',','')
toDateEscaped = toDate.replace(' ','_').replace(',','')

file_path = f'/home/zoro/hahaha/backtesting/kline_data/{symbol}/5_minute/'

file_name = f'5min_ethbusd_{fromDateEscaped}_to_{toDateEscaped}.csv'





client = Client(binance_api_key,binance_secret_key)


klines = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_5MINUTE, fromDate, toDate)

csvfile = open(f'{file_path + file_name}','w',newline='')
kline_writer = csv.writer(csvfile,delimiter=',')

totalLines = len(klines)

for kline in track(klines, description='Fetching ...',):
    kline_writer.writerow(kline)



csvfile.close()
print('Finish')

