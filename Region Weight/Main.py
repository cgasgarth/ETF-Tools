from ExcelTools import *
from RegionWebScraper import *

def main(fileName):
    ETFList = importFromExcel(fileName)
    

main("../Current Portfolio.xlsx")