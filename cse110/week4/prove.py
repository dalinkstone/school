from prettytable import PrettyTable as pt
import time

tb = pt()

tb.field_names = ['Item Name', 'Child\'s Meal', 'Adult\'s Meal', 'Drink']

tb.add_row(['Grass Fed Beef Rib Eye', 8.99, 16.99, 1.99])
tb.add_row(['Mac \'n Cheese', 5.99, 10.99, 1.99])
tb.add_row(['Borscht', 7.99, 12.99, 1.99])

childs_meal_list = [8.99, 5.99, 7.99]
adults_meal_list = [16.99, 10.99, 12.99]

print(tb)
while True:
    try:
        childs_meal = float(input('What is the price of the child\'s meal you want?: '))
    except ValueError:
        print('ERROR: Input must be a float (##.##) of a single meal selection. Try again.')
        continue

    if childs_meal in childs_meal_list:
        break
    else:
        print('ERROR: Input meal price is not on our menu! Please select a menu item.')
        continue


while True:
    try:
        adults_meal = float(input('What is the price of the adult\'s meal you want?: '))
    except ValueError:
        print('ERROR: Input must be a float (##.##) of a single meal selection. Try again.')
        continue
    
    if adults_meal in adults_meal_list:
        break
    else:
        print('ERROR: Input meal price is not on our menu! Please select a menu item.')
        continue

while True:
    try:
        drinks = int(input('How many drinks would you like?: '))
    except ValueError:
        print('ERROR: Input must be an integer (##). Try again.')
        continue
    break

while True:
    try:
        num_children = int(input('Number of children: '))
    except ValueError:
        print('ERROR: Input must be an integer (##). Try again.')
        continue
    break

while True:
    try:
        num_adults = int(input('Number of adults: '))
    except ValueError:
        print('ERROR: Input must be an integer (##). Try again.')
        continue
    break

while True:
    try:
        sales_tax_rate = int(input('Sales Tax Rate: '))
    except ValueError:
        print('ERROR: Input must be an integer (##). Try again.')
        continue
    break

meal_subtotal = round((childs_meal * num_children) + (adults_meal + num_adults) + (drinks * 2.00),2)
sales_tax = round(meal_subtotal * (sales_tax_rate/100), 2)
total_price = round(meal_subtotal + sales_tax, 2)

print('\n')

animation = ['Processing transaction   ', 'Processing transaction.  ', 'Processing transaction.. ', 'Processing transaction...', 'Processing transaction   ']
num = 0
while num < (17*1.5):
    print(animation[num % len(animation)], end="\r")
    time.sleep(0.1)
    num += 1

print('\n')


print(f'Subtotal:   ${meal_subtotal}')
print(f'Sales Tax:  ${sales_tax}')
print(f'Total:      ${total_price}')


while True:
    try:
        payment_amount = float(input('What is the payment amount?: '))
    except ValueError:
        print('ERROR: Input must be a number! Try again.')
        continue

    if payment_amount < total_price:
        print('We do not accept partial payment. Payment must be in full or over the total price.')
        continue
    else:
        break

change = round(payment_amount - total_price, 2)

print(f'Change:     ${change}')

