import random

magic_number = random.randint(1, 100)

guess = ""
while guess != magic_number:
    guess = int(input('What do you think the magic number is?: '))
    if guess > magic_number:
        print('Nice try! The magic number is lower than your guess!\n')
    elif guess < magic_number:
        print('Nice try! The magic number is higher than your guess!\n')
    else:
        print('Nice job! You guessed it!')

