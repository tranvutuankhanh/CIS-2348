# Homework3 Zybooks project.

#10_11
This project defines a Python class called FoodItem that represents a food 
item with nutritional information. It includes a constructor to initialize the name, fat,
carbohydrates, and protein content of a food item, as well as methods to calculate the number of calories 
per serving and print out nutritional information.

The FoodItem constructor initializes a food item with a name, fat content, carbohydrates content, and protein content. 
If any of these parameters are not specified, they are set to default values of "None", 0.0, 0.0, and 0.0, respectively.

The FoodItem class includes two methods:

The print_info() method prints out the nutritional information of a FoodItem object,
including its name, fat content, carbohydrates content, and protein content.

The get_calories(num_servings) method calculates the number of calories in a given number of servings of a FoodItem.
The method takes one parameter, num_servings, which specifies the number of servings to calculate calories for.

#10_15
This is a project that implements a Team class in Python. 
The Team class contains properties for a team name, number of team wins, and number of team losses. 
The class also contains a method get_win_percentage() that calculates the percentage of wins for a team.

To create a new Team object, simply call the class constructor 
and pass in the team name, number of wins, and number of losses

To get the team's win percentage, call the get_win_percentage() method.

The get_win_percentage() method returns a floating-point value representing the team's win percentage.

Print out a message indicating whether the team has a winning or losing average using the __str__() method.

The output will be either "Congratulations, Team {team name} has a winning average!" 
or "Team {team name} has a losing average." depending on the team's win percentage.

#10_17
This is a simple project that demonstrates the use of a Python class 
to create objects that represent items for purchase, and calculate the total cost of those items.

To use this project, simply run the Python script item_to_purchase.py in a Python environment. 
The script will prompt the user to enter information for two items, including the item name, price, and quantity.
It will then create two objects of the ItemToPurchase class, calculate the total cost of the items, and output the result.

#10_19
1.The ItemToPurchase class contains the following attributes:

item_name: a string representing the name of the item (default: "none")
item_price: a float representing the price of the item (default: 0)
item_quantity: an integer representing the quantity of the item (default: 0)
item_description: a string representing the description of the item (default: "none")
The ItemToPurchase class also contains the following methods:
print_item_description(): prints the item description for an ItemToPurchase object.

2.The ShoppingCart class contains the following attributes:

customer_name: a string representing the name of the customer (default: "none")
current_date: a string representing the current date (default: "January 1, 2016")
cart_items: a list of ItemToPurchase objects representing the items in the shopping cart (default: [])
The ShoppingCart class also contains the following methods:

add_item(item): adds an ItemToPurchase object to the shopping cart.
remove_item(item_name): removes an ItemToPurchase object from the shopping cart by name.
modify_item(item): modifies an ItemToPurchase object in the shopping cart.
get_num_items_in_cart(): returns the total quantity of items in the shopping cart.
get_cost_of_cart(): returns the total cost of items in the shopping cart.
print_total(): prints the total cost of items in the shopping cart.
print_descriptions(): prints the descriptions of all items in the shopping cart.

To use this program, run the shopping_cart.py file in your Python environment. 
You will be prompted to enter the customer's name and today's date. 
Then, you will be presented with a menu of options to manipulate the shopping cart.
Choose an option and follow the prompts to add, remove, modify, or view items in the shopping cart.
The program will continue to run until you choose the "q" option to quit.

#11_18
This program takes a list of integers as input, and outputs 
the non-negative integers in ascending order.

You will then be prompted to enter a list of integers separated by spaces.
Once you have entered the list, press enter and 
the program will output the non-negative integers in ascending order.

#11_22
This is a simple Python program that reads a list of words from the user and outputs each word along with its frequency. 
The program is useful for analyzing text data and identifying the most common words in a given document or corpus.

The program uses a dictionary to keep track of the frequency of each word in the input list. 
It loops through each word in the list and adds it to the dictionary if it doesn't already exist, 
or increments its count if it does. Finally, it prints out each word and its frequency.

#11_27
This is a Python program that stores roster and rating information for a soccer team. 
Coaches can rate players during tryouts to ensure a balanced team. 
The program allows the user to input five pairs of numbers, where each pair represents a player's jersey number and rating. 
The program stores the jersey numbers and ratings in a dictionary and outputs them in ascending order by jersey number.

The program also has a menu of options for the user to modify the roster.
The options include adding a player, removing a player, updating a player's rating,
outputting players above a certain rating, and outputting the roster.



