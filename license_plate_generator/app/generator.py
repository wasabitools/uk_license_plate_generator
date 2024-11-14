import random, string
from datetime import datetime
from .validators import validate_memory_tag, validate_date, validate_generated_plate


def calculate_age_identifier(date: str) -> str:
    date_value =  datetime.strptime(date,  "%d/%m/%Y")
    extracted_month =  date_value.month
    extracted_year = str(date_value.year)[-2:]

    if extracted_month < 9:
        return extracted_year
    
    return str(int(extracted_year) + 50)

def generate_suffix(length:int = 3) -> str:
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(length))

def generate_license_plate(memory_tag: str, date: str, license_plates: set) -> str:
    age_identifier = calculate_age_identifier(date)
    suffix = generate_suffix

    if not validate_memory_tag(memory_tag):
        print("Wrong memory tag provided")
    if not validate_date(date):
        print("Wrong date provided")

    license_plate = f"{memory_tag.upper()}{age_identifier} {suffix}"

    if license_plate not in license_plates and validate_generated_plate(license_plate):
        license_plates.add(license_plate)
        return license_plate

