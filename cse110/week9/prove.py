from yahooquery import Ticker
from rich.console import Console
from art import *
import os
from random import choice

console = Console()
affirmation = ['Good choice!', 'Great choose', 'Let\'s do it!', 'Right on!', 'Of course!', 'Certainly!', 'On it!', 'As you wish!', 'Sure thing!']
options = ['[purple]1. Browse Stock Catalog', '[purple]2. Add Stock', '[purple]3. View Selected Stocks', '[purple]4. Remove Stock', '[purple]5. Compute Total Investment Bid', '[purple]6. Quit']
stock_catalog = {'Exxon': 'XOM', 'Microsoft': 'MSFT', 'General Electric': 'GE', 'Procter&Gamble': 'PG', 'WalMart': 'WMT', 'Pfizer': 'PFE', 'Toyota': 'TM', 'JP Morgan': 'JPM', 'Intel': 'INTC', 'Cisco': 'CSCO', 'Wells Fargo': 'WFC', 'AT&T': 'T', 'Coca-Cola': 'KO', 'Pepsico': 'PEP', 'Verizon': 'VZ', 'Google': 'GOOG', 'Home Depot': 'HD', 'Qualcomm': 'QCOM', 'Dell': 'DELL', 'Oracle': 'ORCL', 'Goldman Sachs': 'GS', 'Apple': 'AAPL', 'Boeing': 'BA', 'Yahoo': 'YHOO', 'Nissan': 'NSANY', 'Target': 'TGT', 'McDonalds': 'MCD'}

print(text2art("yStockCart"))

console.print('[white on purple]Welcome to yStockCart![/]\n')

console.print('[purple]Please select one of the following options:\n')
console.print(*options, sep='\n')
print()

option = ""
stock_cart_names = []
stock_cart_num_shares = []
stock_cart_prices = []
accepted_options = [1, 2, 3, 4, 5, 6]
quit_now = False
while option != 6:
    try:
        option = int(input('What would you like to do?: '))
        print()
    except:
        continue

    if option not in accepted_options:
        console.print('[red]ERROR: Please enter a number corresponding to your desired action.\n')
    elif option == 6:
        console.print('[white on red]Thank you for using yStockCart! Come again![/]')
        quit()
    else:
        print('\n')
        console.print(f'[white on purple]{choice(affirmation)}[/]\n')


    if option == 1:
        os.system('cls')
        console.print('[white on purple]Our Catalog includes (but is not limited to):[/]')
        for (key,value) in stock_catalog.items():
            console.print(f'[purple]{key}: {value}')
        
        print()
        console.print('[purple]Please select one of the following options:\n')
        console.print(*options, sep='\n')
        print()
    
    elif option == 2:
        console.print('[white on purple]In order to add a stock to your cart, you must use the Ticker symbol.')
        console.print('[white on red]ATTENTION: Failure to use a proper Ticker Symbol will result in an error.\n')
        while True:
            add_stock = input('What stock would you like to add?: ')
            if not add_stock.isalpha():
                console.print('[red]ERROR: Ticker Symbols do not use numbers.')
            else:
                add_stock = add_stock.upper()
                break
        
        stock = Ticker(add_stock)
        stock_name = stock.quotes[add_stock]['displayName']
        stock_cart_names.append(stock_name)

        stock_cur_price = stock.quotes[add_stock]['regularMarketPrice']
        num_shares = 1
        console.print(f'[white on purple]The current price of {stock_name} is {stock_cur_price}.[/]\n')
        while True:
            num_shares = int(input('How many shares would you like?: '))
            if num_shares > 1000:
                console.print('[red]ERROR: The max number of shares is 1000 per buyer.\n')
            else:
                break
        
        print()

        console.print(f'[purple]The total value of the {num_shares} shares of {stock_name} is: {num_shares*stock_cur_price}.\nWe will add this to your cart.')
        stock_cart_prices.append(num_shares*stock_cur_price)

        print()
        console.print('[purple]Please select one of the following options:\n')
        console.print(*options, sep='\n')
        print()

    elif option == 3:
        os.system('cls')
        console.print('[purple]We can show you only the names of the stocks in your cart. Or we can show you the names and prices.\n')
        while True:
            option3_choice = input('Would you like to see the names of the stocks in your cart or everything?: ')
            print()
            if not option3_choice.isalpha():
                console.print('[red]ERROR: Input must be \'Names\' or \'Everything\'.\n')
            elif option3_choice.lower() == "names":
                print(*stock_cart_names, sep='\n')
                print()
                break
            elif option3_choice.lower() == "everything":
                print_dict = dict(zip(stock_cart_names, stock_cart_prices))
                print()
                print('\n'.join("{}: ${}".format(key, value) for key, value in print_dict.items()))
                print()
                break
            else:
                console.print('[red]ERROR: Input must be \'Names\' or \'Everything\'.\n')


        print()
        console.print('[purple]Please select one of the following options:\n')
        console.print(*options, sep='\n')
        print()

    elif option == 4:
        os.system('cls')
        console.print('[purple]In order to remove a stock from your cart, you must provide the list number as shown below.')
        console.print('[white on red]Failure to provide the list number as shown will result in an error.')

        print('\n'.join(f"{num+1}. {item}" for num, item in enumerate(stock_cart_names)))

        stock_enumeration = [num+1 for num, item in enumerate(stock_cart_names)]

        while True:
            try:
                stock_removal_num = int(input('Which number item would you like to remove?: '))
                if stock_removal_num in stock_enumeration:
                    break
                else:
                    console.print('[red]ERROR: Enter a number item.\n')
            except:
                console.print('[red]ERROR: Enter a number item.\n')

        while True: 
            try:
                stock_index_number = stock_removal_num - 1
                stock_cart_names.pop(stock_index_number)
                stock_cart_prices.pop(stock_index_number)
                console.print('[white on purple]That item has been removed from your cart.')
                break
            except:
                continue

        print()
        console.print('[purple]Please select one of the following options:\n')
        console.print(*options, sep='\n')
        print()

    elif option == 5:
        os.system('cls')
        console.print('[white on purple]It is time to compute the total amount due to purchase the stock investments in your cart.\nTo refresh your memory, this is what is currently in your cart:\n')

        compute_dict = dict(zip(stock_cart_names, stock_cart_prices))
        print('\n'.join("{}: ${}".format(key, value) for key, value in compute_dict.items()))
        print()


        console.print(f'[white on purple]Your total amount due is: {sum(stock_cart_prices)}')

        print()
        console.print('[purple]Please select one of the following options:\n')
        console.print(*options, sep='\n')
        print()
    
    else:
        print()
        console.print('[white on red]ERROR: That is not a valid number.')
        print()
        





        
        






