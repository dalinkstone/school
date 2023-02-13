from random import choice
from words import word_list
from rich.console import Console
from rich.prompt import Prompt

console = Console()
the_word = choice(word_list)
num_guesses = 0
already_guessed = []
guessed = []
pattern = []

Colors = {
    'correct_place': '🟩',
    'correct_letter': '🟨',
    'incorrect_letter': '⬛'
}

console.print(f'\n[white on red] Welcome to WordGuess [/]\n')

guess = ""
while guess != the_word:
    guess = input(f'Guess the word: \n')
    print('\n')
    guess_iter = [letter for letter in guess]
    guessed_letters = []
    guess_pattern = []
    if guess.isalpha() == False:
        console.print('[red]ERROR: WordGuess only uses letters. Try again.\n')
        continue

    guess = guess.upper()

    if len(guess) != 5:
        console.print('[red]You can only guess a five letter word. Try again.\n')
        continue
    elif guess in already_guessed:
        console.print(f'[red]You already guessed {guess}. Try again\n')
        continue
    else:
        already_guessed.append(guess)
        num_guesses+=1
    
    for i, letter in enumerate(guess):
        if the_word[i] == guess[i]:
            guessed_letters += f'[black on green]{letter}[/]'
            guess_pattern.append(Colors['correct_place'])
        elif letter in the_word:
            guessed_letters += f'[black on yellow]{letter}[/]'
            guess_pattern.append(Colors['correct_letter'])
        else:
            guessed_letters += f'[black on black]{letter}[/]'
            guess_pattern.append(Colors['incorrect_letter'])
    
    guessed_letters_print = ''.join(guessed_letters)
    guess_pattern_print = ''.join(guess_pattern)
    guessed.append(guessed_letters_print)
    pattern.append(guess_pattern_print)

    if guess == the_word:
        console.print('[white on blue]Congratulations![/]')
        print(f'You guessed the word in {num_guesses} guesses!\n')
        print('You guessed the following words with the following patterns.')
        console.print(f'[white on blue]{already_guessed}[/]')
        console.print(*pattern, sep='\n')
        break

    console.print(guessed_letters_print)
    console.print(guess_pattern_print)
    print('\n')
    console.print(f'[white on blue]You have already guessed: {already_guessed}')
    console.print(*guessed, sep='\n')
    console.print(*pattern, sep='\n')
    print('\n')


