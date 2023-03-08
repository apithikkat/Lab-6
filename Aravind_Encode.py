

def encode(password):
    encoded_password = ''
    for char in password:
        digit = int(char) + 3     # changing each character to an integer to add 3 to it
        encoded_password += str(digit)      # changing back to a string to compile into encoded password
    return encoded_password



menu = True

while menu:
        menu_option = int(input('Enter 1 for password encoding\n\nEnter 2 for password decoding\n'))

        if menu_option == 1:
            password = input('Enter password for encoding: ')
            print()
            print(f'Your encoded password is: {encode(password)}')
            print()


