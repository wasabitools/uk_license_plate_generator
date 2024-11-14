import pytest

from app.validators import validate_date, validate_memory_tag
from app.exceptions import FutureDateError, InvalidDateError, InvalidMemoryTagError

@pytest.mark.parametrize(
    "memory_tag, expected",
    [
        ("AB", True),
        ("ZZ", False),
        ("IY", False),
        ("QQ", False),
        ("XX", True),
        (None, False),
        ("", False),
    ]
)
def test_validate_memory_tag(memory_tag, expected):
    if memory_tag in [None, ""]:
        with pytest.raises(InvalidMemoryTagError):
            validate_memory_tag(memory_tag)
    elif expected:
        assert validate_memory_tag(memory_tag)
    else:
        with pytest.raises(InvalidMemoryTagError):
            validate_memory_tag(memory_tag)


@pytest.mark.parametrize(
    "date_input, expected",
    [
        ("25/09/2001", True),
        ("31/02/2001", False),
        ("25/09/2100", False),
        ("01/01/2020", True),
        (None, False),
    ]
)
def test_validate_date(date_input, expected):
    if expected:
        assert validate_date(date_input)
    else:
        with pytest.raises((InvalidDateError, FutureDateError)):
            validate_date(date_input)
