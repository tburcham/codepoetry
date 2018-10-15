from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

train = [
    ("A specter is haunting europe", "communist"),
    ("The specter of communism", "communist"),
    ("Long live the proletariat", "communist"),
    ("Commodities are dumb", "communist"),

    ("Free markets are good", "capitalist"),
    ("Buy low sell high", "capitalist"),
    ("$", "capitalist"),
    ("Venture capitalism is great", "capitalist")
]


cl = NaiveBayesClassifier(train)

# print(cl.classify("A specter is haunting this classroom"))
# print(cl.classify("Money money money money"))
# print(cl.classify("Let's buy a sofa"))
#
# prob = cl.prob_classify("Sell something")
# print(prob.prob("communist"), prob.prob("capitalist"))
#
# prob = cl.prob_classify("specter")
# print(prob.prob("communist"), prob.prob("capitalist"))

with open("manafort.txt") as infile:
    text = infile.read()

blob = TextBlob(text)
for sentence in blob.sentences:
    # if len(sentence.words) < 3:
    #     print(sentence)
    # if cl.classify(sentence) == "communist":
    #     print(sentence)

    #print(sentence.sentiment)

    if sentence.sentiment.polarity < 0.5:
        print(sentence)
