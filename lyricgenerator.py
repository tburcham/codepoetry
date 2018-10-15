from requests_html import HTMLSession
session = HTMLSession()
import requests
from pprint import pprint
from textblob import TextBlob
from textblob import Word
import random

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

seed = "beatles"
numsongs = 10

flagwords = ["'", "'s", ".", "-"]

r = session.get("https://www.google.com/search?q=top+100+" + seed + "+songs+of+all+time")
if(r.status_code != 200) :
    print("HTTP Response " + r.status)
    raise SystemExit

text = []
text.append(open('rand.txt').read())
# text.append(open('fountainhead.htm').read())
# text.append(open('atlas_shrugged.htm').read())

textc = ' '.join(text)

texttokens = {}
textb = TextBlob(textc);


# for line in textb:
#     print(line.tags)

for tag in textb.tags:
    # all(i in b for i in a)
    # if all(i in tag[0] for i in flagwords):

    # isflagword = False
    # # print(all(i in tag[0] for i in flagwords))
    # for i in flagwords:
    #     if tag[0].text.match(i):
    #         isflagword = True

    if (tag[0].isalpha() and tag[0] != "'"):
        if (texttokens.get(tag[1]) == None):
            texttokens[tag[1]] = []
        # print(tag[1])
        texttokens[tag[1]].append(tag[0])

for tag in texttokens:
    # print("tag", texttokens[tag])
    texttokens[tag] = list(set(texttokens[tag]))

# print(texttokens)
# nouns = list(set(nouns)) # quick conversion to make a list unique
# print(nouns)





# for html in r.html:
container = r.html.find(".rl_feature", first=True)

items = container.find(".rl_item")[0:numsongs]

for item in items:


    newsong = []
    wordrels = {}
    #print(item.text)

    songTitle = item.find(".title", first=True)

    # s = session.get("https://genius.com/search?q=" + song.text)
    # s.html.render()

    s = requests.get("https://genius.com/api/search/multi?q=" + songTitle.text)
    data = s.json()

    # pprint(data)
    for song in data["response"]["sections"]:
    # songRef = data["response"]["sections"]
    # pprint(songRef)
        if song["type"] == "song":

            url = song["hits"][0]["result"]["url"]
            # print(url)

            t = session.get(url)
            lyrics = t.html.find(".lyrics", first=True)
            # print(lyrics.text)

            lyricLines = lyrics.text.split("\n")

            # print(len(lyricLines))

            for line in lyricLines:
                lineBlob = TextBlob(line)
                # print(lineBlob.tags)

                newline = []
                for tag in lineBlob.tags:
                    pos = texttokens.get(tag[1])

                    if (pos != None):

                        # print('wr', wordrels.get(tag[0]))
                        if wordrels.get(tag[0]) == None:

                            rnd = random.random() * len(pos)
                            rnd = round(rnd)
                            rnd = clamp(rnd, 0, len(pos) - 1)

                            # print(tag[1], rnd, len(pos))

                            newword = pos[rnd]
                            wordrels[tag[0]] = newword

                        else:

                            newword = wordrels.get(tag[0])

                    else:
                        newword = tag[0]

                    newword = newword.lower()

                    # newword = pos[random(0, len(pos))]

                    # print(newword)

                    newline.append(newword)

                newsong.append(newline)

            filesave = open('songs/' + seed + '-' + songTitle.text + '.txt', 'w')

            print('')
            print('============')
            print(songTitle.text)
            print('by Ayn Rand')

            filesave.write(songTitle.text)
            filesave.write('\n')
            filesave.write('by Ayn Rand')
            filesave.write('\n\n')

            for line in newsong:
                l = (' ').join(line)
                print(l)
                filesave.write(l)
                filesave.write('\n')

            filesave.close()


# print(html)
