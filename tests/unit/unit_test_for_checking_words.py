# CREATED: NOVEMBER 18 2026 BY CHARLES KAUFMAN
# LAST EDITED: NOVEMBER 20 2026

import collections
import json

# Opens the words_dictionary.json file and loads it into a dictionary called words.
with open('words_dictionary.json', 'r') as f:
    dictionary = json.load(f)

valid_words = []


# modified function that checks if a user input is valid based on our contraints.
#   This includes:
#     1) Checking if a word is at minimum three letters long.
#     2) Checking if a word is valid. By checking if it is in the words_dictionary.json file,
#        we automatically exluded symbols, numbers, and punctuation.
#     3) Checking if a word is made up of letters from the phrase. This also includes making sure
#        that a letter was not used more than it appears in the phrase.
def unit_test_check_input(output_characters, user_input):
    word_valid = True
    min_input_length = 3
    character_counts = collections.Counter(output_characters)


    # Takes input from user.
    input_characters = [char for char in user_input if char != ' ']

    # Checks to see if the input is at least 3 characters long.
    if len(input_characters) < min_input_length:
        print("ERROR: Please enter a word that is at least 3 characters long.\n")
        return

    # Checks to see if input is valid word.
    if user_input.lower() not in dictionary:
        print(f"ERROR: {user_input} is not a word in the dictionary.\n")
        word_valid = False
        return

    # Compares the characters in the user input to the characters in the output. If a character in the user input is 
    #   not in the output, it prints that the word is invalid. If a character in the user input was used more times 
    #   than it was in the output, it prints that the word is invalid. Else it is valid.
    if word_valid:
        for char in input_characters:
            if char not in character_counts:
                print(f"ERROR: {user_input} has a character that is not in the phrase.\n")
                return
            elif input_characters.count(char) > character_counts[char]:
                print(f"ERROR: {user_input} has a character that is used more times than in the phrase.\n")
                return
        valid_words.append(user_input)
        print(f"INFO: {user_input} is a valid word.\n")


# Test cases for the checker with a given phrase. Note with the given user inputs, 'can' should be a valid input.
phrase_output = "I can't with the man in the yellow hat."
out = [char for char in phrase_output if char != ' ']
user_inputs = ['I', 'can', "can't", '       ', '', 'zealous', 'asdfgdsa', '998765', '[]()',"''", 'yh+', "hat."]

print("----------------------------------")
for inp in user_inputs:
    print(f"Testing input: '{inp}'")
    unit_test_check_input(out, inp)
print("----------------------------------")

print(f"Valid words found: {valid_words}")