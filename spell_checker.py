import re
import os
import os.path
from spellchecker import SpellChecker

# define global variables
INPUT_FILE = './input.txt'
OUTPUT_FILE = './output.txt'
prompt_arr = []

# define functions
# define spellchecker function for string
def spellchecker_string(phrase):
    rev_phrase = phrase
    # instantiate spellchecker
    spell = SpellChecker()

    # separate phrase into words
    res = re.split(r'\W+', rev_phrase)

    # loop through each word and check spelling
    for idx, word in enumerate(res):
            # if word is misspelled, fix it and update string
        if word != spell.correction(word):
            rev_phrase = rev_phrase.replace(word,spell.correction(word))
    return rev_phrase

# define spellchecker function
def spellchecker(prompt):
    rev_prompt = prompt
    # if the input is a string, just call the string function
    if type(rev_prompt) == str:
        rev_prompt = spellchecker_string(rev_prompt)
    # if the input is an array or list, then we want to loop each element
    elif type(rev_prompt) == list:
        for index, phrase in enumerate(rev_prompt):
            rev_prompt[index] = spellchecker_string(phrase)
    return rev_prompt

run_pgm_again = True

while(run_pgm_again):
    # ask user for debug mode
    debug = input('\nWould you like the debug mode on? (Y/N): ')
    if debug.upper() == 'Y' or debug.upper() == 'YES':
        debug = True
    else:
        debug = False

    if debug:
        print('Debug mode is ON ...')
    else:
        print('Debug mode is OFF ...')

    # ask user for input or read from file
    existing_file = input('\nWould you like to use existing file? (Y/N): ')
    if existing_file.upper() == 'Y' or existing_file.upper() == 'YES':
        if debug:
            print('Reading from existing file: ', INPUT_FILE)
        # open and read file
        file = open(INPUT_FILE, 'r')
        # import text
        text = file.readlines()
        if debug:
            print("Text imported from file {}: {}".format(INPUT_FILE,text))
        # parse out the text into array
        prompt_arr = [line.strip() for line in text]
        if debug:
            print("Array generated from input file: ", prompt_arr)
        # close file
        file.close()
    else:
        in_prompt = input('\nPlease enter string/phrase for program to process: ')
        prompt_arr = [in_prompt]
        print('Input phrase: ', in_prompt)
        if debug:
            print('String stored: ', prompt_arr)

    # call the spellchecker function
    prompt_arr = spellchecker(prompt_arr)

    # print output
    for index, phrase in enumerate(prompt_arr):
        print('Corrected phrase #{}: {}'.format(index + 1,phrase))

    # if input data from file, save it
    if existing_file.upper() == 'Y' or existing_file.upper() == 'YES':
        if debug:
            print('\nWriting corrected phrases to file: {} ...'.format(OUTPUT_FILE))
        # open and write to file
        file = open(OUTPUT_FILE, 'w')
        for prompt in prompt_arr:
            file.writelines(prompt + '\n')
        if debug:
            print('Corrected phrases written to file:', OUTPUT_FILE)
        # close file
        file.close()

    rerun = input('\nWould you like to run through the program again? (Y/N): ')
    if rerun.upper() != 'Y' and rerun.upper() != 'YES':
        run_pgm_again = False
