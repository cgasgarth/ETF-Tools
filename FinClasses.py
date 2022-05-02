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
        self.jsonList = []
    
    def setHoldings(self, holdings):
        self.holdings = holdings

    def getTicker(self):
        return self.ticker
    
    def getWeight(self):
        return self.weight

    def getHoldings(self):
        return self.holdings
    

    def setJsonList(self, jsonList):
        self.jsonList = jsonList
    
    def getJsonList(self):
        return self.jsonList
    
    def getRegionJSON(self):
        return self.jsonList[0]
    
    def getCountryJSON(self):
        return self.jsonList[1]
    
    def getSectorJSON(self):
        return self.jsonList[2]
    
    def getMarketCapJSON(self):
        return self.jsonList[3]
    


    #override print function
    def __str__(self):
        return self.ticker