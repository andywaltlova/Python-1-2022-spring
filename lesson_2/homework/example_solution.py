import calendar

year = int(input('Enter year in YYYY format: '))
month = int(input('Enter month in MM format: '))
day = int(input('Enter day in DD format: '))

weekday_num = calendar.weekday(year, month, day)
weekday_str = calendar.day_name[weekday_num]

print(f'{day}-{month}-{year} was {weekday_str}')

# If you really want to have DD-MM-YYYY format, including zeros in day and month
# Oficcial docs https://docs.python.org/3/library/string.html#formatspec
# However other sources from google can have better examples

print(f'{day:02d}-{month:02d}-{year} was {weekday_str}')

