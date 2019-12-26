import re
def count_words(sentence):
    word_kit = {}
    regex = re.compile(r"\'*[\s\":._,!&@$^%\n]+\'*|\'$")
    splitted = regex.split(sentence)
    for word in splitted:
        if word != "":
            if word.lower() in word_kit:
                word_kit[word.lower()] += 1
            else:
                word_kit[word.lower()] = 1
    return word_kit