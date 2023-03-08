#Vu Tran
#Student ID: 2233511

#Part A for Code problem 02

from datetime import datetime

# Get the current date
current_date = datetime.now()

# Initialize a list to store the valid dates
dates = []

# Read dates from user input until -1 is entered
while True:
    date_str = input().strip()
    if date_str == '-1':
        break

    # Extract month, day, and year from the input string
    month_start = 0
    month_end = date_str.find(' ')
    day_start = month_end + 1
    day_end = date_str.find(',', day_start)
    year_start = day_end + 2
    year_end = year_start + 4

    # Parse the date using datetime.strptime()
    try:
        # Construct a string in the format '%B %d, %Y'
        # and use datetime.strptime() to parse it
        month = date_str[month_start:month_end]
        day = date_str[day_start:day_end]
        year = date_str[year_start:year_end]
        date_str = f"{month} {day}, {year}"
        date = datetime.strptime(date_str, '%B %d, %Y')

        # Check if the date is before or equal to the current date,
        # and add it to the list if it is
        if date <= current_date:
            dates.append(date)
    except ValueError:
        # If the date string couldn't be converted to a datetime object, ignore it
        pass

# Output the valid dates in the format M/D/YYYY
for date in dates:
    print(date.strftime('%-m/%-d/%Y'))

