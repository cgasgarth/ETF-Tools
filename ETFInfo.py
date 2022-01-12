import requests
import json
import re
from pprint import pprint
from FinClasses import *

keys = ['SMH']


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0"
}


def getETFInfo(key):
    url = "https://www.zacks.com/funds/etf/{}/holding"
    tickAndWeight = []
    with requests.Session() as req:
        req.headers.update(headers)
        r = req.get(url.format(key))
        print(f"Extracting: {r.url}")
        for line in r.text.splitlines():
            if not line.startswith('etf_holdings.formatted_data'):
                continue
            data = json.loads(line[30:-1])
            for holding in data:
                goal = re.search(r'etf/([^"]*)', holding[1])
                if goal:
                    #print(goal.group(1))
                    #print(float(holding[3]))
                    newStock = stock(goal.group(1), float(holding[3]))
                    tickAndWeight.append(newStock)
            break
    return tickAndWeight

