import datetime


# def welcome_user():
#     print("Hello User!")
#     print("Python welcomes you to the world!")
#
#
# welcome_user()


# def welcome_user(name):
#     print(f"Hello {name}!")
#     print("Python welcomes you to the world!")
#
#
# welcome_user(input("Please enter your name : "))

# def welcome_user(first_name, last_name):
#     print(f"Hi {first_name} {last_name}!")
#     print("Python welcomes you to the world!")
#
#
# input_first_name = input("Please enter your first name : ")
# input_last_name = input("Please enter your last name : ")
#
# # welcome_user(input_last_name, input_first_name)
#
# # welcome_user(input_first_name, input_last_name)
#
# # welcome_user(first_name=input_first_name,last_name=input_last_name)
#
# welcome_user(last_name=input_last_name, first_name=input_first_name)


def welcome_user(first_name, last_name, birth_year):
    print(f"Hi {first_name} {last_name}!")
    print(f"You are {calculate_age(birth_year)} years old!")


def calculate_age(year):
    return datetime.datetime.now().year - year


input_first_name = input("Please enter your first name : ")
input_last_name = input("Please enter your last name : ")
input_dob = int(input("Please enter your birth year : "))

welcome_user(last_name=input_last_name, first_name=input_first_name, birth_year=input_dob)
