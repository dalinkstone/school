import math

w = None
a = None
d = None

w = int(input("Enter the width of the tire in mm (ex 205): "))
a = int(input("Enter the aspect ratio of the tire (ex 60): "))
d = int(input("Enter the diameter of the wheel in inches (ex 215): "))

volume = ((math.pi*(w*w)*a)*((w*a)+(2540*d))/10000000000)

print(f"\nThe approximate volume is {volume:.2f} liters")