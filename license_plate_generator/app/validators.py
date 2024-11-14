import re
from datetime import datetime

def validate_memory_tag(memory_tag: str) -> bool:
    memory_tag = memory_tag.upper()
    pattern = r"^[A-HK-PR-Y]{2}$"
    return bool(re.match(pattern, memory_tag))

def validate_date(date: str) -> bool:
    try:
        date_value = datetime.strptime(date, "%d/%m/%Y")
        return date_value <= datetime.now()
    except ValueError:
        return False