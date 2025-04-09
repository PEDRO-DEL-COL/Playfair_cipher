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

keyword = cleanup_text(input('Type your keyword: '))

keyword_list = []

valid_letters = set(string.ascii_lowercase)

for letter in keyword:
    if letter in valid_letters and letter not in keyword_list:
        keyword_list.append(letter)

alphabet = list(string.ascii_lowercase)

alphabet.remove('j')

alphabet_without_keyword_list = [letter for letter in alphabet if letter not in keyword_list]

playfair_table = keyword_list + alphabet_without_keyword_list

matrix = []

for i in range(0,25,5):
    line = playfair_table[i:i+5]
    matrix.append(line)

for line in matrix:
    print(line)

# the user will provide an input with the word that should be coded
# the program will separate them into pairs, if the number of characters is odd, it should add a 'x' to make it even

word_to_be_coded = cleanup_text(input('Type the word you\'d like to code: '))

word_to_be_coded_list = []
i = 0

while i < len(word_to_be_coded):
    letter1 = word_to_be_coded[i]

    if i + 1 < len(word_to_be_coded):
        letter2 = word_to_be_coded[i + 1]

        if letter1 == letter2:

            word_to_be_coded_list.extend([letter1, 'x'])
            i += 1
        else:
            word_to_be_coded_list.extend([letter1, letter2])
            i += 2
    else:
        word_to_be_coded_list.extend([letter1, 'x'])
        i += 1

coded_word = ''

for i in range(0, len(word_to_be_coded_list), 2):
    l1, l2 = word_to_be_coded_list[i], word_to_be_coded_list[i+1]
    c1, c2 = code_pair(l1,l2,matrix)
    coded_word += c1 + c2

print(word_to_be_coded_list)
print(coded_word)
