import re
from datetime import datetime
from exceptions import FutureDateError, InvalidDateError, InvalidMemoryTagError, InvalidLicensePlateError

def validate_memory_tag(memory_tag: str) -> bool:
    pattern = r"^[A-HK-PR-Y]{2}$"
    if memory_tag is None:
        raise InvalidMemoryTagError("Memory tag can't be empty. Please provide a memory tag.")
    if re.match(pattern, memory_tag.upper()) is False:
        raise InvalidMemoryTagError("Provided memory tag is not correct.")
    return True

def validate_date(date: str) -> bool:
    if date is None:
        raise InvalidDateError("Date can't be empty. Please provide a date.")
    try:
        date = datetime.strptime(date, "%d/%m/%Y")
        if date <= datetime.now():
            raise FutureDateError("Provided date can't be a future date.")
    except ValueError:
        raise InvalidDateError("Date format should be dd/mm/yyyy.")
    
    return True
    
def validate_generated_plate(license_plate: str) -> bool:
    plate_format = r"^[A-HK-PR-Y]{2}\d{2} \W{3}$"
    if re.match(plate_format, license_plate) is False:
        raise InvalidLicensePlateError("Generated license plate is incorrect.")
    return True