# Le Chiffre
#
# Team Name: Encryptodes
# Members:Barry Dees, Niko Krause, Javen Wilson,
#         Steven Alleman, and Isiah Hinds.
#
# A program that attempts to solve cipher texts that are shifted by some number.
# For the thresholds, we were able to get ciphertext-1= , ciphertext-2= , ciphertext-3= , ciphertext-4= , and the doubly encrypted=

import sys 

# the alphabet
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\\|;:'\",<.>/? "

# debug for test printing 
DEBUG = True 

# -- taking input from StdIn -- 
def take_input() ->str:
    userInput: str = sys.stdin.read()
    if(DEBUG):
        print(userInput)
    return userInput
    
    
# -- reading the contents of the dictionary file --
with open("dictionary.txt", "r") as dictionary:
    dictionary_content = dictionary.read()
    

    
### MAIN ###
