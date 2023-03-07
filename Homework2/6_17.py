# Name: Vu Tran
# Student ID: 2233511

word = input()

password = ''

for character in word:  # update password rather than word

    if character == 'i':
        password += '!'

    elif character == 'a':
        password += '@'

    elif character == 'm':
        password += 'M'

    elif character == 'B':
        password += '8'

    elif character == 'o':
        password += '.'

    else:
        password += character

print(f'{password}q*s')
