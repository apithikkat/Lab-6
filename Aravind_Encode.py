

def encode(password):
    encoded_password = ''
    for char in password:
        digit = int(char) + 3
        encoded_password += str(digit)
    return encoded_password



menu = True

while menu:
        menu_option = int(input('Enter 1 for password encoding\n\nEnter 2 for password decoding\n'))

        if menu_option == 1:
            password = input('Enter password for encoding: ')
            print()
            print(f'Encoded password is: {encode(password)}')
            print()


