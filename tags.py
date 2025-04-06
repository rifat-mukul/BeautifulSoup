import requests
from bs4 import BeautifulSoup

with open("sample.html", "r") as f:
    html_doc = f.read()


soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify()) 

# pretify print the cointent that are in  the soup

# for printing title
print(soup.title,"  =======  " ,type(soup.title))
print("================================")

print(soup.title.string,"  =======  " ,type(soup.title.string))
print("================================")

print(soup.div)

print("================================")

# find all the same tag 
print(soup.find_all("div"))
print("================================")
print(soup.find_all("div")[0])
print("================================")
print(soup.find_all("div")[1])
print("================================")
for link in soup.find_all("a"):
    print(link)
    print("==========")
    print(link.get("href"))
    print("======end ============")
print("================================")

s = soup.find(id="link2")

print(s)
print("================================")
print(s.get("href"))
print("================================")
print(soup.select("div.italic"))
print("================================")
print(soup.select("div.italic")[1])
print("================================")
print(soup.select("span#italic"))
print("================================")
print(soup.span.get("class"))
print("================================")
print(soup.span.get("id"))
print("================================")
print(soup.find(id="italic"))
print("================================")
print(soup.find(class_="italic"))
print("================================")
print(soup.find_all(class_="italic"))
print("================================")
for child in soup.find(class_="container").children:
    print(child)
print("================================")
for parent in soup.find(class_="box").parents:
    print(parent)
    break
print("================================")
cont = soup.find(class_="container")
print(cont)
print("================================")
cont = soup.find(class_="container")
cont.name = "span"
print(cont)
print("================================")
cont = soup.find(class_="container")
cont["class"] = "myclass"
print(cont)
print("================================")
cont = soup.find(class_="myclass")
cont.string = "this is new string"
print(cont)
print("================================")
cont2 = soup.find(class_="myclass")
print(cont2.has_attr("class"))
print("================================")
cont3 = soup.find(class_="myclass")
print(cont3.has_attr("contenteditable"))
print("================================")
def has_class_not_id(tag):
    return tag.has_attr("class") and not tag.has_attr("id")

results = soup.find_all(has_class_not_id)
print(results)
print("================================")

def has_content(tag):
    return tag.has_attr("content")

results2 = soup.find_all(has_content)

for rst in results2:
    print(rst)
# print(results2)
print("================================")
print("================================")
print("================================")