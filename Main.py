from ETFInfo import *
from FinClasses import *
from FinClasses import *
from ExcelTools import *

def main(fileName):
    etfList = importFromExcel(fileName)
    for etf in etfList:
        holdings = getETFInfo(etf.getTicker())
        etf.setHoldings(holdings)
    for etf in etfList:
        weight = 0.0
        for stock in etf.getHoldings():
            weight += stock.getWeight()
        print(etf.getTicker(), weight)
        print("--------------------------")


main("Current Portfolio.xlsx")