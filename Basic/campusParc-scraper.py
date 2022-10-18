from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import time

PATH = "#/chromedriver" # path of driver

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

garageOppPctDict = {}

# loop through dataFrame and get a python dictionary
for row in range(len(df)-1):
    garageOppPctDict[df.loc[row, "GARAGE / Lot"]] = int(df.loc[row, "OCCUPANCY"].rstrip("%"))

print(garageOppPctDict)

# check for duplicates and print result

unique = set()
duplicatePct = []

for pct in garageOppPctDict.values(): # for percentage in garage dictionary
    if pct in unique and pct == min(garageOppPctDict.values()): # if percentage is a duplicate and is the smallest
        duplicatePct.append(pct) # add to duplicate lsit
    else:
        unique.add(pct)


if len(duplicatePct) == 0:
    # lowest occupancy percentage
    lowestOppPct = min(garageOppPctDict.values())
    # lowest occupancy garage
    lowestOppGarage = [key for key, value in garageOppPctDict.items() if value == min(garageOppPctDict.values())] 

    print("Currently, " + str(lowestOppGarage[0]) + " has the lowest garage occupancy at " + str(lowestOppPct) + "%.")
else:
    # grab garage names with matching min values
    lowestOppGarages = [key for key, value in garageOppPctDict.items() if value == duplicatePct[0]] 
    print("Currently, " + ', '.join(lowestOppGarages) + " garages have the lowest occupancy levels at " + duplicatePct[0] + "%.")


driver.close()
