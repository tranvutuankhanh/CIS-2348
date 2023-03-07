# Name: Vu Tran
# Student ID: 2233511

def isPalindrome(string):
    reversedString = string[::-1]
    if reversedString == string:
        return True
    else:
        return False


inputString = input()
string = inputString.replace(" ", "")
if isPalindrome(string):
    print(inputString, "is a palindrome")
else:
    print(inputString, "is not a palindrome")
