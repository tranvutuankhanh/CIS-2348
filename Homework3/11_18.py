# Name: Vu Tran
# Student ID: 2233511

nums = list(map(int, input().split()))

# Keep only the non-negative integers
non_negatives = [num for num in nums if num >= 0]

# Sort the non-negative integers in ascending order
non_negatives.sort()

# Output the non-negative integers, separated by a space
for num in non_negatives:
    print(num, end=" ")
