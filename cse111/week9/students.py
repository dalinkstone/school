import csv


def main():

    result = read_dictionary("students.py")

    nums = list(result.keys())

    while True:
        try:
            num = int(input("Enter a I-Number: "))
        except:
            continue

        if num in nums:
            student = result[num]
            print(student)
            break
        else:
            print('That student is not in the database. Try again')

    return result


def read_dictionary(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """

    dict = {}
    

    with open("students.csv", "rt") as file:

        next(file)

        reader = csv.reader(file)

        for row in reader:

            key = int(row[0])

            dict[key] = row[1]

    return dict

if __name__ == "__main__":
    main()