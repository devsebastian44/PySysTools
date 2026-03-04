import calendar


def display_monthly_calendar(year: int, month: int):
    """Generates and shows the calendar of the specified month and year."""
    print(calendar.month(year, month))


if __name__ == "__main__":
    current_year = 2023
    current_month = 3
    display_monthly_calendar(current_year, current_month)