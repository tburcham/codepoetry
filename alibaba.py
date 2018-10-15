from requests_html import HTMLSession
session = HTMLSession()

r = session.get("https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=drugs")

# for html in r.html:
items = r.html.find(".item-content")
for item in items:
    price = item.find(".price", first=True).text
    title = item.find(".title", first=True).text

    print(title, ":", price)
