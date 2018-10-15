import random

text = open('atlas.txt').readlines()

for line in text:
    #print(line.replace('\\n', ''))
    line = line.strip()
    #line = line.replace('Vermont', 'VVVVVVV')
    # print(line)

    words = line.split(' ')

    #print(words[0].center(30, '.').upper())

    # random_word = random.choice(words)
    # print(random_word)

    #random.shuffle(words)
    # words = sorted(words)
    # new_line = " ".join(words)
    # print(new_line)

    words = [word for word in words if word.endswith("ing")]
    new_line = " ".join(words)
    print(new_line)
