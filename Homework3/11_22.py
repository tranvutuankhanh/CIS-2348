# Name: Vu Tran
# Student ID: 2233511

# Receive input string containing words separated by spaces.
word_list = input().split()

# Iterate over each word and count its occurrences in the string.
# Inefficient for large input strings, but works for small ones.
for word in word_list:
    count = 0
    for item in word_list:
        if word == item:
            count += 1

    # Print word and its count.
    print(word, count)