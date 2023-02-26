with open('cse110\week11\hr_system.txt', 'r') as hr_file:
    for line in hr_file:
        print("Name: "+line.split(" ")[0]+", Title: "+line.split(" ")[2])
