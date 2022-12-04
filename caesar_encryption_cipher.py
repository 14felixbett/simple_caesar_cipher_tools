print('\nWELCOME! HERE IS A SIMPLE CAESAR CIPHER ENCRYPTION TOOL. \n______________________________________________________________')

# string module imported
import string

# define the encryption cipher function
def encrypt_cipher(text, shift, alphabets, characters):

# define the function to shift alphabets
    def shift_alphabet(alphabet):
        if shift_direction.lower() == 'left':
            return alphabet[(26-(shift%26)):] + alphabet[:(26-(shift%26))]
        elif shift_direction.lower() == 'right':
            return alphabet[(shift%26):] + alphabet[:(shift%26)]

# define the function to shift punctuation (characters)
    def shift_character(character):
        if shift_char.lower() == 'yes' or shift_char.lower() == 'y':
            if shift_direction.lower() == 'left':
                return character[(32-(shift%32)):] + character[:(32-(shift%32))]
            elif shift_direction.lower() == 'right':
                return character[(shift%32):] + character[:(shift%32)]
        elif shift_char.lower() == 'no' or shift_char.lower() == 'n':
            return character[0:] + character[:0]

    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    # the map() function returns a map object (an iterator) of the results

    final_alphabet = ''.join(alphabets)
    final_shifted = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted)

    shifted_characters = tuple(map(shift_character, characters))
    final_character = ''.join(characters)
    final_shifted_char = ''.join(shifted_characters)
    table_char = str.maketrans(final_character, final_shifted_char)
    return text.translate(table).translate(table_char)

# prompt user to input message and required specifications for encryption
plain_text = input('\nPlease enter the message you want encrypted. \nMESSAGE: ')
shift_char = input('\nDoes your message have characters? And if yes, do you also want to shift them? ENTER (yes/ y) OR (no/ n): ')
shift = int(input('\nPlease enter the number of positions you want to shift the message: '))
shift_direction = input('\nTo specify the direction you want the message shifted, please ENTER; (left OR right): ')

print('\nThe encrypted message is;') # encryption cipher function called returns encrypted message
print('ENCRYPTED MESSAGE: ', encrypt_cipher(plain_text, shift, [string.ascii_lowercase, string.ascii_uppercase], [string.punctuation]))
print('______________________________________________________________________________________________________________________ \n')