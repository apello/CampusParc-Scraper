from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import time

PATH = "/Users/apello/Downloads/chromedriver" # path of driver

chrome_options = Options() # chrome options
chrome_options.add_argument("--headless") # hide browser

driver = webdriver.Chrome(executable_path=PATH,
                              chrome_options=chrome_options) # create new chrome session

url = "https://osu.campusparc.com/" # campus parc website

driver.get(url) # load web page
driver.implicitly_wait(5) # wait fro page to load

# grab page source 
soup = BeautifulSoup(driver.page_source, 'lxml')

# grab tables
tables = soup.find_all('table')

# convert table to dataFrame
dfs = pd.read_html(str(tables))
df = dfs[0]

# print(f'Total tables: {len(dfs)}')
# print(dfs[0])

# parse through dataFrame and create dict

garageOppPct = {}

for row in range(len(df)-1):
    garageOppPct[df.loc[row, "GARAGE / Lot"]] = df.loc[row, "OCCUPANCY"]

# print(garageOppPct)

# find smallest value
lowestOppPct = [occupancy for garageName, occupancy in garageOppPct.items() if occupancy == min(garageOppPct.values())]
# find smallest occupancy garage name
lowestOppGarage = [garageName for garageName, occupancy in garageOppPct.items() if occupancy == min(garageOppPct.values())] 

# print(lowestOppPct)
# print(lowestOppGarage)


if len(lowestOppGarage) < 2 and len(lowestOppPct) < 2:
    print("Currently, " + str(lowestOppGarage[0]) + " has the lowest occupancy at " + str(lowestOppPct[0]) + ".")


driver.close()