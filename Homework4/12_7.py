# Name: Vu Tran
# Student ID: 2233511


def get_age():
    # Get the user's age as an integer
    age = int(input())
    # Check if the age is within the acceptable range (18 to 75)
    if 18 <= age <= 75:
        return age
    # If the age is not within the range, raise a ValueError with a message
    raise ValueError("Invalid age.")


def fat_burning_heart_rate(age):
    # Calculate the fat-burning heart rate using the formula (220 - age) * 0.7
    return (220 - age) * 0.7


if __name__ == "__main__":
    try:
        # Get the user's age using the get_age() function
        age = get_age()
        # Calculate and print the fat-burning heart rate for the given age
        print("Fat burning heart rate for a", age, "year-old:", fat_burning_heart_rate(age), "bpm")
    except ValueError as e:
        # If a ValueError is raised (i.e., age is not within the range), print the error message
        print(e)
        print("Could not calculate heart rate info.\n")
