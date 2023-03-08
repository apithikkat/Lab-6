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
            menu_option = int(input('Enter 1 for password encoding\n\nEnter 2 for password decoding\n'))

            if menu_option == 1:
                password = input('Enter password for encoding: ')
                Encoded_password = encode(password)

            if menu_option == 2:
                Decoded_password = None

            if menu_option == 3:
                break


if __name__ == '_main_':
    main()


