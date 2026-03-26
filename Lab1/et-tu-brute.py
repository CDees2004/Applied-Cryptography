# Et tu, Brute?
#
# Team Name: Encryptodes
# Members: Barry Dees, Niko Krause, Javen Wilson,
#          Steven Alleman, and Isiah Hinds.
#
# A program that attempts to solve cipher texts that are 
# shifted by some number.

import sys

with open("dictionary.txt", "r") as dictionary:
    dictionary_content = dictionary.read()

# the alphabet
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\\|;:'\",<.>/? "


# debug for test printing 
DEBUG = True


# -- taking input from StdIn -- 
def take_input()->str:
    userInput: str = sys.stdin.read()
    if(DEBUG):
        print(userInput)
    return userInput


# -- performing a caesar cipher shift --
# take in alphabet list and shift amount, return shifted alphabet 
def caesar_shift(alphabet: str, cipher_text: str, shift_amount: int)->str: 
    alphabet_length: int = len(ALPHABET) 
    result: list[str] = []
    
    for index in range(alphabet_length): 
        # using mod to account for wrapping 
        # performing the actual shift to get a shifted alphabet 
        wrapped_index = (index + shift_amount) % alphabet_length 
        result.append(alphabet[wrapped_index])
    
 
    shifted_alphabet: str = "".join(result) 
    string_result: list[str] = []
    
    # apply the shifted alphabet to the cipher_text to get the plaintext attempts
    for character in cipher_text: 
        if character in alphabet:
            original_index = alphabet.index(character)
            string_result.append(shifted_alphabet[original_index])
        
    return "".join(string_result)


# -- trying all rotations -- 
def try_rotations(cipher_text: str): 
    for i in range(len(ALPHABET)):
        plain_text_attempt: str = caesar_shift(ALPHABET, cipher_text, i)
        if(DEBUG): 
            print(f"Shift of {i} \n", plain_text_attempt)
        
    
# -- determine which results are valid by comparing word amount to
#    dictionary text file --
def test_against_dictionary(candidate_cipher: str): 
    score: int = 0 
    for word in candidate_cipher: 
        if word in dictionary_content


### MAIN ### 
user_input_ciphertext: str = take_input()
try_rotations(user_input_ciphertext)
#test_case: str = caesar_shift(ALPHABET, user_input_ciphertext, 1)

   
