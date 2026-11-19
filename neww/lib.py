import requests
from bs4 import BeautifulSoup
import pandas as pd
url="https://www.cricbuzz.com/cricket-series/ipl-2022/auction/completed"
r=requests.get(url)
#print(r)
b=BeautifulSoup(r.text ,"html.parser")
#print(b)
head=b.find_all("div", class_='grid sticky top-0 z-[1]')
print(head)
print("_________________________________________")
header=[]
for i in head:
    name=i.text
    header.append(name)
print(header)    