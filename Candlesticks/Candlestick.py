

# Creates a Candlestick Object which identifys type of candlestick and 
class Candlestick(object):
	def __init__(self, open, close, low, high):
		self.open = open
		self.close = close
		self.low = low
		self.high = high
		

	def getProperties(self):
		return [self.open, self.close, self.low, self.high]

