# Name: Vu Tran
# Student ID: 2233511

# exact_change function definition
def exact_change(user_total):
    if user_total <= 0:
        return None, None, None, None, None
    else:
        num_dollars = user_total // 100
        user_total %= 100

        num_quarters = user_total // 25
        user_total %= 25

        num_dimes = user_total // 10
        user_total %= 10

        num_nickels = user_total // 5
        num_pennies = user_total % 5

        return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies


# main function definition
if __name__ == '__main__':
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)
    if num_dollars is None:
        print("no change")
    else:
        if num_dollars > 0:
            if num_dollars == 1:
                print('1 dollar')
            else:
                print(f'{num_dollars} dollars')

        if num_quarters > 0:
            if num_quarters == 1:
                print('1 quarter')
            else:
                print(f'{num_quarters} quarters')

        if num_dimes > 0:
            if num_dimes == 1:
                print('1 dime')
            else:
                print(f'{num_dimes} dimes')

        if num_nickels > 0:
            if num_nickels == 1:
                print('1 nickel')
            else:
                print(f'{num_nickels} nickels')

        if num_pennies > 0:
            if num_pennies == 1:
                print('1 penny')
            else:
                print(f'{num_pennies} pennies')
