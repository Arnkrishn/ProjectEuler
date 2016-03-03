from datetime import date, timedelta, datetime

def count_sundays(start_date, end_date):
    sunday_count = 0
    run_date = start_date
    leap_year = False

    while run_date <= end_date:
        year = run_date.year
        month = run_date.month
        if year % 400 == 0 or year % 4 == 0:    # Check leap year
            leap_year = True
        else:
            leap_year = False

        if month in (4, 6, 9, 11):
            delta = 30
        elif month == 2 and leap_year:
            delta = 29
        elif month == 2 and not leap_year:
            delta = 28
        else:
            delta = 31

        run_date = run_date + timedelta(days=delta)
        if run_date.weekday() == 6:
            sunday_count += 1

    return sunday_count


#Test
print count_sundays(datetime(1901, 1, 1), datetime(2000, 12, 31))
