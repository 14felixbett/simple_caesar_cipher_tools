print('\nWELCOME! HERE IS A SIMPLE CAESAR CIPHER DECRYPTION TOOL. \n______________________________________________________________')

# string module imported
# contains but not limited to lowercase and uppercase alphabet and punctuations required for,
# mapping to each letter or character of user input and shifting the user input to return the decrypted message
import string

# define the decryption cipher function
def decrypt_cipher(text, shift, alphabets, characters):

# since the length of alphabets(26 each for lowercase and uppercase) is not equal to that of the characters(32);
# two functions need to be defined to slice the alphabets or characters at,
# the number specified, of positions one wants to shift them
# and append them to the end of the remaining alphabets or characters

# function to shift alphabets defined
# to ensure that function still works when input of shift number is higher than length of either strings of alphabet;
# modulo operation used with length of either string of lowercase or uppercase alphabet
# functions needs to account for direction i.e., to shift either left or right when prompted by user for both alphabets and characters
    def shift_alphabet(alphabet):
        if shift_direction.lower() == 'left':
            return alphabet[(26-(shift%26)):] + alphabet[:(26-(shift%26))]
        elif shift_direction.lower() == 'right':
            return alphabet[(shift%26):] + alphabet[:(shift%26)]
    
# function to shift characters defined and same operations as in function to shift alphabets performed
# function specifies that characters are shifted only if user specifies that they also want to shift them
# else, do not shift characters, keep them as they are
    def shift_character(character):
        if shift_char.lower() == 'yes' or shift_char.lower() == 'y':
            if shift_direction.lower() == 'left':
                return character[(32-(shift%32)):] + character[:(32-(shift%32))]
            elif shift_direction.lower() == 'right':
                return character[(shift%32):] + character[:(shift%32)]
        elif shift_char.lower() == 'no' or shift_char.lower() == 'n':
            return character[0:] + character[:0]

# the map() function returns a map object (an iterator) of the results
# after applying the functions to each item of either strings of alphabet and/ or characters (punctuations)
# concatenate the results to form new string and the new shifted string after iteration
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