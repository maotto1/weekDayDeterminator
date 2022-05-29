import datetime
import math

MONTH_NUMBERS = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
WEEKDAY_NAMES_GERMAN = ["Sonntag", "Montag", "Dienstag", "Mitwoch", "Donnerstag", "Freitag", "Samstag"]


def print_date(date: datetime.date, result):
    print(f'Der {date.strftime("%d.%m.%Y")} ist ein {result}')


def is_leap_year(year: datetime.date.year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def calculate_week_day(day: datetime.date):
    if day < datetime.date.fromisoformat('1582-10-15'):
        raise ValueError("date too early")
    daily_number = day.day % 4
    monthly_number = MONTH_NUMBERS[day.month - 1]
    leap_adjustment = -1 if (day.month <= 2 and is_leap_year(day.year)) else 0
    century = math.floor(day.year / 100)
    year_short = day.year % 100
    century_number = 2 * (3 - (century % 4))
    decade_number = (year_short + math.floor(year_short / 4)) % 7
    return (daily_number + monthly_number + century_number + decade_number + leap_adjustment) % 7


if __name__ == '__main__':
    today = datetime.date.today()
    week_day = WEEKDAY_NAMES_GERMAN[calculate_week_day(today)]
    print_date(today, week_day)
