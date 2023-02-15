# Name: Vu Tran
# Student ID: 2233511

# This is 5.22 homework on Zybooks

print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")

print("\nSelect first service:")
first_service = input()
print("Select second service:")
second_service = input()

total = 0

print()

print("Davy's auto shop invoice\n")
if first_service == "Oil change":
    print("Service 1: Oil change, $35")
    total = total + 35
elif first_service == "Tire rotation":
    print("Service 1: Tire rotation, $19")
    total = total + 19
elif first_service == "Car wash":
    print("Service 1: Car wash, $7")
    total = total + 7
elif first_service == "Car wax":
    print("Service 1: Car wax, $12")
    total = total + 12
elif first_service == "-":
    print("Service 1: No service")
else:
    print("Service 1: Invalid entry")

if second_service == "Oil change":
    print("Service 2: Oil change, $35")
    total=total+35
elif second_service == "Tire rotation":
    print("Service 2: Tire rotation, $19")
    total=total+19
elif second_service == "Car wash":
    print("Service 2: Car wash, $7")
    total=total+7
elif second_service == "Car wax":
    print("Service 2: Car wax, $12")
    total=total+12
elif second_service == "-":
    print("Service 2: No service")
else:
    print("Service 2: Invalid entry")

print(f'\nTotal: ${total}')
