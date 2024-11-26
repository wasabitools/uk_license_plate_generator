import pytest

from app.generators import calculate_age_identifier


@pytest.mark.parametrize(
    "date, expected",
    [
        ("01/04/2010", "10"),
        ("01/10/2010", "60"),
        ("01/01/2020", "20"),
        ("01/12/2021", "71"),
    ],
)
def test_calculate_age_identifier_valid(date, expected):
    assert calculate_age_identifier(date) == expected


@pytest.mark.parametrize(
    "date, expected_exception, expected_message",
    [
        (None, ValueError, "Date can't be empty. Please provide a date."),
        (
            "28-02-2010",
            ValueError,
            "Invalid date format: 28-02-2010. Please use the format dd/mm/yyyy.",
        ),
        (
            "40/04/2010",
            ValueError,
            "Invalid date format: 40/04/2010. Please use the format dd/mm/yyyy.",
        ),
        (
            "invalid_date",
            ValueError,
            "Invalid date format: invalid_date. Please use the format dd/mm/yyyy.",
        ),
    ],
)
def test_calculate_age_identifier_invalid(date, expected_exception, expected_message):
    with pytest.raises(expected_exception, match=expected_message):
        calculate_age_identifier(date)
