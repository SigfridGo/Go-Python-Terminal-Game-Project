# Worlde Clone

import random ## Random Module for getting a random word from list
import string ## Module for ASCII letters (English Alphabet)

testwords = ['RATIO', 'SPACE', 'CORAL', 'EXACT', 'APPLE', 'JAZZY', 'PAPER', 'CHAIR']
guess = None       ## Initial Value
attempts = 0
max_attempts = 6

## Colored Boxes using ANSI codes (no module import needed)
green_box = '\033[42m\033[30m'                    # Correct letter - right position
yellow_box = '\033[43m\033[30m'                   # Correct letter - wrong position
gray_box = '\033[48;2;120;124;126m\033[30m'       # Wrong letter
blank_box = '\033[0m'                             # reset terminal colors

randomword = random.choice(testwords).lower()

while guess != randomword and attempts < max_attempts:
    guess = input(f'Attempt {attempts + 1}/{max_attempts} - Type a 5-letter word: ').lower()
    if not all(char in string.ascii_lowercase for char in guess):       # Check if every character is a valid English letter (a-z)
        print('Error: The word must only contain standard English letters.')
    elif len(guess) != 5:
        print('Error: The word has to be 5 letters only.')
    elif guess not in [word.lower() for word in testwords]:
        print('Error: The word is not in the list.')
    else:
        attempts += 1

    ## Applying colored boxes to each letter and appending & joing to a list
    answer = []
    guess_upper = guess.upper()             # upper to match list of testwords
    randomword_upper = randomword.upper()

    for i in range(5):      # added multiple boxes for visual clarity
        if guess_upper[i] == randomword_upper[i]:
            answer.append(f'{green_box} {green_box} {green_box} {blank_box}')
        elif guess_upper [i] in randomword_upper:
            answer.append(f'{yellow_box} {yellow_box} {yellow_box} {blank_box}')
        else:
            answer.append(f'{gray_box} {gray_box} {gray_box} {blank_box}')
    print('  '.join(answer))        # planned to add input letters in each box later


if guess == randomword.lower():
    print(f'You got the correct word in {attempts} guesses.')
else:
    print(f'You ran out of guesses. The word was {randomword}.')

