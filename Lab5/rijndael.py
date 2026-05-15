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

PUNCTUATION = set("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")

# =====================================================
# CHANGE THESE VALUES ONLY
# =====================================================

# For ciphertext-1, ciphertext-2, ciphertext-3:
DICTIONARY_FILE = "dictionary1-3.txt"
THRESHOLD = 0.75
BINARY_OUTPUT = False
START_FILTER = []

# For ciphertext-4, use:
#DICTIONARY_FILE = "dictionary4-1.txt" # THIS NAME MIGHT NEED TO BE CHANGED IN YOUR GRADING
# THE TEMPLATE NAME DISAGREES WITH THE PROVIDED FILE NAME!!!!!
#THRESHOLD = 0.75
#BINARY_OUTPUT = True
#START_FILTER = ['j', 'J']

# For ciphertext-5, use:
#DICTIONARY_FILE = "dictionary5.txt"
#THRESHOLD = 0.75
#BINARY_OUTPUT = True
#START_FILTER = []

# =====================================================
# ALGORITHM IMPLEMENTATION
# =====================================================

# Reading the ciphertext from Stdin as bytes
def take_input() -> bytes:
    # user_input:bytes = stdin.read().encode('utf-8', errors='surrogateescape')
    # return user_input
    return stdin.buffer.read()
    
# Reading dictionary. Takes in file name and returns list of possible keys
def generate_candidate_keys(DICTIONARY_FILE: str) -> list[str]:
    # Opening dictionary, reading, putting each line into a list
    candidate_keys: list[str] = []
   
   # Using ignore to skip characters that don't fit the encoding
    with open(DICTIONARY_FILE, 'r', encoding="utf-8", errors="ignore") as dictionary_file:
        for line in dictionary_file:
            candidate_key: str = line.strip()
            # Filtering empty lines 
            if candidate_key:
                candidate_keys.append(candidate_key)
            
    return candidate_keys
    
# Helper function to perform the AES-CBC-Decrypt
def aes_cbc_decrypt(e, hashed_candidate_key, initialization_vector):
    cipher = AES.new(hashed_candidate_key, AES.MODE_CBC, initialization_vector)
    return cipher.decrypt(e)
    
# Helper function to normalize an individual word 
def normalize_word(word: str) ->str:
    normalized_word: str = ""
    for character in word: 
        if (character not in PUNCTUATION):
            normalized_word += character.lower()
            
    return normalized_word
    
# Normalizing the candidate keys
def normalize_dictionary(candidate_keys:str) ->set[str]:
    normalized_candidates = set()
    for word in candidate_keys:
        normalized_candidates.add(normalize_word(word))
    return normalized_candidates

# Scoring the plaintext candidates to be compared against THRESHOLD
def score_plaintexts(candidate_key: str, normalized_dictionary: list[str]):
    # Splitting m into words 
    split_m: str = candidate_key.split()
    total: int = 0 
    valid: int = 0
    for word in split_m: 
        normalized_word = normalize_word(word)
        if not normalized_word:
            # Skipping invalid words
            continue
        total += 1
        if normalized_word in normalized_dictionary:
            valid += 1
    # These will be compared against the THRESHOLD
    return valid, total

# Checking if the expected output is a PDF 
def check_PDF(m_bytes: bytes)-> bool:
    # Returns a boolean based on if the header is found
    return b"%PDF" in m_bytes[:20] or b"%PDF" in m_bytes
    
def rijndael_decryption(ciphertext: bytes, candidate_keys: list[str]):
    # Outside of loop since these calculations are the same for all candidate keys
    # IV is the first 16 bytes of the ciphertext 
    initialization_vector: bytes = ciphertext[:16]
    
    # E is the rest of the ciphertext 
    e: bytes = ciphertext[16:].strip(b"\r\n") # cleaning up invalid bytes

    # Need to trim padding on E to be a multiple of the block size 
    remainder_from_block_size: int = len(e) % BLOCK_SIZE
    if (remainder_from_block_size != 0):
        e = e[:-remainder_from_block_size] # Cutting the padding off
        
    # Normalizing the keys 
    normalized_dictionary: set = normalize_dictionary(candidate_keys)
        
    # Repeating the algorihm for every candidate key
    for candidate_key in candidate_keys:
        # If ciphertext-4 we can filter keys not starting with j/J
        if (START_FILTER):
            if candidate_key[0] not in START_FILTER:
                continue
                
        # Conerting candidate key to bytes and hashing 
        k = sha256(candidate_key.encode()).digest()
 
        # Applying the AES decryption algorithm to get M
        m: bytes = aes_cbc_decrypt(e, k, initialization_vector)
        # Removing padding. Must encode the pad char!!
        m = m.rstrip(PAD_WITH.encode())
        
        # If the expected output is readable text
        if not BINARY_OUTPUT:
            try:
                # Convert m from bytes -> string 
                m_string_rep: str = m.decode("utf-8", errors="ignore")
            except:
                # Skipping gibberish results
                continue
                
            # Scoring the plaintext candidate
            valid_words, total_words = score_plaintexts(m_string_rep, normalized_dictionary)
            
            # If the THRESHOLD is satisfied, the result is valid
            if (valid_words / total_words) > THRESHOLD:
                print(f"Key = {candidate_key}")
                print(m_string_rep)
                return
            
        # If the expected output is a PDF or binary file 
        elif (BINARY_OUTPUT or check_PDF(m)):
            # PRINTING FOR PDF AND BINARY, ASSIGNMENT DOES NOT MENTION HOW TO BINARY THAT ISNT PDF
            stderr.write(f"Key = {candidate_key}\n")
            # m as raw bytes to stdout
            stdout.buffer.write(m)
            return  
            
# =====================================================
# MAIN
# =====================================================

if __name__ == '__main__':
    input_ciphertext: bytes = take_input()
    candidate_keys: str = generate_candidate_keys(DICTIONARY_FILE)
    rijndael_decryption(input_ciphertext, candidate_keys)
