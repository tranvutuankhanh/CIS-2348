# Name: Vu Tran
# Student ID: 2233511

# Global variable to keep track of the number of calls to quicksort
num_calls = 0


# Partitioning algorithm used by quicksort to divide the array into two partitions
def partition(user_ids, i, k):
    # Choose the middle index as pivot index
    pivot_index = (i + k) // 2
    pivot = user_ids[pivot_index]
    l = i
    h = k
    # Loop until left and right indices meet
    while True:
        # Move the left index until it reaches a value greater than the pivot
        while user_ids[l] < pivot:
            l += 1
        # Move the right index until it reaches a value smaller than the pivot
        while user_ids[h] > pivot:
            h -= 1
        # If the left and right indices have crossed or met, return the right index as the pivot index
        if l >= h:
            return h
        # Swap the values at the left and right indices
        user_ids[l], user_ids[h] = user_ids[h], user_ids[l]
        # Move the left and right indices one step closer to each other
        l += 1
        h -= 1


# Quicksort algorithm to sort an array of user IDs
def quicksort(user_ids, i, k):
    # Declare the global variable to be modified inside the function
    global num_calls
    # Increment the number of calls to quicksort
    num_calls += 1
    # If there is more than one element to be sorted
    if i < k:
        # Partition the array using the pivot returned by partition() function
        pivot_index = partition(user_ids, i, k)
        # Recursively call quicksort for the left partition
        quicksort(user_ids, i, pivot_index)
        # Recursively call quicksort for the right partition
        quicksort(user_ids, pivot_index + 1, k)


# Main program
if __name__ == "__main__":
    user_ids = []
    # Read user IDs from input until -1 is entered
    user_id = input().strip()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input().strip()

    # Call quicksort on the entire array of user IDs
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print the number of calls to quicksort
    print(num_calls)

    # Print the sorted user IDs
    for user_id in user_ids:
        print(user_id)
