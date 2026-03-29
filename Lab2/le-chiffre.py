# Le Chiffre
#
# Team Name: Encryptodes
# Members:Barry Dees, Niko Krause, Javen Wilson,
#         Steven Alleman, and Isiah Hinds.
#
# A program that attempts to solve cipher texts that are shifted by some number.
# For the thresholds, we were able to get ciphertext-1= , ciphertext-2= , 
# ciphertext-3= , ciphertext-4= , and the doubly encrypted=

import sys 

# the alphabet
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\\|;:'\",<.>/? "

# debug for test printing 
DEBUG = True 


# -- top level notes -- 
    
# we are getting the key from the dictionary and using 
# the key in combination with the ciphertext to get our 
# plaintext. We need to utilize dictionaries because 
# plaintext AND key must be included in output. 


# -- reading the contents of the dictionary file --
with open("dictionary.txt", "r") as dictionary:
    dictionary_content = dictionary.read()


# -- taking input from StdIn -- 
def take_input() ->str:
    userInput: str = sys.stdin.read()
    if(DEBUG):
        print(userInput)
    return userInput
  
  
# -- setting up the vigenere table    
def map_alphabet(): 
    # it is a table of all caesar shifts  
    
    
# -- performing a caesar cipher shift --
# recycled from program #1
# take in alphabet list and shift amount, return shifted alphabet 
def caesar_shift(alphabet: str, cipher_text: str, shift_amount: int) ->str: 
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
# recycled from program #1
def try_rotations(cipher_text: str) ->dict[int, str]:
    candidate_ciphers: dict[int, str] = {}
    for i in range(len(ALPHABET)):
        
        plain_text_attempt: str = caesar_shift(ALPHABET, cipher_text, i)
        candidate_ciphers[i] = plain_text_attempt
        if(DEBUG): 
            print(f"Shift of {i} \n", plain_text_attempt)
    return candidate_ciphers
        
    
# -- creating a single key -- 
# take the key and repeat it to the length of the plaintext 
def create_key(input_key: str) -> str: 
    # take one string as input and the length of 
    # the plaintext and repeat each char until its equal 
    # to the length of the plaintext 
    pass


# -- making one plaintext -- 
# a single decryption attempt taking a key and the ciphertext 
# to generate a plaintext candidate 
def decrypt_text(plaintext: str, key: str) -> str: 
    # take one char from key and look it up on left of table 
    # scroll to the right until you reach the corresponding char of the ciphertext (row headers)
    # scroll up until you reach the resulting plaintext character (column headers)
    pass


# -- trying all possible keys -- 
def try_keys(): 
    pass 
    
    
# -- generating all plaintexts with keys -- 
def generate_plaintext_candidates(): 
    pass 
    
    
# -- comparing candidate plaintexts against dictionary to get best candidate     
def compare_against_dictionary(): 
    pass 

   
### MAIN ###
user_input: str = take_input()
