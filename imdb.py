import time;
from requests_html import HTMLSession
session = HTMLSession()

r = session.get("https://www.imdb.com/chart/top?ref_=nv_mv_250")
# r.html.render()
items = r.html.find(".titleColumn a")
for item in items:
    # print(item.attrs.get("href"), item.text)

    urls = item.absolute_links
    # print(urls)
    title = item.text;
    for url in urls:
        r = session.get(url)
        content = r.html.find("#goofs", first=True)

        # print(name)
        if content:
            print(title)
            print(content.text)
            print('')

        time.sleep(0.2)
