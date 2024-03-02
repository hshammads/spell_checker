import re
import os
import os.path
import tkinter as tk
import pathlib
from pathlib import Path
from tkinter import filedialog as fd
from spellchecker import SpellChecker

# define global variables
input_file = ''
file_path = ''
file_name = ''
file_extension = ''
output_file = ''
prompt_arr = []

# create tkinter GUI
app = tk.Tk()

# specify GUI title and dimensions
app.title('Spell Checker')
app.geometry('600x350')

# Create a textfield for putting the
# text extracted from file
tk_text = tk.Text(app, height=16)

# Specify the location of textfield
tk_text.grid(column=0, row=0, sticky='nsew')

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

# Create a function to open the file dialog
def process_file():
    # Specify the file types
    filetypes = (('text files', '*.txt'),
                 ('document files', '*.docx'),
                 ('csv files', '*.csv'),
                 ('All files', '*.*'))

    # Show the open file dialog by specifying path
    file = fd.askopenfile(filetypes=filetypes,
                       initialdir="~/Downloads")
    input_file = os.path.abspath(file.name)
    file_path = os.path.dirname(input_file)
    file_name = Path(input_file).stem
    file_extension = Path(input_file).suffix
    # Insert the text extracted from file in a textfield
    # text.insert('1.0', file.readlines())
    tk_text.delete('1.0',tk.END)
    tk_text.insert(tk.END, 'Input file: {}\n'.format(file_name + file_extension))
    tk_text.insert(tk.END, 'Opening file ...\n')
    # open and read file
    file = open(input_file, 'r')
    # import text
    tk_text.insert(tk.END, 'Reading data from file ...\n')
    text = file.readlines()
    # close file
    file.close()

    # parse out the text into array
    prompt_arr = [line.strip() for line in text]
    tk_text.insert(tk.END, 'Data gathered from file: {}\n'.format(prompt_arr))
    tk_text.insert(tk.END, 'Spell checking ...\n')
    for index, phrase in enumerate(prompt_arr):
        prompt_arr[index] = spellchecker_string(phrase)
    tk_text.insert(tk.END, 'Spell check complete!\n\n')

    # write out corrected text
    output_file = file_path + '/' + file_name + '_spellchecked' + file_extension
    print(output_file)
    # open and write to file
    file = open(output_file, 'w')
    tk_text.insert(tk.END, 'Writing data ...\n')
    for prompt in prompt_arr:
        file.writelines(prompt + '\n')
    # close file
    file.close()
    tk_text.insert(tk.END, 'Data written to file: {}\n\n'.format(output_file))
    tk_text.insert(tk.END, 'If you would like to run the program again, select another file to process.\nOtherwise, exit out the program.\n')

# Create buttons
process_button = tk.Button(app, text = 'Select file to process', command = process_file)
process_button.grid(row = 1, sticky = 'w', padx = 200, pady = 50)

# Make infinite loop for displaying app on the screen
app.mainloop()
