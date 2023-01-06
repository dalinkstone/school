import enum
import re
import phonenumbers as pn

#Prompting the user to input data
first_name = input("First Name: ")
last_name = input("Last Name: ")
email_address = input("Email address: ")

print('NOTICE: Only US Based Phonenumbers are Allowed.')
print('Please input your US Based Phonenumber digit-by-digit.')
formatter = pn.AsYouTypeFormatter("US")
digit1 = input('First digit: ')
formatter.input_digit(digit1)
digit2 = input('Second digit: ')
formatter.input_digit(digit2)
digit3 = input('Third digit: ')
formatter.input_digit(digit3)
digit4 = input('Fourth digit: ')
formatter.input_digit(digit4)
digit5 = input('Fifth digit: ')
formatter.input_digit(digit5)
digit6 = input('Sixth digit: ')
formatter.input_digit(digit6)
digit7 = input('Seventh digit: ')
formatter.input_digit(digit7)
digit8 = input('Eigth digit: ')
formatter.input_digit(digit8)
digit9 = input('Ninth digit: ')
formatter.input_digit(digit9)
digit10 = input('Tenth digit: ')
phone_number = formatter.input_digit(digit10)


job_title = input("Job title: ")
id_number = input("ID Number: ")
hair_color = input("Hair color: ")
eye_color = input("Eye color: ")
start_month = input("Start month: ")
training = input("Have you completed your training? (Yes/No): ")
training = re.sub('\s+', '', training)
acceptable_list = ['yes', 'no']

if training.lower() not in acceptable_list:
    print(f'Your input for training was: {training}. This is not an acceptable answer. Please try again.')
    training = input("Have you completed your training? (Yes/No): ")

#Cleaning the input data
first_name = re.sub(r"[0-9]", "", first_name)
first_name = re.sub('\s+', '', first_name)
last_name = re.sub(r"[0-9]", "", last_name)
last_name = re.sub('\s+', '', last_name)
job_title = re.sub('\s+', ' ', job_title)
email_address = re.sub('\s+', '', email_address)
hair_color = re.sub(r"[0-9]", "", hair_color)
hair_color = re.sub('\s+', '', hair_color)
eye_color = re.sub(r"[0-9]", "", eye_color)
eye_color = re.sub('\s+', '', eye_color)
start_month = re.sub('\s+', '', start_month)


first_name = first_name.title()
last_name = last_name.upper()
job_title = job_title.title()
email_address = email_address.lower()
hair_color = hair_color.title()
eye_color = eye_color.title()
start_month = start_month.title()
training = training.title()

print('\n')
print('Your ID Card is:')
print('----------------------------------------')
print(f'{last_name}, {first_name}')
print(job_title)
print(f'ID: {id_number}\n')
print(email_address)
print(f'{phone_number}\n')
print(f"{'Hair: '+hair_color:<23}             Eyes: {eye_color}")
print(f"{'Month: '+start_month:<25}           Training: {training}")
print('----------------------------------------')