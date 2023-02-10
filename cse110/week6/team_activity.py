acceptable_riders = ['1', '2']
acceptable_age = 18
height_limit = 36
num_riders = []

while True:
    try:
        riders = input("How many riders will there be today?: ")
        riders_input = riders.split()
        for rider in riders_input:
            if rider in acceptable_riders:
                num_riders.append(rider)
                break
        if num_riders[0] in acceptable_riders:
            break
    except:
        print('There can only be 1 or 2 riders! Come back later')
        quit()
        
if num_riders[0] == '2':
    while True:
        try:
            age_first = int(input("How old is the first rider?: "))
            break
        except ValueError:
            print("Error: Ages must be only numbers")


    while True:
        try:
            age_second = int(input("How old is the second rider?: "))
            break
        except ValueError:
            print("Error: Ages must be only numbers")

    if age_first and age_second < acceptable_age:
        print('Nice try kiddos. Come back when you have someone over 18 with you!')
        quit()

    while True:
        try:
            height_first = int(input("How tall is the first rider in inches?: "))
            break
        except ValueError:
            print("Error: Height must be only a whole number!")

    while True:
        try:
            height_second = int(input("How tall is the second rider in inches?: "))
            break
        except ValueError:
            print("Error: Height must be only a whole number!")

    if height_first or height_second < height_limit:
        print('No one under 36 inches can ride this ride. That\'d be too dangerous!')
        quit()
    else:
        print('Enjoy the ride!')
        quit()

if num_riders[0] == 1:
    while True:
        try:
            age_first = int(input("How old is the rider?: "))
            break
        except ValueError:
            print("Error: Ages must be only numbers")
    
    if age_first < acceptable_age:
        print('You have to be at least 18 years old to be on this ride!')
    
    while True:
        try:
            height_first = int(input("How tall is the rider in inches?: "))
            break
        except ValueError:
            print("Error: Height must be only a whole number!")
        
    if height_first < height_limit:
        print('No one under 36 inches can ride this ride. That\'d be too dangerous!')
        quit()
    else:
        print('Enjoy the ride!')
        quit()



