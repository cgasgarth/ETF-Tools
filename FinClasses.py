class stock():
    def __init__(self, name, ticker, weight):
        self.name = name
        self.ticker = ticker
        self.weight = weight
    
    def getTicker(self):
        return self.ticker
    
    def getWeight(self):
        return self.weight
    
    def getName(self):
        return self.name

class ETF():
    def __init__(self, ticker, weight):
        self.ticker = ticker
        self.weighting = weight
        self.holdings = []
    
    def setHoldings(self, holdings):
        self.holdings = holdings

    def getTicker(self):
        return self.ticker
    
    def getHoldings(self):
        return self.holdings