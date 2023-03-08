#Name: Vu Tran
#Student ID: 2233511

from datetime import datetime

current_date = datetime.now()

# Read input from file
with open('inputDates.txt') as f:
    input_lines = f.readlines()

dates = []

for date_str in input_lines:
    date_str = date_str.strip()
    if date_str == '-1':
        break

    month_start = 0
    month_end = date_str.find(' ')
    day_start = month_end + 1
    day_end = date_str.find(',', day_start)
    year_start = day_end + 2
    year_end = year_start + 4

    try:
        month = date_str[month_start:month_end]
        day = date_str[day_start:day_end]
        year = date_str[year_start:year_end]
        date_str = f"{month} {day}, {year}"
        date = datetime.strptime(date_str, '%B %d, %Y')
        if date <= current_date:
            dates.append(date)
    except ValueError:
        pass

# Print output to console
for date in dates:
    print(date.strftime('%-m/%-d/%Y'))
