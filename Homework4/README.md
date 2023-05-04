# Homework4 Readme

## 12_7
This Python script calculates the fat-burning heart rate for a user based on their age.

The script consists of two main functions: get_age() and fat_burning_heart_rate(age).

get_age(): Prompts the user to input their age and checks if it is within the acceptable range (18 to 75). If the age is valid, it returns the age; otherwise, it raises a ValueError with a message "Invalid age."

fat_burning_heart_rate(age): Takes the age as a parameter and calculates the fat-burning heart rate using the formula (220 - age) * 0.7.

## 12_9
The Age Incrementer is a simple Python script that accepts user input consisting of a name and age, increments the age by 1, and prints the name and new age. If the age input is not a valid integer, the script will print the name with an age of 0.

#### Usage
Run the script.
Provide input in the format "name age".
Press Enter.
The script will output the name with the incremented age.
Repeat steps 2-4 as needed.
To exit, enter "-1".

The script uses a try/except block to handle ValueError exceptions when converting the input string to an integer, ensuring smooth execution even with invalid input.


