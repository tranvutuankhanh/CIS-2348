#Name: Vu Tran
#Student ID: 2233511

#This is 3.19 homework on Zybooks

#Part 1: Ask users input height and width.
# Then calculate and output the area of wall.

print('Enter wall height (feet):')
height = int(input())

print('Enter wall width (feet):')
width = int(input())

area = height * width

print(f'Wall area: {area} square feet')

#Part 2: Calculate and output the amount of paint
# in gallons needed to paint the wall

paint_needed = area/350.00

print('Paint needed: %.2f gallons' % paint_needed)

#Part 3: Calculate and output the number of 1 gallon
# cans needed to paint the wall.

cans = int(round(paint_needed))

print(f'Cans needed: {cans} can(s)')

#Part 4: Calculate and output the total cost of the paint
# cans depending on which color is chosen.

print('\nChoose a color to paint the wall:')
color = str(input())

paint_color= {
'red': 35,
'blue': 25,
'green': 23
}

print('Cost of purchasing {} paint: $'.format(color), end="")
print(paint_color[color] * cans)
