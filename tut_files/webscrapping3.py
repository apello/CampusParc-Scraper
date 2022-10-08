from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

tbody = doc.tbody # get tbody tag on website
tr_tags = tbody.contents # get content of tbody

# basic traversing:
    # tr_tags[0].parent.name
    # tr_tags[0].descendants -> gives all children in other tag
    #  tr_tags[0].children
    # tr_tags[0].next_sibling
    # tr_tags[1].previous_sibling
    # tr_tags[0].next_siblings
    # list(tr_tags[0].next_siblings)

prices = {}

for tr in tr_tags[:10]: # first 10 table rows
    name,price = tr.contents[2:4] # specific indexes of content
    fixed_name = name.p.string
    fixed_price = price.a.string

    prices[fixed_name] = fixed_price

print(prices)