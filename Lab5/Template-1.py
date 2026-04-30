# Rijndael

# Team Name:
# Members:

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
THRESHOLD = 
USE_TAG = 
BINARY_OUTPUT = 
START_FILTER = []

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












