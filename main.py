
"""
Name: Justin

Purpose:  To write a Python solution that will encrypt and decrypt a message
    using a Vigenère cipher. Pseudocode to encrypt a message:
    1.	Initialize an empty string.
    2.	For each letter in the plaintext message:
    a.	Determine which letter of the key to use.
    b.	Using the key letter, look up the ciphertext letter in the
    Vigenère square in the plaintext character column.
    c.	Add the ciphertext letter to the ciphertext message.
    3.	Return the resulting string as the ciphertext message.
"""
#########################
# IMPORTS
#########################
from string import ascii_uppercase

#########################
# CONSTANTS
#########################
_ALPHABET = ascii_uppercase + ' '
_LETTERS_IN_ALPHABET = len(_ALPHABET) - 1


def valid_phrase(message):
    """
    valid_phrase checks that each character in the message is a letter
    in the alphabet. Calls the .find() function.
    Parameter message may have a space and letters of the alphabet.
    Returns a true if the message is alphabetic, and
    a false otherwise.

    :param message: a message to encrypt or decrypt
    :type message: a string
    :return: a boolean, false if any character in the message is not
    alphabetic, and true otherwise.
    :rtype: string
    """

    checking = message.replace(" ", "")
    length = len(checking)
    CHECKING = checking.isalpha()

    if message == "" or message == " ":
        return False

    for i in range(length):
        if CHECKING:
            return True
        else:
            return False

def letter_to_index(letter):
    """
    letter_to_index returns the index of the letter in the alphabet.
    Calls the .find() function.

    :param letter: one of the letters in the message
    :type letter: a string
    :return: the index of the parameter in the alphabet string
    :rtype: string
    """

    global _ALPHABET
    index = _ALPHABET.find(letter)
    return index

def index_to_letter(idx):
    """
    index_to_letter returns the letter of the alphabet based on the
    parameter index. Calls the .find() function.

    :param idx: the index of the parameter in the alphabet string
    :type idx: a string
    :return: the letter from the alphabet at the index provided
    :rtype: string
    """

    global _ALPHABET

    letter = _ALPHABET[idx]
    return letter

def vigenere_index(key_letter, plain_text_letter):
    """
    vigenere_index takes a letter from the key and a plaintext letter,
    and returns the encrypted letter. Calls the functions
    letter_to_index() and index_to_letter().

    :param key_letter: one letter from the key
    :type key_letter: String
    :param plain_text_letter:  one letter from the plain_text
    :type plain_text_letter: String
    :return: a single character as a string representing the
    encrypted letter
    :rtype: string
    """

    if plain_text_letter == " ":
        vig_letter = " "
    else:
        position_key = letter_to_index(key_letter)
        position_text = letter_to_index(plain_text_letter)
        vig_index = (position_text + position_key) % 26
        vig_letter = index_to_letter(vig_index)
    return vig_letter

def undo_vig(key_letter, ct_letter):
    """
    undo_vig takes a letter from the key, a ciphertext letter,
    and returns the plaintext letter. Calls the functions
    letter_to_index() and index_to_letter().

    :param key_letter: one letter from the key
    :type key_letter: string
    :param ct_letter:  one letter from the cypher text
    :type ct_letter: string
    :return: a string representing the unencrypted letter
    :rtype: string
    """

    if ct_letter == " ":
        vig_letter = " "
    else:
        position_key = letter_to_index(key_letter)
        position_cypher = letter_to_index(ct_letter)
        vig_index = (position_cypher - position_key) % 26
        while vig_index < 0 :
            vig_index += 26
        vig_letter = index_to_letter(vig_index)
    return vig_letter


def decrypt_vigenere(key, cipher_text):
    """
    decrypt_vigenere takes a keyword, the cipher text for the
    message, and returns the plain text message. Calls the
    function undo_vig().

    :param key: The decryption key
    :type key: string
    :param cipher_text:  The cipher text
    :type cipher_text: string
    :return: Returns a string representing the decrypted text
    :rtype: string
    """

    plain_text = ''
    key = key.replace(" ", "")

    cipher_length = len(cipher_text)
    for i in range(cipher_length):
        key_letter = key[i % len(key)]
        cipher_letter = cipher_text[i]
        plain_text += undo_vig(key_letter, cipher_letter)
    return plain_text

def encrypt_vigenere(key, plain_text):
    """
    encrypt_vigenere take a keyword and the plain text for the message,
    and returns the encrypted Vigenere cipher text. Calls the function
    vigenere_index().

    :param key: The encryption key
    :type key: string
    :param plain_text:  The plain text
    :type plain_text: string
    :return: Returns a string representing the encrypted text
    :rtype: string
    """

    encryted_cipher_text = ''
    length = len(plain_text)
    for i in range(length):
        KEY = key[i % len(key)]
        PLAIN_TEXT = plain_text[i]
        encryted_cipher_text += vigenere_index(KEY, PLAIN_TEXT)
    return encryted_cipher_text


def get_message():
    """
    Prompts the user for the message to be encrypted.
    Calls the.upper() function. Returns the message
    to be encrypted.

    :return: the message to be encrypted
    :rtype: string
    """
    message_encrypt = input("Enter the message to be encrypted: ").upper()
    return message_encrypt


def get_cyphertext():
    """
    Prompts the user for the cipher text to decrypt. Returns
    the cipher text to decrypt. Calls the.upper() function.

    :return: the cipher text to decrypt
    :rtype: string
    """

    cipher_text = input("Enter the cypher text to decrypt: ").upper()
    return cipher_text


def get_key():
    """
    Prompts the user for the Vigenere key. Returns the Vigenere key.
    Calls the .upper() function.

    :return: the Vigenere key
    :rtype: string
    """

    key = input("Enter the Vigenere key: ").upper()
    return key


def get_choice():
    """
    Prompts the user for their choice of E, Q, or D. Does not check for
    case. Calls the .input(),.upper() and .strip() functions.
    Returns the choice.

    :return: A string "E", "Q", or "D" representing the choice
    :rtype: string
    """

    message = input("Enter an E to encrypt a message, "\
                    "a D to decrypt a message, "\
                    "and Q to quit: ").upper()
    return message

def main():
    """
    A Python solution that will encrypt and decrypt a message
    using a Vigenère cipher.

    :return: none
    """

    INPUT = get_choice()
    while INPUT != 'Q':
        if INPUT == 'E':
            key = get_key()
            while valid_phrase(key) == False:
                print("Not a valid key! Letters must be in the alphabet.")
                key = get_key()
            message = get_message()
            while valid_phrase(message) == False:
                print("Not a valid message! Letters must be in the alphabet.")
                message = get_message()
            print(encrypt_vigenere(key, message))


        elif INPUT == 'D':
            key = get_key()
            while valid_phrase(key) == False:
                print("Not a valid key! Letters must be in the alphabet.")
                key = get_key()
            cyphertext = get_cyphertext()
            while valid_phrase(cyphertext) == False:
                print("Not a valid cypher! Letters must be in the alphabet.")
                cyphertext = get_cyphertext()
            print(decrypt_vigenere(key, cyphertext))



        elif INPUT == 'Q':
            exit()
        else:
            print("Invalid response!")

        INPUT = get_choice()


if __name__ == '__main__':
    main()
