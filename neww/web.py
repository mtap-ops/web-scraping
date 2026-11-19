import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com/courses/the-ultimate-content-creator-bootcamp?gad_source=1&gad_campaignid=24356436165&gbraid=0AAAAAqQsM_2GlEW5SjZd6q_ceFv0AqcsN&gclid=CjwKCAjwi-zWBhAdEiwAqlRf-Gq0A3qM6VLBFZso9vcHZ2JR2NQ9hihqJgO0aFInMShoET8FYyI2zxoChhIQAvD_BwE"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36"}

r=requests.get(url)
print(r.content)
print(r.status_code)

b=BeautifulSoup(r.content , "html.parser")
print(b.prettify())
print("-----------------------")

data1=b.find("p", class_ = "text-xl text-zinc-300 dark:text-zinc-400 leading-relaxed max-w-3xl")
print(data1)
print("-----------------------")
c=data1.get_text(" ", strip=True)
print(c)
print("-----------------------") 
a=b.find("ul" , class_="list-disc pl-6 space-y-3 text-foreground dark:text-foreground marker:text-primary")
print(a)
print(a.find_all("p"))
print("-----------------------") 
print(a.find_all("li"))
print("-----------------------") 
for l1 in a:
    print(l1.text)
print("-----------------------")     
print(len(list(a.children)))   # tells abt child
print("-----------------------") 
#print(b.find_all("a"))
#print("-----------------------") 
for i in b.find_all("a"):               #to get link 
    print(i)
print("-----------------------")     
for i in b.find_all("a"):
    print(i.get("href"))
print("-----------------------")    
img=b.find_all("img")                          # to get image
print(img)    
print("-----------------------")              
for i1 in img:
    print(i1.get("src"))
print("-----------------------")        
print(type(i1.get("src")))
print("-----------------------") 
for i1 in img:
    print(i1.get("alt"))   
