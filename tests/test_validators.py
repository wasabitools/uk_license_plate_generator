import pytest

from app.exceptions import InvalidDateError, InvalidMemoryTagError
from app.validators import validate_date, validate_memory_tag


@pytest.mark.parametrize(
    "memory_tag, expected",
    [
        ("AB", True),
        ("XY", True),
    ],
)
def test_validate_memory_tag_valid(memory_tag, expected):
    assert validate_memory_tag(memory_tag) == expected


@pytest.mark.parametrize(
    "memory_tag,  expected_exception, expected_message",
    [
        ("ZZ", InvalidMemoryTagError, "Provided memory tag is not correct."),
        (
            "",
            InvalidMemoryTagError,
            "Memory tag can't be empty. Please provide a memory tag.",
        ),
        ("A1", InvalidMemoryTagError, "Provided memory tag is not correct."),
    ],
)
def test_validate_memory_tag(memory_tag, expected_exception, expected_message):
    with pytest.raises(expected_exception, match=expected_message):
        validate_memory_tag(memory_tag)


@pytest.mark.parametrize(
    "date, expected",
    [
        ("01/01/2020", True),
        ("28/02/2027", "Provided date can't be a future date."),
    ],
)
def test_validate_date(date, expected):
    if expected:
        assert validate_date(date)
    else:
        with pytest.raises(InvalidDateError):
            validate_date(date)
