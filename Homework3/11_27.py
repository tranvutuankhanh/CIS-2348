# Name: Vu Tran
# Student ID: 2233511

# Create an dictionary to store the roster information
roster = {}

# get input from the user for each player's jersey number and rating, and store it in the dictionary
for i in range(5):
    jersey_number = int(input(f"Enter player {i + 1}'s jersey number:\n"))
    rating = int(input(f"Enter player {i + 1}'s rating:\n"))
    roster[jersey_number] = rating
    print()

# sort the jersey numbers in the roster and display the roster information
sorted_jersey_numbers = sorted(roster.keys())
print("ROSTER")
for jersey_number in sorted_jersey_numbers:
    print(f"Jersey number: {jersey_number}, Rating: {roster[jersey_number]}")

# allow the user to interact with the roster by providing a menu of options
option = ""
while option != "q":
    print("\nMENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")

    option = input("\nChoose an option:\n")

    # if the user selects the "o" option, display the roster information again
    if option == "o":
        sorted_jersey_numbers = sorted(roster.keys())
        print("\nROSTER")
        for jersey_number in sorted_jersey_numbers:
            print(f"Jersey number: {jersey_number}, Rating: {roster[jersey_number]}")

    # if the user selects the "a" option, prompt for a new player's jersey number and rating and add them to the roster
    elif option == "a":
        jersey_number = int(input("\nEnter a new player's jersey number:\n"))
        rating = int(input("Enter the player's rating:\n"))
        roster[jersey_number] = rating

    # if the user selects the "d" option, prompt for a jersey number and remove the player from the roster
    elif option == "d":
        jersey_number = int(input("\nEnter a jersey number:\n"))
        if jersey_number in roster:
            del roster[jersey_number]
        else:
            print("That player is not in the roster.")

    # if the user selects the "u" option, prompt for a jersey number and a new rating and update the roster
    elif option == "u":
        jersey_number = int(input("\nEnter a jersey number:\n"))
        if jersey_number in roster:
            new_rating = int(input("Enter a new rating for the player:\n"))
            roster[jersey_number] = new_rating
        else:
            print("That player is not in the roster.")

    # if the user selects the "r" option, prompt for a rating and display all players above that rating
    elif option == "r":
        rating = int(input("\nEnter a rating:\n"))
        print(f"\nABOVE {rating}")
        for jersey_number in sorted_jersey_numbers:
            if roster[jersey_number] > rating:
                print(f"Jersey number: {jersey_number}, Rating: {roster[jersey_number]}")

    # if the user selects the "q" option, exit the loop and end the program
    elif option == "q":
        break

    # if the user selects an invalid option, display an error message and prompt again
    else:
        print("\nInvalid option. Please try again.")
