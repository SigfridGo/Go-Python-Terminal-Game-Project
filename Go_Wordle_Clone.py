# Worlde Clone

import random ## Random Module for getting a random word from list
import string ## Module for ASCII letters (English Alphabet)

testwords = ['RATIO', 'SPACE', 'CORAL', 'EXACT']
guess = None ## Initial Value
attempts = 0
max_attempts = 6

## Colored Boxes using ANSI codes (no module needed)
green = '\033[42m\033[30m' # Correct letter - right position
yellow = '\033[43m\033[30m' # Correct letter - wrong position
gray = '\033[47m\033[30m' # Wrong letter
blank = '\033[0m' # reset terminal colors

randomword = random.choice(testwords).lower()

while guess != randomword and attempts < max_attempts:
    guess = input(f'Attempt {attempts + 1}/{max_attempts} - Type a 5-letter word: ').lower()
    if not all(char in string.ascii_lowercase for char in guess): ## Check if every character is a valid English letter (a-z)
        print('Error: The word must only contain standard English letters.')
    elif len(guess) != 5:
        print('Error: The word has to be 5 letters only.')
    elif guess not in [word.lower() for word in testwords]:
        print('Error: The word is not in the list.')
    else:
        attempts += 1

## logic for colored boxes somewhere here


if guess == randomword.lower():
    print(f'You got the correct word in {attempts} guesses.')
else:
    print(f'You ran out of guesses. The word was {randomword}.')