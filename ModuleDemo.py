from module.CommonUtils import calculate_age

birth_year_input = int(input("Please enter your birth year : "))
age = calculate_age(birth_year_input)
print(f"You are {age} years old!")
