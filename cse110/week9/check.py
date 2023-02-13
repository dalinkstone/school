
friends = []
i = 1
while True:
    friend = input(f'What is the name of friend number {i}: ')
    if friend != 'end':
        friends.append(friend)
    else:
        break
    
    i += 1
print()
print('Your friends are:')
print(friends, sep='\n')
