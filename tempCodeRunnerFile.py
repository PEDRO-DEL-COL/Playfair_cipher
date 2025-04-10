# This is a Playfair's cipher decoder and coder
# The Playfair's cipher is an effective way to hide a word that you don't want people to know about
# This program can create the coded word for you and also


import unicodedata
import string

# funciton to find the position of a char inside the matrix created by the keyword of your choice
def find_position(letter, matrix):
    for i, line in enumerate(matrix):
        if letter in line:
            return i, line.index(letter)
    
    return None, None

# this function will take as input the pair of letters to be coded and relate their
# position inside the given matrix according to the rules
def code_pair(letter1, letter2, matrix):
    line1, col1 = find_position(letter1, matrix)
    line2, col2 = find_position(letter2, matrix)

    if line1 == line2:
        return matrix[line1][(col1 + 1) % 5], matrix[line2][(col2 + 1) % 5]
    
    elif col1 == col2:
        return matrix[(line1 + 1) % 5][col1], matrix[(line2 + 1) % 5][col2]
    
    else:
        return matrix[line1][col2], matrix[line2][col1]

# function to clean any input from symbols and unwanted characters
def cleanup_text(text):
    text = text.strip().lower().replace('j', 'i')
    text = ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn' and c in string.ascii_lowercase
    )
    return text

# function that creates the matrix already cleaning the keyword and setting it without repeating characters
def create_matrix(keyword):
    keyword = cleanup_text(keyword)
    seen = set()
    keyword_list = [c for c in keyword if c not in seen and not seen.add(c)]
    alphabet = [c for c in string.ascii_lowercase if c != 'j' and c not in keyword_list]
    matrix = keyword_list + alphabet
    return [matrix[i:i+5] for i in range(0,25,5)]

def code_word(word, matrix):
    word_list = []
    i = 0
    coded_word = ''

    while i < len(word):
        letter1 = word[i]
        if i+1 < len(word):
            letter2 = word[i+1]
            if letter1 == letter2:
                word_list.extend([letter1, 'x'])
                i += 1
            else:
                word_list.extend([letter1, letter2])
                i += 2
        
        else:
            word_list.extend([letter1, 'x'])
            i += 1

    for i in range(0, len(word_list), 2):
        letter1 = word_list[i]
        letter2 = word_list[i+1]
        char1, char2 = code_pair(letter1, letter2, matrix)
        coded_word = coded_word + char1 + char2

    return coded_word

matrix = create_matrix(input('Type your keyword: '))

word_to_be_coded = cleanup_text(input('Type the word you want to code: '))

coded_word = code_word(word_to_be_coded, matrix)

print(coded_word)