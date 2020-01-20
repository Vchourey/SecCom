from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests
import urllib

urls = 'https://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbolCode=-10006&symbol=NIFTY&symbol=NIFTY&instrument=-&date=-&segmentLink=17&symbolCount=2&segmentLink=17'

html = requests.get(url=urls).text

supe = BeautifulSoup(html, "html.parser")


top_gain = supe.find('table', {"id": "octable"})

try:
    for row in top_gain.find_all("thead"):
        head = row.find_all(['th', 'tr'])
        for headers in head:
            cells = headers.findChildren('th')
            print(cells.string)

except:
    print(" Error occurred while extracting data")
