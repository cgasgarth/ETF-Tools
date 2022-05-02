from ETFDBScraper import *
import os, inspect, sys
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 
from ExcelTools import *
from FinClasses import *


def main(fileName):
    ETFs = importFromExcel(fileName)
    for ETF in ETFs:
        jsonList = getJSONS(ETF.getTicker())
        ETF.setJsonList(jsonList)
    for json in ETFs[0].getJsonList():
        print(json)

main("../Current Portfolio.xlsx")