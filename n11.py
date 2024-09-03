#BeautifulSoup ile n11den verileri çekme

import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"


headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

html = requests.get(url, headers=headers).content
soup = BeautifulSoup(html, "html.parser")


liste = soup.find_all("li", {"class":"column"}, limit=10)

count = 1
for li in liste:
    link = li.a.get("href")
    p_name = li.a.h3.text
    price = li.find("div",  {"class":"priceContainer"}).find_all("span")[-1].ins.text.strip("TL")

    print(f"{count}. ürün ismi {p_name} fiyat : {price}")
    count += 1