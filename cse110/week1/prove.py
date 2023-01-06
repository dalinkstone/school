import uuid

your_color = input("What is your favorite color?: ")

your_color = your_color.lower()
password_key = uuid.uuid4().hex

if (your_color == 'red') or (your_color == 'blue'):
    print('Secret Code Accepted\n')
    print(f'Your favorite color is {your_color} and this is your password key: {password_key}')
else:
    print('That\'s boring... Is your favorite color really '+your_color+'?')

key_check = input("What is your password key?: ")

def valid_check(key_check):
    try:
        uuid.UUID(str(key_check))
        return print('Pass key accepted! That\'s my favorite color too!')
    except ValueError:
        return print("That's not a pass_key. Your favorite color must not be my favorite color.")

output = valid_check(key_check)