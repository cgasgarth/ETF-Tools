class stock():
    def __init__(self, name, ticker, weight):
        self.name = name
        self.ticker = ticker
        self.weight = weight
    
    def getTicker(self):
        return self.ticker
    
    def getWeight(self):
        return self.weight
    
    def setWeight(self, weight):
        self.weight = weight

    def getName(self):
        return self.name

class ETF():
    def __init__(self, ticker, weight):
        self.ticker = ticker
        self.weight = weight
        self.holdings = []
    
    def setHoldings(self, holdings):
        self.holdings = holdings

    def getTicker(self):
        return self.ticker
    
    def getWeight(self):
        return self.weight

    def getHoldings(self):
        return self.holdings