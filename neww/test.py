import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.cricbuzz.com/cricket-series/ipl-2022/auction/completed"
r = requests.get(url)
b = BeautifulSoup(r.text, "html.parser")

row = b.find_all("div", class_="grid group cursor-pointer transition-colors duration-200 ease-out hover:bg-[#FAFAFA]")

data = []
for i in row:
    cells = [div.text.strip() for div in i.find_all("div")]
    print("________________________")
    print(cells)
    if len(cells) < 11:
        continue
    print("________________________")
    print(list(enumerate(cells)))

    role_country = cells[5].split("•")
    data.append({
        "Player": cells[3],
        "Role": role_country[0].strip(),
        "Country": role_country[1].strip() if len(role_country) > 1 else "",
        "Status": cells[7],
        "Base Price": cells[8],
        "Final Price": cells[9],
        "Team": cells[10],
    })
print("_____________________________________")
df = pd.DataFrame(data)
print(df.head(10))
