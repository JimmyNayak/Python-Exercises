from datetime import datetime


def calculate_age(birth_year):
    return datetime.now().year - birth_year
