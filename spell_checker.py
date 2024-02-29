import re
from spellchecker import SpellChecker

# sample prompts
prompt = [
    "Hello, my nname is",
    "The president of the United States is",
    "This is a spllchecekr",
    "Let's review"
]

phrase = "testing tsring"

# define spellchecker function for string
def spellchecker_string(phrase):
    # instantiate spellchecker
    spell = SpellChecker()

    # separate phrase into words
    res = re.split(r'\W+', phrase)

    # loop through each word and check spelling
    for idx, word in enumerate(res):
        print("word #{}: {}".format(idx,word))
        # if word is misspelled, fix it and update string
        if word != spell.correction(word):
            print("Incorrect word: {}. Proposed update: {}".format(word,spell.correction(word)))
            phrase = phrase.replace(word,spell.correction(word))
    return phrase

# define spellchecker function
def spellchecker(input):
    # if the input is a string, just call the string function
    if type(input) == str:
        input = spellchecker_string(input)
        print("Updated string: {}".format(input))
    # if the input is an array or list, then we want to loop each element
    elif type(input) == list:
        for index, phrase in enumerate(input):
            input[index] = spellchecker_string(phrase)
            print("Updated string {}: {}".format(index, input[index]))

spellchecker(phrase)
spellchecker(prompt)
