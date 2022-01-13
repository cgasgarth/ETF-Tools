import requests
import json
from FinClasses import *

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0"
}

def cleanHTML(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def getName(text):
    if text.find("title=") != -1:
        text = text[ (text.find("title=")+7) : -1]
        text = text[0: text.find('"')]
        return(text)
    else:
        return text
        
def getWeight(text):
    if text == "NA":
        return 0.0
    else:
        return float(text)

def getETFInfo(key):
    url = "https://www.zacks.com/funds/etf/{}/holding"
    with requests.Session() as req:
        req.headers.update(headers)
        r = req.get(url.format(key))
        print(f"Extracting: {r.url}")
        stockList = []
        for line in r.text.splitlines():
            if not line.startswith('etf_holdings.formatted_data'):
                continue
            data = json.loads(line[30:-1])
            for holding in data:
                #print(holding)
                #goal = re.search(r'<[^>]>', holding[1])
                name = getName(holding[0])
                ticker = cleanHTML(holding[1])
                weight = getWeight(cleanHTML(holding[3]))
                newStock = stock(name, ticker, weight)
                stockList.append(newStock)
            break
        return stockList

