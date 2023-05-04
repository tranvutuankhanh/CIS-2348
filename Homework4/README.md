# Homework4 Readme

## 12_7
This Python script calculates the fat-burning heart rate for a user based on their age.

The script consists of two main functions: get_age() and fat_burning_heart_rate(age).

get_age(): Prompts the user to input their age and checks if it is within the acceptable range (18 to 75). If the age is valid, it returns the age; otherwise, it raises a ValueError with a message "Invalid age."

fat_burning_heart_rate(age): Takes the age as a parameter and calculates the fat-burning heart rate using the formula (220 - age) * 0.7.

## 12_9
The Age Incrementer is a simple Python script that accepts user input consisting of a name and age, increments the age by 1, and prints the name and new age. If the age input is not a valid integer, the script will print the name with an age of 0.

#### Usage
1.Run the script.
2.Provide input in the format "name age".
3.Press Enter.
4.The script will output the name with the incremented age.
5.Repeat steps 2-4 as needed.
6.To exit, enter "-1".

#### Error Handling
The script uses a try/except block to handle ValueError exceptions when converting the input string to an integer, ensuring smooth execution even with invalid input.

## 14_11
This is a Python implementation of the selection sort algorithm. The program sorts a list of numbers in descending order and prints the intermediate steps during the sorting process. This can be helpful for understanding how the selection sort algorithm works.

#### Usage
1.Clone the repository to your local machine.
2.Open your terminal and navigate to the directory containing the script.
3.Run the script with python selection_sort_descend_trace.py or python3 selection_sort_descend_trace.py (depending on your Python installation).
4.Enter a space-separated list of integers when prompted.
5.The script will display the intermediate steps of the sorting process.

## 14_13
This Python program implements the Quicksort algorithm to sort an array of user IDs. It also keeps track of the number of calls to the quicksort function.

#### How to run the program
1.Ensure you have Python installed on your system.
2.Copy and paste the code into a new file called quicksort_user_ids.py.
3.Run the program using the command: python quicksort_user_ids.py.

#### Program Input
The program will prompt you to enter user IDs one at a time. Once you have entered all the user IDs you want to sort, enter -1 to indicate the end of input.

#### Program Output
The program will output the number of calls made to the quicksort function, followed by the sorted list of user IDs.

#### Functions
1.partition(user_ids, i, k): This function is used by the quicksort algorithm to partition the array into two parts based on a pivot. It returns the index of the pivot.
2.quicksort(user_ids, i, k): This function implements the quicksort algorithm on the given array of user IDs from index i to index k.

#### Main program
The main program reads user IDs from input until -1 is entered, then calls the quicksort function to sort the array, and finally prints the number of calls to the quicksort function and the sorted user IDs.




