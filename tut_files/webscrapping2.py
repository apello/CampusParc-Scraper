from bs4 import BeautifulSoup
import requests

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

tag = doc.find("option")
print(tag.attrs) #print tag attributes

tags = doc.find_all(["p", "div", "option"]) # find multiple tags
print(tags)

# find tags with specific values, content
specific_tag = doc.find_all(["option"], text="Undergraduate", value="undergraduate") 
print(specific_tag)

# find tags with specific classes
class_tag = doc.find_all(class_="btn-item") 
print(class_tag)

# # grab all words after character using regular expression
# # regular_expression = doc.find_all(text=re.compile("\$.*")) 
# # print(regular_expression) 

 
#  # find tags with specific values, content
# limit_tag = doc.find_all("option", limit=2) 
# print(limit_tag)

# # save modified html
# modified_tag = doc.find_all("input", type="text")
# for tag in modified_tag:
#     tag["placeholder"] = "Change"

# with open("changed.html", "w") as file: # create file as write
#     file.write(str(doc)) # write to file