# Worlde Clone

import random ## Random Module for getting a random word from list


testwords = ['ratio', 'space', 'coral', 'exact']
guess = None ## Initial Value

randomword = random.choice(testwords)

while guess != randomword:
    try: ## Check for value (int or str)
        guess = str(input('Type a 5-letter word: '))
        if len(guess) != 5:
            print('Error: The word has to be 5 letters only.')
    except ValueError:
        print('The input has to be a word')
