# Et tu, Brute?
#
# Team Name: Encryptodes
# Members: Barry Dees, Niko Krause, Javen Wilson,
#          Steven Alleman, and Isiah Hinds.
#
# A program that attempts to solve cipher texts that are 
# shifted by some number.

import sys

# the alphabet
ALPHABET = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQ
              RSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\\|;
              :'\",<.>/?"""
              
# debug for test printing 
DEBUG = True 


# -- taking input from StdIn -- 
def take_input():
    userInput: str = sys.stdin.read()
    if(DEBUG):
        print(userInput)


# -- performing a caesar cipher shift --

# take in alphabet list and shift amount, return shifted alphabet 
def caesar_shift(alphabet: str, shift_amount: int) ->str: 
    alphabet_length: int = len(ALPHABET) 
    result: list[str] = []
    
    for index in range(alphabet_length): 
        # using mod to account for wrapping 
        wrapped_index = (index + shift_amount) % alphabet_length 
        result.append(alphabet[wrapped_index])
    
    string_result: str = "".join(result) 
    return string_result 
    
    
# -- determine which results are valid by comparing word amount to
#    dictionary text file --


### MAIN ### 
take_input()
result_string: str = caesar_shift(ALPHABET, 1)
print(result_string)

   
