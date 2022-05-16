import sys

sys.path.insert(0, "../SharedTools")
from FinClasses import *


def sortByWeight(stockList): #sort the stocklist by weighting of the stock
    # Traverse through 1 to len(arr)
    for i in range(1, len(stockList)):
        key = stockList[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key.getWeight() < stockList[j].getWeight():
                stockList[j+1] = stockList[j]
                j -= 1
        stockList[j+1] = key

def addStock(newStock, stockList, ETFWeight): #add stock to stocklist, account if stock
    for stock in stockList: #already exists
        if newStock.getTicker() == stock.getTicker():
            stock.setWeight(stock.getWeight() + newStock.getWeight() * ETFWeight)
            return
    newStock.setWeight(newStock.getWeight() * ETFWeight)
    stockList.append(newStock)

def totalWeights(ETFList): #returns a list of stocks with the weighting of each being the 
    stockList = [] #weighting in the entire portfolio
    for ETF in ETFList:
        ETFWeight = ETF.getWeight()
        for stock in ETF.getHoldings():
            addStock(stock, stockList, ETFWeight)
    sortByWeight(stockList)
    return stockList

def getNumHoldings(ETFList): 
    stockList = []
    for ETF in ETFList:
        for stock in ETF.getHoldings():
            stockList.append(stock.getTicker())
    return len(set(stockList)) #convert to set to make unqiue
