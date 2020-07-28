import IdentifyTrend as trend
from Candlestick import Candlestick
import requests
from datetime import datetime

candles = requests.get('https://finnhub.io/api/v1/stock/candle?symbol=GOOGL&resolution=1&from=1595597400&to=1595620800&token=bseji3frh5rdgbcj0dk0').json()
	
if (candles['s'] != 'no_data'):
	for i in range(len(candles["c"])-3):
		print ("Candlestick At Time: " + datetime.fromtimestamp(candles["t"][i]).strftime('%Y-%m-%d %H:%M:%S')	) 
		candlestick1 = Candlestick(candles["o"][i],candles["c"][i],candles["l"][i],candles["h"][i])
		candlestick2 = Candlestick(candles["o"][i+1],candles["c"][i+1],candles["l"][i+1],candles["h"][i+1])
		candlestick3 = Candlestick(candles["o"][i+2],candles["c"][i+2],candles["l"][i+2],candles["h"][i+2])
		candlestick4 = Candlestick(candles["o"][i+3],candles["c"][i+3],candles["l"][i+3],candles["h"][i+3])

		if (candlestick4):
			trend.identifyAll(candlestick1, candlestick2 = candlestick2, candlestick3 = candlestick3, candlestick4 = candlestick4)
		if (candlestick3):
			trend.identifyAll(candlestick1, candlestick2 = candlestick2, candlestick3 = candlestick3)
		if (candlestick2):
			trend.identifyAll(candlestick1, candlestick2 = candlestick2)
		if (candlestick1):
			trend.identifyAll(candlestick1)





