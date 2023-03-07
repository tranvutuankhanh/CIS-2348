# Name: Vu Tran
# Student ID: 2233511

# input for the first equation
a = int(input())
b = int(input())
c = int(input())

# input for the second equation
d = int(input())
e = int(input())
f = int(input())

check = False
# Loop to go through the -10 to 10
for x in range(-10, 10):
    for y in range(-10, 10):
        # Equation
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)

            check = True
            # Break the loop
            break

if not check:
    print("No solution")
