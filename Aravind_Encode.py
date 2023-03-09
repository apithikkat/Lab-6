# Aravind Ithikkat

def encode(password):
    encoded_password = ''
    for char in password:
        digit = int(char) + 3     # changing each character to an integer to add 3 to it
        encoded_password += str(digit)      # changing back to a string to compile into encoded password
    return encoded_password

def decoder(encoded_password):
    decoded_password = ""
    for i in encoded_password:
        decoded_digit = str((int(i) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password

def main():

    menu = True

    while menu:
        print()

        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()
        menu_option = int(input('Please enter an option: '))

        if menu_option == 1:
            password = input('Please enter your password to encode: ')
            Encoded_password = encode(password)
            print('Your password has been encoded and stored!')

        if menu_option == 2:
            Decoded_password = decoder(encoded_password)
            print()
            print(f'The encoded password is {Encoded_password}, and the original password is {Decoded_password}.')

        if menu_option == 3:
            break


if __name__ == '_main_':
    main()


