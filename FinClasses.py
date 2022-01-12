class stock():
    def __init__(self, ticker, weight):
        self.ticker = ticker
        self.weight = weight
    
    def getTicker(self):
        return self.ticker
    
    def getWeight(self):
        return self.weight

class ETF():
    def __init__(self, ticker):
        self.ticker = ticker
        self.holdings = []
    
    def setHoldings(self, holdings):
        self.holdings = holdings

    def getTicker(self):
        return self.ticker
    
    def getHoldings(self):
        return self.holdings