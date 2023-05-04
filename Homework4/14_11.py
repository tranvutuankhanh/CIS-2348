# Name: Vu Tran
# Student ID: 2233511

def selection_sort_descend_trace(lst):
    n = len(lst)  # Get list length

    for i in range(n - 1):
        max_idx = i  # Initialize max index

        # Loop through unsorted part of list
        for j in range(i + 1, n):
            if lst[j] > lst[max_idx]:
                max_idx = j  # Update max index

        # Swap elements
        lst[i], lst[max_idx] = lst[max_idx], lst[i]

        # Print current state of list
        print(' '.join(str(x) for x in lst) + ' ')


def main():
    lst = list(map(int, input().split()))  # Read and convert input
    selection_sort_descend_trace(lst)  # Sort list


if __name__ == "__main__":
    main()  # Run main function
