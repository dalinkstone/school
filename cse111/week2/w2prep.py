import math

items = int(input("Enter the number of items: "))
per_box = int(input("\nEnter the number of items per box: "))

print(f"For {items}, packing {per_box} items in each box, you will need {math.ceil(items/per_box)}.")