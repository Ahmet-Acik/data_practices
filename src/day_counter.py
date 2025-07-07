"""
Day Counter Program
This program provides various functions to count days in different scenarios.
"""

from datetime import datetime, date, timedelta
import calendar


def days_between_dates(start_date, end_date):
    """
    Calculate the number of days between two dates.
    
    :param start_date: Start date (datetime.date or string in 'YYYY-MM-DD' format)
    :param end_date: End date (datetime.date or string in 'YYYY-MM-DD' format)
    :return: Number of days between the dates
    """
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
    
    delta = end_date - start_date
    return abs(delta.days)


def days_until_date(target_date):
    """
    Calculate the number of days until a target date from today.
    
    :param target_date: Target date (datetime.date or string in 'YYYY-MM-DD' format)
    :return: Number of days until the target date (negative if date has passed)
    """
    if isinstance(target_date, str):
        target_date = datetime.strptime(target_date, '%Y-%m-%d').date()
    
    today = date.today()
    delta = target_date - today
    return delta.days


def days_since_date(past_date):
    """
    Calculate the number of days since a past date.
    
    :param past_date: Past date (datetime.date or string in 'YYYY-MM-DD' format)
    :return: Number of days since the past date
    """
    if isinstance(past_date, str):
        past_date = datetime.strptime(past_date, '%Y-%m-%d').date()
    
    today = date.today()
    delta = today - past_date
    return delta.days


def days_in_month(year, month):
    """
    Get the number of days in a specific month and year.
    
    :param year: Year (integer)
    :param month: Month (integer, 1-12)
    :return: Number of days in the month
    """
    return calendar.monthrange(year, month)[1]


def days_in_year(year):
    """
    Get the number of days in a specific year.
    
    :param year: Year (integer)
    :return: Number of days in the year (365 or 366 for leap years)
    """
    return 366 if calendar.isleap(year) else 365


def is_leap_year(year):
    """
    Check if a year is a leap year.
    
    :param year: Year (integer)
    :return: True if leap year, False otherwise
    """
    return calendar.isleap(year)


def count_weekdays_between_dates(start_date, end_date):
    """
    Count the number of weekdays (Monday-Friday) between two dates.
    
    :param start_date: Start date (datetime.date or string in 'YYYY-MM-DD' format)
    :param end_date: End date (datetime.date or string in 'YYYY-MM-DD' format)
    :return: Number of weekdays between the dates
    """
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
    
    # Ensure start_date is before end_date
    if start_date > end_date:
        start_date, end_date = end_date, start_date
    
    weekdays = 0
    current_date = start_date
    
    while current_date <= end_date:
        if current_date.weekday() < 5:  # Monday=0, Sunday=6
            weekdays += 1
        current_date += timedelta(days=1)
    
    return weekdays


def count_weekends_between_dates(start_date, end_date):
    """
    Count the number of weekend days (Saturday-Sunday) between two dates.
    
    :param start_date: Start date (datetime.date or string in 'YYYY-MM-DD' format)
    :param end_date: End date (datetime.date or string in 'YYYY-MM-DD' format)
    :return: Number of weekend days between the dates
    """
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
    
    # Ensure start_date is before end_date
    if start_date > end_date:
        start_date, end_date = end_date, start_date
    
    weekends = 0
    current_date = start_date
    
    while current_date <= end_date:
        if current_date.weekday() >= 5:  # Saturday=5, Sunday=6
            weekends += 1
        current_date += timedelta(days=1)
    
    return weekends


def age_in_days(birth_date):
    """
    Calculate age in days from birth date to today.
    
    :param birth_date: Birth date (datetime.date or string in 'YYYY-MM-DD' format)
    :return: Age in days
    """
    if isinstance(birth_date, str):
        birth_date = datetime.strptime(birth_date, '%Y-%m-%d').date()
    
    today = date.today()
    delta = today - birth_date
    return delta.days


def add_days_to_date(start_date, days_to_add):
    """
    Add a specific number of days to a date.
    
    :param start_date: Start date (datetime.date or string in 'YYYY-MM-DD' format)
    :param days_to_add: Number of days to add (can be negative to subtract)
    :return: New date after adding the days
    """
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
    
    new_date = start_date + timedelta(days=days_to_add)
    return new_date


def get_day_of_week(input_date):
    """
    Get the day of the week for a given date.
    
    :param input_date: Date (datetime.date or string in 'YYYY-MM-DD' format)
    :return: Day of the week as string
    """
    if isinstance(input_date, str):
        input_date = datetime.strptime(input_date, '%Y-%m-%d').date()
    
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days[input_date.weekday()]


def display_calendar_month(year, month):
    """
    Display a calendar for a specific month and year.
    
    :param year: Year (integer)
    :param month: Month (integer, 1-12)
    :return: String representation of the calendar
    """
    return calendar.month(year, month)


def main():
    """
    Main function to demonstrate the day counting functions.
    """
    print("=== Day Counter Program ===\n")
    
    # Current date
    today = date.today()
    print(f"Today's date: {today}")
    print(f"Day of the week: {get_day_of_week(today)}")
    print()
    
    # Example calculations
    start_date = "2025-01-01"
    end_date = "2025-12-31"
    
    print(f"Days between {start_date} and {end_date}: {days_between_dates(start_date, end_date)}")
    print(f"Days until New Year 2026: {days_until_date('2026-01-01')}")
    print(f"Days since New Year 2025: {days_since_date('2025-01-01')}")
    print()
    
    # Current year info
    current_year = today.year
    current_month = today.month
    
    print(f"Days in {current_year}: {days_in_year(current_year)}")
    print(f"Is {current_year} a leap year? {is_leap_year(current_year)}")
    print(f"Days in current month ({current_month}/{current_year}): {days_in_month(current_year, current_month)}")
    print()
    
    # Weekday/weekend counting
    print(f"Weekdays between {start_date} and {end_date}: {count_weekdays_between_dates(start_date, end_date)}")
    print(f"Weekend days between {start_date} and {end_date}: {count_weekends_between_dates(start_date, end_date)}")
    print()
    
    # Example birth date calculation
    birth_date = "1990-01-01"
    print(f"Age in days for someone born on {birth_date}: {age_in_days(birth_date)} days")
    print()
    
    # Date arithmetic
    future_date = add_days_to_date(today, 100)
    print(f"Date 100 days from today: {future_date}")
    past_date = add_days_to_date(today, -100)
    print(f"Date 100 days ago: {past_date}")
    print()
    
    # Display current month calendar
    print("Current month calendar:")
    print(display_calendar_month(current_year, current_month))


if __name__ == "__main__":
    main()


# Calculate days for each date pair
day_counts = []

result1 = days_between_dates("2025-05-19", "2025-07-07")
print(f"Days between 2025-05-19 and 2025-07-07: {result1}")
day_counts.append(result1)

result2 = days_between_dates("2025-03-14", "2025-05-26")
print(f"Days between 2025-03-14 and 2025-05-26: {result2}")
day_counts.append(result2)

result3 = days_between_dates("2025-03-15", "2025-05-27")
print(f"Days between 2025-03-15 and 2025-05-27: {result3}")
day_counts.append(result3)

result4 = days_between_dates("2025-04-14", "2025-05-28")
print(f"Days between 2025-04-14 and 2025-05-28: {result4}")
day_counts.append(result4)

result5 = days_between_dates("2025-02-27", "2025-05-28")
print(f"Days between 2025-02-27 and 2025-05-28: {result5}")
day_counts.append(result5)

result6 = days_between_dates("2025-04-03", "2025-06-02")
print(f"Days between 2025-04-03 and 2025-06-02: {result6}")
day_counts.append(result6)

# Calculate and display the average
average_days = sum(day_counts) / len(day_counts)
print(f"\nAll day counts: {day_counts}")
print(f"Total days: {sum(day_counts)}")
print(f"Number of calculations: {len(day_counts)}")
print(f"Average days: {average_days:.2f}")
