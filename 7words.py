import itertools

words = "Here are seven words we can use"
words_list = words.split(" ")

print(words_list)

permutated_words = list(itertools.permutations(words_list))

for word_list in permutated_words:
    print(word_list)
