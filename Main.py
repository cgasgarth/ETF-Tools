from ETFInfo import *
from FinClasses import *
from FinClasses import *
from ExcelTools import *
from FinTools import *

def main(fileName):
    ETFList = importFromExcel(fileName)
    for ETF in ETFList:
        holdings = getETFInfo(ETF.getTicker())
        ETF.setHoldings(holdings)
    print("----------------------------------------------------")
    print("Portfolio stock weights, printing stocks over 1%")
    stockWeights = totalWeights(ETFList)
    for stock in stockWeights:
        if stock.getWeight() > 1:
            print(stock.getTicker(), str(stock.getWeight()) + "%")



main("Current Portfolio.xlsx")