import os
import django
import random
from faker import Faker
from faker.providers import date_time, person, address, company
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "expense_tracker.settings")
django.setup()

from user_expense.models import UserData

fake = Faker()
fake.add_provider(date_time)
fake.add_provider(person)
fake.add_provider(address)
fake.add_provider(company)

def generate_user_data():
    fixed_salary = fake.random_number(digits=5)
    variable_salary = fake.random_number(digits=4)
    ctc = fixed_salary + variable_salary
    # Ensure that the start value is less than the stop value
    in_hand_min = min(variable_salary, fixed_salary, ctc)
    in_hand_max = max(variable_salary, fixed_salary, ctc)
    in_hand_salary = random.randint(in_hand_min, in_hand_max)

    return {
        'Name': fake.name(),
        'Date_of_birth': fake.date_of_birth(minimum_age=18, maximum_age=65),
        'Profession': fake.job(),
        'Address': fake.address(),
        'Fixed_salary': fixed_salary,
        'Variable_salary': variable_salary,
        'In_hand_salary': in_hand_salary,
        'CTC': ctc
    }


for _ in range(10):
    user_data = generate_user_data()
    UserData.objects.create(**user_data)