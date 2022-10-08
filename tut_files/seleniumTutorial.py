from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

PATH = "/Users/apello/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.techwithtim.net/")
print(driver.title) # title of website

# print(driver.page_source)

search = driver.find_element("name","s") # find element
search.send_keys("test") #type in search bar
search.send_keys(Keys.RETURN)

main = WebDriverWait(driver, timeout=10).until(
    lambda d: d.find_element(By.ID, "main")
)

articles = main.find_elements(By.TAG_NAME, "article")

for article in articles:
    header = article.find_element(By.CLASS_NAME, "entry-summary")
    print(header.text)

# print(main.text)

# driver.close() -> closes tab
driver.quit() # closes brower