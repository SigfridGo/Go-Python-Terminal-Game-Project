# Worlde Clone

import random ## Random Module for getting a random word from list
import string ## Module for ASCII letters (English Alphabet)
import nltk   ## English dictionary module 

## Downloads the dataset into the pc
nltk.download('words')
from nltk.corpus import words

## Extracting only the 5-letter words from the english module (and lower case)
word_list = [w.lower() for w in words.words() if len(w) == 5 and w.isalpha()]

## Colored Boxes using ANSI codes (no module import needed)
green_box = '\033[42m\033[30m'                    # Correct letter - right position
yellow_box = '\033[43m\033[30m'                   # Correct letter - wrong position
gray_box = '\033[48;2;120;124;126m\033[30m'       # Wrong letter
blank_box = '\033[0m'                             # Reset terminal colors
red_text = '\033[31m'
empty_tile = f'{blank_box}[    ]{blank_box}'       # For the 6x5 grid similar to Wordle

def wordle_board(board):
    for row in board:
        print('  '.join(row))
    print()
    print()

while True:
    guess = None       ## Initial Value
    attempts = 0
    max_attempts = 6
    randomword = random.choice(word_list).lower()
    board = [[empty_tile for i in range(5)] for i in range(max_attempts)]

    # Replicating the list of letters in wordle 
    # Dictionary for letters to be joined later
    letters_list = {char: f' {char.upper()} ' for char in string.ascii_lowercase}

    while guess != randomword and attempts < max_attempts:
        ## Prints the board
        wordle_board(board)

        ## Replicating the virtual keyboard from Wordle
        print(' ' + ''.join(letters_list[c] for c in 'qwertyuiop'))
        print('  ' + ''.join(letters_list[c] for c in 'asdfghjkl'))
        print('    ' + ''.join(letters_list[c] for c in 'zxcvbnm') + '\n')

        ## Checks for invalid inputs
        guess = input(f'Attempt {attempts + 1}/{max_attempts} - Type a 5-letter word: ').lower()
        if not all(char in string.ascii_lowercase for char in guess):       # Check if every character is a valid English letter (a-z)
            print(f'{red_text}Error: The word must only contain standard English letters.{blank_box}')
            continue
        elif len(guess) != 5:
            print(f'{red_text}Error: The word has to be 5 letters only.{blank_box}')
            continue
        elif guess not in word_list:
            print(f'{red_text}Error: The word is not in the list.{blank_box}')
            continue
        else:
            attempts += 1

        ## Applying colored boxes to each letter and appending & joining to a list
        answer = [None] * 5              ## pre-allocating answer indexes to compare and count each letters' apperance in randomword_upper
        guess_upper = guess.upper()      # upper to match list of testwords
        randomword_upper = randomword.upper()

        mismatch_count = {}         # counts each character index for repeating letters, adds count to check for mismatch on pass 1 and 2
        for ch in randomword_upper:
            mismatch_count[ch] = mismatch_count.get(ch, 0) + 1

        ## 1st Pass: Letters matching exact index
        ## Counts the number of correct letter placements for the guess
        ## Decrements count for checking yellow/gray box placements on next pass
        for i in range(5):
            ch = guess_upper[i]
            if ch == randomword_upper[i]:
                answer[i] = f'{green_box}  {ch}   {blank_box}'
                letters_list[guess[i]] = f'{green_box} {ch} {blank_box}'
                mismatch_count[ch] -= 1

        ## 2nd Pass: Yellow and gray boxes
        ## Checks each index if they have green box from 1st pass, skips to next index if true
        ## If mismatch_count > 0, a letter that repeats is somewhere else as well, a yellow box is then placed
        for i in range(5):
            if answer[i] is not None:
                continue
            ch = guess_upper[i]
            if mismatch_count.get(ch, 0) > 0:
                answer[i] = f'{yellow_box}  {ch}   {blank_box}'
                mismatch_count[ch] -= 1     ## Decrements so that it doesn't count more than what is repeated
                if green_box not in letters_list[guess[i]]:
                    letters_list[guess[i]] = f'{yellow_box} {ch} {blank_box}'
            else:
                answer[i] = f'{gray_box}  {ch}   {blank_box}'
                if green_box not in letters_list[guess[i]] and yellow_box not in letters_list[guess[i]]:
                    letters_list[guess[i]] = f'{gray_box} {ch} {blank_box}'

        ## Replaced print(f'  '.join(answer)) since board = answer already prints the attempted answer
        board[attempts - 1] = answer
    wordle_board(board)

    if guess == randomword.lower():
        print(f'You got the correct word in {attempts} guesses.')
    else:
        print(f'You ran out of guesses. The word was {randomword.upper()}.')

    play_again = input('\nDo you want to play again? (y/n): ').strip().lower()
    if play_again != 'y':
        break
    print('\n--New Wordle Game--')