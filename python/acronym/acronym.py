from functools import reduce
import re

def return_capitalized_first_letter(word):
    if len(word) > 0:
        return word[0].upper()

def abbreviate(words):
    regex = re.compile("[\\s\\-\\_]")
    return reduce((lambda x, y: x + y), map(return_capitalized_first_letter, filter((lambda x: len(x) > 0) ,regex.split(words))))