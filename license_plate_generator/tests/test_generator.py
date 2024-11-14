import pytest
from generator import generate_license_plate, calculate_age_identifier
from exceptions import InvalidMemoryTagError, InvalidDateError

@pytest.mark.parametrize(
    "date_input, expected",
    [
        ("01/01/2001", "01"),
        ("15/09/2001", "51"),
        ("01/12/2002", "52"),
        ("15/08/2005", "05"),
    ]
)
def test_calculate_age_identifier(date_input, expected):
    assert calculate_age_identifier(date_input) == expected

@pytest.mark.parametrize(
    "memory_tag, date, expected_output",
    [
        ("AB", "01/01/2001", True),
        ("XY", "15/09/2005", True),
        ("AA", "01/01/2050", False),
        ("", "01/01/2001", False),
    ]
)
def test_generate_license_plate(memory_tag, date, expected_output):
    license_plates = set()
    if expected_output:
        license_plate = generate_license_plate(memory_tag, date, license_plates)
        assert license_plate is not None
        assert license_plate not in license_plates
    else:
        with pytest.raises((InvalidMemoryTagError, InvalidDateError)):
            generate_license_plate(memory_tag, date, license_plates)
