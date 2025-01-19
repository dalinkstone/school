import math
from datetime import date
import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type

w = None
a = None
d = None
phone = None
number = None

day = date.today()

w = int(input("Enter the width of the tire in mm (ex 205): "))
a = int(input("Enter the aspect ratio of the tire (ex 60): "))
d = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = ((math.pi*(w*w)*a)*((w*a)+(2540*d))/10000000000)

print(f"The approximate volume is {volume:.2f} liters")

while phone != True:
    try:
        number = input("\nIf you would like to buy the tires, please enter a valid phone number: ")
        phone = carrier._is_mobile(number_type(phonenumbers.parse(number)))
        break
    except:
        print("Must include your country code and be an active mobile number!")

with open("volumes.txt", "at") as volumes:
    print(f"{day}, {w}, {a}, {d}, {volume:.2f}, {number}", file=volumes)