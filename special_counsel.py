from textblob import TextBlob
from textblob import Word
import random;

ngram_length = 4
pos_selector = 'VB'
num_phrases = 50

text = open('manafort.txt').read()
text_analyzed = TextBlob(text)

# print(text_analyzed.noun_phrases)

# print(text_analyzed.sentiment)

# for line in text:
#
#     line = line.strip()
#     words = line.split(' ')
#
#     words = [word for word in words if word.endswith("ing")]
#     new_line = " ".join(words)
#     print(new_line)

sentences = text_analyzed.sentences



# for sentence in sentences:
#    sentiment_text.append(sentence)
# sentiment_text = text_analyzed.raw_sentences
# sentiment_text.sort()
# print(('\n').join(sentiment_text))



ngrams = text_analyzed.ngrams(ngram_length)
# print(ngrams)

# ngrams.sort()
# print(('\n').join(ngrams))

ngram_list = []
for ngram in ngrams:

    # for word in ngram:
    first_word = TextBlob(ngram[0])

    # print('ngram first word:', first_word.tags[0])

    if (first_word.tags[0][1].startswith(pos_selector)):

        ngram_phrase = []
        for word in ngram:
            ngram_phrase.append(word)

        # ngram_phrase.append('full stop')
        ngram_list.append((' ').join(ngram_phrase))


    # ngram_tags = ngram.pos_tags
    # print('ngram:', ngram[0], ngram_tags)

    # print('ngram:', ngram[0], ngram[0].pos_tag, '\n')
    # if (ngram[0].pos_tag == 'VB'):
    #     print('len', len(ngram))
    #     if (len(ngram) == 2):
    #         ngram_list.append(ngram[0] + ' // ' + ngram[1] + ' // ' + ngram[2])

# ngram_list.sort()

filtered_ngram_list = []

for i in range(num_phrases):
    rnd = random.choice(ngram_list)

    phrase = TextBlob(rnd).translate('en', 'ru')

    # print(rnd, " ", phrase)
    # print(phrase)

    phrase_list = phrase.words

    # print('phrases.push_back("' + (' ').join(phrase_list) + '");')
    print('phrases.push_back(make_tuple("' + (' ').join(phrase_list) + '", "' + rnd + '"));')

# print(('\n').join(ngram_list))

# print('positive?')
# for sentence in sentences:
#
#
#     if sentence.sentiment.polarity > 0:
#         print(sentence)
#         print(sentence.sentiment)
#         print('')
#
#
# syn_text = []
#
# print('negative?')
# for sentence in sentences:
#
#     if sentence.sentiment.polarity < 0:
#         print(sentence)
#         print(sentence.sentiment)
#         print('')
#
#         for word in sentence.words:
#             word = Word(word)
#             print(word)
            # d = word.define()
            # if (len(d) > 0):
            #     syn_text.append(d[0])
            # if len(word.synsets) > 0:
            # syn_text.append(word.synsets[-1].lemma_names()[-1])
            # print(word.define())

# print(('\n').join(syn_text))

# Most positive / most negative?
# Redaction?
# Only good news
# definitions
# Word-frequency
# synonym substition
