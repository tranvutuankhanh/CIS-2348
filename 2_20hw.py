#Name: Vu Tran
#Student ID: 2233511

# This is 2.20 homework on Zybooks

#Part 1: Input from user
print('Enter amount of lemon juice (in cups):')
lemon = float(input())

print('Enter amount of water (in cups):')
water = float(input())

print('Enter amount of agave nectar (in cups):')
agave_nectar = float(input())

print('How many servings does this make?')
servings = float(input())

#Print the output.
print("\nLemonade ingredients - yields {:.2f} servings".format(servings))
print("{:.2f} cup(s) lemon juice" .format(lemon))
print("{:.2f} cup(s) water".format(water))
print("{:.2f} cup(s) agave nectar".format(agave_nectar))

#Part 2: Input a new servings and output new ingredients and serving size.
print('\nHow many servings would you like to make?')
desired = float(input())

lemon1 = (lemon * desired)/servings
water1 = (water * desired)/servings
agave_nectar1 = (agave_nectar * desired)/servings

print("\nLemonade ingredients - yields {:.2f} servings".format(desired))
print("{:.2f} cup(s) lemon juice" .format(lemon1))
print("{:.2f} cup(s) water".format(water1))
print("{:.2f} cup(s) agave nectar".format(agave_nectar1))

#Part 3: Convert cup(s) to gallons
print("\nLemonade ingredients - yields {:.2f} servings".format(desired))
print("{:.2f} gallon(s) lemon juice" .format(lemon1/16))
print("{:.2f} gallon(s) water".format(water1/16))
print("{:.2f} gallon(s) agave nectar".format(agave_nectar1/16))
