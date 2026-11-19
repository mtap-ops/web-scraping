import requests
from bs4 import BeautifulSoup
url="https://webscraper.io/test-sites/load-more"
r=requests.get(url)
print(r)
b=BeautifulSoup(r.text ,"lxml")
#print(b)
print("________________________________")
boxes= b.find_all("div",class_="card-body")
print (boxes)
print("________________________________")
print (len(boxes))
print("________________________________")
name=b.find_all("h3", class_='card-title mt-3 mb-0')
print(name)
print("________________________________")
for i in name:
    print(i.text)
print("________________________________")  
price=b.find_all("p", class_='price col-6 mb-0 text-end p-0')
print(price)
print("________________________________")  
for i in price:
    print(i.text)
print("________________________________")  
