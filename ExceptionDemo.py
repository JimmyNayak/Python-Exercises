import datetime


def calculate_age(year):
    return datetime.datetime.now().year - year


try:
    birth_year = int(input("Please enter your birth year : "))
    print(f"You are {calculate_age(birth_year)} years old!")
except Exception as e:
    print(e)
