people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

young_age = 999

young_name = ""


for item in people:
    item_clean = item.split(" ")
    
    name = item_clean[0]
    age = int(item_clean[1])

    if age < young_age:

        young_age = age

        young_name = name


print(f'This is {young_name} and they are {young_age}')