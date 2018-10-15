import time;
import datetime;
from requests_html import HTMLSession
session = HTMLSession()




def download_file(url, filename):
    local_filename = filename #url.split('/')[-1]
    local_filename = "".join([c for c in local_filename if c.isalpha() or c.isdigit() or c==' ']).rstrip()

    if url.find("http") > -1:

        # print(url.find(".jpg"))

        fileformat = ""
        if url.find(".jpg") > 0 or url.find("jpeg") > 0:
            fileformat = ".jpg"
        elif url.find(".png") > 0 or url.find(" png") > 0:
            fileformat = ".png"


        r = session.get(url, stream=True)
        with open("images/" + local_filename + fileformat, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)

    return local_filename





# r = session.get("https://www.amazon.com/s/ref=nb_sb_ss_i_4_6?url=search-alias%3Daps&field-keywords=plan+b+pill+emergency+contraceptive&sprefix=plan+b%2Caps%2C148&crid=1M2H2XRPGZ7DS")
#
#
# for html in r.html:
#     items = html.find(".s-item-container")
#
#     for item in items:
#
#         # print(item.html)
#
#         if item.find("h2"):
#             title = item.find("h2", first=True).text
#             imgsrc = item.find("img.s-access-image", first=True).attrs.get("src")
#
#
#
#             print(title, imgsrc)
#
#             filepath = download_file(imgsrc, title)

r = session.get("https://www.bing.com/images/search?q=birth+control+pills&FORM=HDRSC2")

for html in r.html:
    items = html.find(".iuscp")

    for item in items:

        # print(item.html)
        img = item.find("img.mimg", first=True)
        titleEl = item.find(".infnmpt ul li:nth-child(2)", first=True)
        filetype = item.find(".infnmpt ul li:nth-child(1)", first=True)

        if titleEl != None:
            title = titleEl.text + "_" + str(datetime.datetime.now()).split('.')[0]
        else:
            title = ""
        #mmComponent_images_1 > ul:nth-child(1) > li:nth-child(2) > div > div.infopt > div > div.infpd.hoff > ul > li:nth-child(2)

        # print(title)

        if img != None and title != None:
            # title = item.find("h2", first=True).text

            imgsrc = img.attrs.get("src")
            if (imgsrc == None):
                imgsrc = img.attrs.get("data-src")
            # title = img.attrs.get("alt")

            # print(title, imgsrc)
            if filetype != None:
                imgsrc += "&___f=" + filetype.text


            if imgsrc != None and imgsrc.find("http") > -1:
                print(title, imgsrc)

                filepath = download_file(imgsrc, title)


# r = session.get("https://www.google.com/search?q=contraceptiive+pill&tbm=isch&source=lnms&sa=X&ved=0ahUKEwiHjeqD5fXdAhWqUt8KHfKYCCE4FBD8BQiVAigB&biw=1694&bih=935")
# r.html.render()
# items = r.html.find(".rg_bx")
# for item in items:
#     # print(item.attrs.get("href"), item.text)
#
#     # urls = item.absolute_links
#     # print(urls)
#     title = item.find('a.iKjWAf', first=True).find('.mVDMnf', first=True).text;
#     # print(title);
#
#     imgpath = item.find('a.rg_l', first=True).attrs.get('href');
#     s = session.get("https://www.google.com/" + imgpath);
#     s.html.render();
#
#     imgItem = s.html.find("img.irc_mi", first=True)
#     print(imgItem)
#     print(imgItem.attrs.get("src"));

    # imgsrc = item.find('a.rg_l', first=True).absolute_links;
    # imgsrc2 = item.find('a.rg_l', first=True).attrs.get('href');
    # print(imgsrc2);
    #
    # filepath = download_file("https://www.google.com/" + imgsrc2, title);
    #
    # print(title, filepath);

    # for url in urls:
    #     r = session.get(url)
    #     content = r.html.find("#goofs", first=True)
    #
    #     # print(name)
    #     if content:
    #         print(title)
    #         print(content.text)
    #         print('')

    time.sleep(1)


#https://www.google.com/search?q=contraceptiive+pill
