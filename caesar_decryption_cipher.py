print('\nWELCOME! HERE IS A SIMPLE CAESAR CIPHER DECRYPTION TOOL. \n______________________________________________________________')

# string module imported
import string

# define the decryption cipher function
def decrypt_cipher(text, shift, alphabets, characters):

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
    final_alphabet = ''.join(alphabets)
    final_shifted = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted)
# the maketrans() method returns a mapping table that can be used with the translate() method to replace;
# each item of the concatenated new string with the corresponding item in the same position in the new shifted string

    shifted_characters = tuple(map(shift_character, characters))
    final_character = ''.join(characters)
    final_shifted_char = ''.join(shifted_characters)
    table_char = str.maketrans(final_character, final_shifted_char)
    return text.translate(table).translate(table_char)

# prompt user to input message and required specifications for decryption
plain_text = input('Please enter the message you want decrypted. \nENCRYPTED MESSAGE: ')
shift_char = input('\nDo you have characters in your message? And if yes, were they shifted during encryption? ENTER (yes/ y) OR (no/ n): ')
shift = int(input('\nPlease enter the number of positions the message was shifted during encryption: '))
shift_direction = input('\nTo specify the direction you want the message shifted to decrypt, please ENTER; ("left", if to encrypt, the message was shifted right) OR ("right", if to encrypt, the message was shifted left): ')

print('\nThe decrypted message is;') # decrytion cipher function called; returns decrypted message
print('DECRYPTED MESSAGE: ', decrypt_cipher(plain_text, shift, [string.ascii_lowercase, string.ascii_uppercase], [string.punctuation]))
print('______________________________________________________________________________________________________________________ \n')