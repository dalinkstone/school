
account_names = []
balances = []

quit_option = ""
while quit_option == "":
    print('Enter the names and balances of bank accounts (type \'quit\' when done).')
    account = input('What is the name of this account?: ')
    if account == 'quit':
        break
    else:
        account_names.append(account)

        balance = float(input('What is the balance?: '))
        balances.append(balance)

print()
print('Account Information: ')
account_dict = dict(zip(account_names, balances))
print('\n'.join("{}: ${:.2f}".format(key, value) for key, value in account_dict.items()))

print()

print(f'Total: ${sum(balances)}')
print(f'Average: ${sum(balances)/len(balances)}')

    

