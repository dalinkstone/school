import time

#This introduces the program to the user
print('@@@@@@@@@@@@@@@@@@@@@@')
print('@ Create your story! @')
print('@@@@@@@@@@@@@@@@@@@@@@\n')

#Here we display what information is required of the user
print('Please supply the following words: \n')

#This while loop is setup to validate the input so that only letters may be input into the input prompt.
#If letters are not put into the prompt the user is notified of an error message and prompted again.
while True:
    adjective = input('Adjective: ')
    if adjective.isalpha():
        break
    print('ERROR: Numbers are not valid input. Try again.')

while True:
    animal = input('Animal: ')
    if animal.isalpha():
        break
    print('ERROR: Numbers are not valid input. Try again.')

while True:
    verb1 = input('Verb: ')
    if verb1.isalpha():
        break
    print('ERROR: Numbers are not valid input. Try again.')

while True:
    exclamation = input('Exclamation: ')
    if exclamation.isalpha():
        break
    print('ERROR: Numbers are not valid input. Try again.')

while True:
    verb2 = input('Verb: ')
    if verb2.isalpha():
        break
    print('ERROR: Numbers are not valid input. Try again.')

while True:
    verb3 = input('Verb: ')
    if verb3.isalpha():
        break
    print('ERROR: Numbers are not valid input. Try again.')

#Here we clean the data into its proper format
#I added the upper formatting on the exclamation to add some tone to the story
adjective = adjective.lower()
animal = animal.lower()
verb1 = verb1.lower()
exclamation = exclamation.upper()
verb2 = verb2.lower()
verb3 = verb3.lower()

print('\n')

print('Loading your story...')
animation = [
"[        ]",
"[=       ]",
"[===     ]",
"[====    ]",
"[=====   ]",
"[======  ]",
"[======= ]",
"[========]",
"[ =======]",
"[  ======]",
"[   =====]",
"[    ====]",
"[     ===]",
"[      ==]",
"[       =]",
"[        ]",
"[        ]"
]
num = 0
while num < (17*8):
    print(animation[num % len(animation)], end="\r")
    time.sleep(0.1)
    num += 1

print(f'The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb1} down the hallway. \"{exclamation}!\" I yelled. But all I could think to do was to {verb2} over and over. Miraculously, that caused it to stop, but not before it tried to {verb3} right in front of my family.')
