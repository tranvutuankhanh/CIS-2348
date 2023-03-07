# Name: Vu Tran
# Student ID: 2233511

import datetime


def parse_date(date_str):
    # Check if the input string matches the expected date format
    if date_str.find(",") != -1:
        # Extract the month, day, and year using the find() method
        comma_pos = date_str.find(",")
        month_day = date_str[:comma_pos].strip()
        year = date_str[comma_pos + 1:].strip()

        if month_day.find(" ") != -1:
            space_pos = month_day.find(" ")
            month = month_day[:space_pos].strip()
            day = month_day[space_pos + 1:].strip()
        else:
            # Handle the case where the day is not separated by a space
            month = month_day
            day = "1"

        # Convert the extracted values to a datetime object
        try:
            Date = datetime.datetime.strptime(f"{month} {day} {year}", "%B %d %Y")
            current_date = datetime.datetime.now()
            # Check if the extracted date is before or equal to the current date
            if Date <= current_date:
                return Date.strftime("%-m/%-d/%Y")
        except ValueError:
            pass

    # Return None if the input string does not match the expected format
    return None


# Read dates from the input file
with open("inputDates.txt") as f:
    dates = f.readlines()

# Parse the dates and write the correct ones to the output file
with open("parsedDates.txt", "w") as f:
    for date in dates:
        date = date.strip()
        if date == "-1":
            break
        parsed_date = parse_date(date)
        if parsed_date is not None:
            f.write(parsed_date + "\n")
