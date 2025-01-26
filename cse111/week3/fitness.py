# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime
import re
import math


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = None
    while True:
            gender = input("Please enter your gender (M or F): ").upper()
            if gender == 'M' or gender == 'F':
                break
            elif gender.isalpha() == False:
                print("There are only two genders and they begin with M or F. Try again.")
            elif len(gender) != 1:
                print("We only asked for a single letter.")
    
    birthdate = None
    while True:
        birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
        if re.search("\d\d\d\d[-]\d\d[-]\d\d", birthdate) != None:
            break
        else:
            print("Please enter your birthdate in the format of YYYY-MM-DD. Must be numbers.")

    weight = None
    while True: 
        try:
            weight = int(input("Enter your weight in U.S. pounds (###): "))
        except ValueError:
            print("Please input your weight as a whole number. Try Again.")
            continue
        else:
            break
    
    height_feet = None
    height_inches = None
    while True:
        height = input("Enter your height in U.S Feet and Inches (#'##): ")
        if re.search("[1-7][']\d$|[1-7][']10|[1-7][']11", height) != None:
            height_nums = re.findall(r'\d+', height)
            height_feet = int(height_nums[0])
            height_inches = int(height_nums[1])
            break
        else:
            print("Please input your height in the form of: FEET'INCHES. Try again.")
    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    kilo = kg_from_lb(weight)
    cm = cm_from_in(height_feet, height_inches)
    age = compute_age(birthdate)
    print(f"Age (years): {age}")
    print(f"Weight (kg): {kilo}")
    print(f"Height (cm): {cm}")
    print(f"Body mass index: {body_mass_index(kilo, cm)}")
    print(f"Basal metabolic rate (kcal/day): {basal_metabolic_rate(gender, kilo, cm, age)}")
    # Print the results for the user to see.
    pass


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    kg = round(pounds * 0.45359237, 1)
    return kg


def cm_from_in(feet, inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    cm = round(((feet * 12) + inches) * 2.54, 1)
    return cm


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = round((10000 * weight) / (height * height), 1)
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender == 'M':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    return round(bmr, 1)


# Call the main function so that
# this program will start executing.
main()