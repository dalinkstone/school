
print('Enter numbers. Enter 0 when finished.')

list_num = []
the_num = 0
num = ""
while num != the_num:
    num = int(input("Enter a number: "))
    if num != the_num:
        list_num.append(num)
    else:
        break

print()
print(f'The sum is: {sum(list_num)}')
print(f'The average is: {sum(list_num)/len(list_num)}')
print(f'The max is: {max(list_num)}')
