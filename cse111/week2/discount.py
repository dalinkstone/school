from datetime import datetime

day = datetime.now()

day_of_week = day.weekday()

subtotal = float(input("Please enter the subtotal: "))

discount = subtotal * .10


if ((day_of_week == 1 or day_of_week == 2) and subtotal > 50.00):
    subtotal = subtotal - (subtotal * .10)
    print(f"Discount amount: {discount:.2f}")
    print(f"Sales tax amount: {subtotal*.06:.2f}")
    print(f"Total: {subtotal+subtotal*.06:.2f}")
else:
    print(f"Sales tax amount: {subtotal*.06:.2f}")
    print(f"Total: {subtotal+subtotal*.06:.2f}")



