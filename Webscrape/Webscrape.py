#her henter man html fil lokalt
"""
from bs4 import BeautifulSoup
import requests

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

#print(doc.prettify())


#her henter man spesifikke tags 

tag = doc.title 
#tag.string = "hello" #endrer ting i dokumentet
print(tag.string)

tags = doc.find_all("p")
print(tags)
"""

#Lese html fra en webside

from bs4 import BeautifulSoup
import requests

url = "https://www.coreyms.com"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

print(doc.prettify())


