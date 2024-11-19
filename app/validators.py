import re
from datetime import datetime
from exceptions import (
    FutureDateError,
    InvalidDateError,
    InvalidMemoryTagError,
)


def validate_memory_tag(memory_tag: str) -> bool:
    pattern = r"^[A-HJ-PR-Y]{2}$"
    if not memory_tag:
        raise InvalidMemoryTagError(
            "Memory tag can't be empty. Please provide a memory tag."
        )
    if re.match(pattern, memory_tag.upper()) is None:
        raise InvalidMemoryTagError("Provided memory tag is not correct.")
    return True


def validate_date(date: str) -> bool:
    try:
        date = datetime.strptime(date, "%d/%m/%Y").date()
        today = datetime.now().date()
        if date > today:
            raise FutureDateError("Provided date can't be a future date.")
    except ValueError as e:
        raise InvalidDateError("Date format should be dd/mm/yyyy.") from e

    return True
