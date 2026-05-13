# Rijndael

# Team Name: Encryptodes
# Members: Barry Dees, Niko Kraus, Steven Alleman, Isaiah Hinds, Javen Wilson

from sys import stdin, stdout, stderr
from hashlib import sha256
from Crypto import Random
from Crypto.Cipher import AES

# the AES block size to use
BLOCK_SIZE = 16

# the padding character to use to make the plaintext a multiple of BLOCK_SIZE in length
PAD_WITH = "#"


# =====================================================
# CHANGE THESE VALUES ONLY
# =====================================================

# For ciphertext-1, ciphertext-2, ciphertext-3:
DICTIONARY_FILE = "dictionary1-3.txt"
#THRESHOLD = 
#USE_TAG = 
#BINARY_OUTPUT = 
#START_FILTER = []

# For ciphertext-4, use:
#DICTIONARY_FILE = "dictionary4.txt"
#THRESHOLD = 
#USE_TAG = 
#BINARY_OUTPUT = 
#START_FILTER = []

# For ciphertext-5, use:
#DICTIONARY_FILE = "dictionary5.txt"
#THRESHOLD = 
#USE_TAG = 
#BINARY_OUTPUT = 
#START_FILTER = []

# =====================================================
# ALGORITHM IMPLEMENTATION
# =====================================================

# Reading the ciphertext from Stdin as bytes
def take_input() -> bytes:
    # Error handling here could later be a potential point of failure
    user_input:bytes = stdin.read().encode('utf-8', errors='surrogateescape')
    return user_input
    
# Reading dictionary. Takes in file name and returns list of possible keys
def read_dictionary(DICTIONARY_FILE: str) -> list[str]:
    # Opening dictionary, reading, putting each line into a list
    possible_keys: list[str] = []
    
    dictionary: str = open(DICTIONARY_FILE)
    for line in dictionary:
        possible_key:str = dictionary.readline()
        possible_keys.append(possible_key)
      
    return possible_keys
    

# =====================================================
# MAIN
# =====================================================

if __name__ == '__main__':
    input: bytes = take_input()
    print(read_dictionary(DICTIONARY_FILE))



