import requests

def fetchAndSaveToFile(url, path):
    r = requests.get(url)

    with open(path, "w") as f:
        f.write(r.text)

url = "https://www.tbsnews.net/economy"

fetchAndSaveToFile(url, "data/tbsEconomy.html")

# r = requests.get(url)

# print(r.text)