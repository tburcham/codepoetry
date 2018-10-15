import time
from requests_html import HTMLSession
session = HTMLSession()

r = session.get("https://newyork.craigslist.org/d/free-stuff/search/zip")

# print(r.html.text)

for html in r.html:

    titles = html.find(".result-title")

    for title in titles:

        url = title.attrs.get("href")
        # name = title.text

        # r = session.get(url)
        # content = r.html.find("#postingbody", first=True)
        #
        # print(name)
        # if content:
        #     print(content.text)
        #
        # time.sleep(0.2)

        print(title.text)
