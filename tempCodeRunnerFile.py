print(soup.title,"  =======  " ,type(soup.title))
# print("================================")

# print(soup.title.string,"  =======  " ,type(soup.title.string))
# print("================================")

# print(soup.div)

# print("================================")

# # find all the same tag 
# print(soup.find_all("div"))
# print("================================")
# print(soup.find_all("div")[0])
# print("================================")
# print(soup.find_all("div")[1])
# print("================================")
# for link in soup.find_all("a"):
#     print(link)
#     print("==========")
#     print(link.get("href"))
#     print("======end ============")
# print("================================")

# s = soup.find(id="link2")

# print(s)
# print("================================")
# print(s.get("href"))
# print("================================")
# print(soup.select("div.italic"))
# print("================================")
# print(soup.select("div.italic")[1])
# print("================================")
# print(soup.select("span#italic"))
# print("================================")
# print(soup.span.get("class"))
# print("================================")
# print(soup.span.get("id"))
# print("================================")
# print(soup.find(id="italic"))
# print("================================")
# print(soup.find(class_="italic"))
# print("================================")
# print(soup.find_all(class_="italic"))
# print("================================")
# for child in soup.find(class_="container").children:
#     print(child)
# print("================================")
# for parent in soup.find(class_="box").parents:
#     print(parent)
#     break
# print("================================")
# cont = soup.find(class_="container")
# print(cont)
# print("================================")
# cont = soup.find(class_="container")
# cont.name = "span"
# print(cont)
# print("================================")
# cont = soup.find(class_="container")
# cont["class"] = "myclass"
# print(cont)
# print("================================")
# cont = soup.find(class_="myclass")
# cont.string = "this is new string"
# print(cont)