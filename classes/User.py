from datetime import datetime


class User:
    birth_year = datetime.now().year

    def __init__(self, birth_year):
        self.birth_year = birth_year

    def calculate_age(self):
        print(f"You are {datetime.now().year - self.birth_year} years old!")

    def show_user(self):
        print("Hello user!")
