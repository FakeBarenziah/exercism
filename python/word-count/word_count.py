import re
def count_words(sentence):
    word_kit = {}
    sentence = re.split("\s|,|_|\.|:", sentence)
    for word in sentence:
        if word != "":
            if word.lower() in word_kit:
                word_kit[word.lower()] += 1
            else:
                word_kit[word.lower()] = 1
    return word_kit