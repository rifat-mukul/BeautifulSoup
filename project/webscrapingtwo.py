import requests

from bs4 import BeautifulSoup

import pandas as pd


url = "https://www.amazon.in/s?k=iphone&crid=E9N0MWVB5SLU&sprefix=iphon%2Caps%2C406&ref=nb_sb_noss_2"
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux Mint; rv:109.0) Gecko/20100101 Firefox/117.0'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# print(soup.prettify())
soup.prettify()

# spans = soup.find(class_="a-size-medium")
# print(spans)

data = {"title":[], "price":[]}

spans = soup.select("h2.a-size-medium.a-spacing-none.a-color-base.a-text-normal span")
prices = soup.select("span.a-price")


for i, span in enumerate(spans, 1):
    # print(f"{i} === {span.string}")
    data["title"].append(span.string)
print("==========================")


for i, price in enumerate(prices, 1):
    if not ("a-text-price") in price.get("class"):
        x = price.find("span").get_text()
        # print(f"{i} ==== {x}")

        data["price"].append(x)

print("================================")

df = pd.DataFrame.from_dict(data)
df.to_csv("data.csv")


