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
def generate_candidate_keys(DICTIONARY_FILE: str) -> list[str]:
    # Opening dictionary, reading, putting each line into a list
    candidate_keys: list[str] = []
    
    dictionary: str = open(DICTIONARY_FILE)
    for line in dictionary:
        candidate_key:str = dictionary.readline().rstrip()
        candidate_keys.append(candidate_key)
      
    return candidate_keys
    
def rijndael_encryption(ciphertext: str, candidate_keys: list[str]): # Don't know the return type yet
    # Repeating the algorihm for every candidate key
    for key in candidate_keys:
        # Convert candidate key to bytes and hashing
        byte_key: bytes = key.encode()
        
        hash_object = sha256()
        hash_object.update(byte_key)
        hashed_key = hash_object.digest()
        
        # Need to make byte array object rather than just bytes 
        # because a bytes object is immutable
        #initialization_vector


# =====================================================
# MAIN
# =====================================================

if __name__ == '__main__':
    input_ciphertext: bytes = take_input()
    candidate_keys: str = generate_candidate_keys(DICTIONARY_FILE)
    rijndael_encryption(input_ciphertext, candidate_keys)


