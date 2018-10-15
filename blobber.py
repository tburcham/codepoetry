from textblob import TextBlob
from textblob import Word

text = open('manafort.txt').read()
blob = TextBlob(text)

# blob.sentences
# print(blob.sentences)

# for word in blob.words:
#     print(word)

nouns = []
for tag in blob.tags:
    if tag[1] == "VBG":
        nouns.append(tag[0])
        # print(tag[0])

nouns = list(set(nouns)) # quick conversion to make a list unique
print(nouns)

# for phrase in blob.noun_phrases:
#     print(phrase)
