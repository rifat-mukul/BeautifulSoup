import requests

from bs4 import BeautifulSoup


url = "https://www.ryans.com/category/all-laptop-apple"
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux Mint; rv:109.0) Gecko/20100101 Firefox/117.0'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

soup.prettify()

# card_text = soup.find_all(class_= "card-text") 

# print(card_text)
# for i, item in enumerate(card_text, 1):
#     name = item.get_text(strip=True)
#     print(f"{i}. {name}")

products = soup.select("p.card-text a")

for i, tag in enumerate(products, 1):
    title = tag.get('title')
    if title:
        print(f"{i}. {title}")

print("====================================")

# price_tag = soup.select("a.pr-text.cat-sp-text.pb-1.text-dark.text-decoration-none")

# for price in price_tag:
#     print(print.string)

cards = soup.select("div.card.h-100")

# for i, card in enumerate(cards, 1):


#     price_tag = card.select_one("a.pr-text.cat-sp-text.pb-1.text-dark.text-decoration-none")
#     price = price_tag.text.strip()


#     # print(f"{i}  🖥️ {model}\n")
#     print(f"---- 💰 Price:  {price}")