# Name: Vu Tran
# Student ID: 2233511

# This is Hw#1 on BlackBoard

print('Birthday Calculator')
print('Enter current day ')

current_month = int(input('Month: '))
current_day = int(input('Day: '))
current_year = int(input('Year: '))
print()

print('Enter your birthday ')
birth_month = int(input('Month: '))
birth_day = int(input('Day: '))
birth_year = int(input('Year: '))
print()



if (current_month > birth_month) or (current_month == birth_month and current_day >= birth_day):
    years = current_year - birth_year
else:
    years = current_year - birth_year - 1

if current_month == birth_month and current_day == birth_day:
    print('Happy Birthday')

if current_month > 12:
    print('Input current month error!')
elif current_day > 31:
    print('Input current day error!')
elif birth_month > 12:
    print('Input birth month error!')
elif birth_day > 31:
    print('Input birth day error!')
else:
    print('You are ' + str(years) + ' years old.')
