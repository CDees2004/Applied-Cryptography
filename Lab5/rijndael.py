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
PAD_WITH = b"#"


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
    user_input:bytes = stdin.read().encode('utf-8', errors='surrogateescape')
    return user_input
    # return stdin.buffer.read()
    
# Reading dictionary. Takes in file name and returns list of possible keys
def generate_candidate_keys(DICTIONARY_FILE: str) -> list[str]:
    # Opening dictionary, reading, putting each line into a list
    candidate_keys: list[str] = []
   
    with open(DICTIONARY_FILE, 'r') as dictionary_file:
        for line in dictionary_file:
            candidate_key: str = line.strip()
            candidate_keys.append(candidate_key)
            
    return candidate_keys
    
def rijndael_decryption(ciphertext: bytes, candidate_keys: list[str]):
    # Repeating the algorihm for every candidate key
    for key in candidate_keys:
        # Convert candidate key to bytes and hashing
        byte_key: bytes = key.encode() # Using bytes intead of bytearray to prevent side effects
        
        hash_object = sha256()
        hash_object.update(byte_key)
        hashed_key = hash_object.digest()
        
        # IV is the first 16 bytes of the ciphertext 
        initialization_vector: bytes = ciphertext[:16]
        
        # E is the rest of the ciphertext 
        e: bytearray = bytearray(ciphertext[16:])

        # # Need to pad E to be a multiple of the block size 
        while (len(e) % BLOCK_SIZE != 0):
            e.extend(PAD_WITH)
        
        # Applying the AES decryption algorithm
        cipher = AES.new(hashed_key, AES.MODE_CBC, initialization_vector)
        
        plaintext: bytes = cipher.decrypt(e)
      
# =====================================================
# MAIN
# =====================================================

if __name__ == '__main__':
    input_ciphertext: bytes = take_input()
    candidate_keys: str = generate_candidate_keys(DICTIONARY_FILE)
    rijndael_decryption(input_ciphertext, candidate_keys)
