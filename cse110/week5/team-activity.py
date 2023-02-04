import time

while True:
    try:
        grade_percentage = int(input('What is your grade percentage (number only): '))
        break
    except ValueError:
        print('Input must be a whole integer (##). Please try again.')
        continue

if (grade_percentage >= 97):
    grade_letter = 'A+'
elif (grade_percentage >= 93) and (grade_percentage < 97):
    grade_letter = 'A'
elif (grade_percentage >= 90) and (grade_percentage < 93):
    grade_letter = 'A-'
elif (grade_percentage >= 87) and (grade_percentage < 90):
    grade_letter = 'B+'
elif (grade_percentage >= 83) and (grade_percentage < 87):
    grade_letter = 'B'
elif (grade_percentage >= 80) and (grade_percentage < 83):
    grade_letter = 'B-'
elif (grade_percentage >= 77) and (grade_percentage < 80):
    grade_letter = 'C+'
elif (grade_percentage >= 73) and (grade_percentage < 77):
    grade_letter = 'C'
elif (grade_percentage >= 70) and (grade_percentage < 73):
    grade_letter = 'C-'
elif (grade_percentage >= 67) and (grade_percentage < 70):
    grade_letter = 'D+'
elif (grade_percentage >= 63) and (grade_percentage < 67):
    grade_letter = 'D'
elif (grade_percentage >= 60) and (grade_percentage < 63):
    grade_letter = 'D-'
else: 
    grade_letter = 'F'

print('\n')

print('Calculating your grade...')
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

print(f'Your letter grade is {grade_letter}!\n')

if grade_percentage > 70:
    print('Congratulations! You passed the class! Yay!')
else:
    print('Maybe you should study harder...')

