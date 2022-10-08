from bs4 import BeautifulSoup # scraps html
import requests # connects to web pages

# open index.html in read mode as file (f)
with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser") # parse index as html

# tag = doc.find("a") # links
# # tag.string <- access content
# tag.string = "hello" # change content of tags
# tags = doc.find_all("p") # find all tags 

# # ---- nested tag
# tag = doc.find_all("p")[1]

# ---- access web page online
url = "https://www.newegg.com/tp-link-archer-tx3000e-pci-express/p/N82E16833704507?Item=N82E16833704507&cm_sp=Homepage_SS-_-P0_33-704-507-_-10082022" # website we want to access

result = requests.get(url) #sends http request, returns page content
doc = BeautifulSoup(result.text, "html.parser")
# print(doc.prettify())

prices = doc.find_all(text="$") # find dollar signs on page
parent = prices[0].parent # find parent of dollar sign 
strong = parent.find("strong")
print(strong.string)
#print(parent)

