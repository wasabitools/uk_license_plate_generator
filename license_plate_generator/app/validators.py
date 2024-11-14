import re
from datetime import datetime

def validate_memory_tag(memory_tag: str) -> bool:
    pattern = r"^[A-HK-PR-Y]{2}$"
    return bool(re.match(pattern, memory_tag.upper()))

def validate_date(date: str) -> bool:
    try:
        date_value = datetime.strptime(date, "%d/%m/%Y")
        return date_value <= datetime.now()
    except ValueError:
        return False
    
def validate_generated_plate(license_plate: str) -> bool:
    plate_format = r"^[A-HK-PR-Y]{2}\d{2} \W{3}$"
    return bool(re.match(plate_format, license_plate))