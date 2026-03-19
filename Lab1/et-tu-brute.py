# Et tu, Brute?
#
# Team Name: Encryptodes
# Members: Barry Dees, Niko Krause, Javen Wilson, Steven Alleman
#          Isaiah Hinds
#
# A program that attempts to solve cipher texts that are 
# shifted by some number.

#from sys import stdin
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
# for character at index i in ALPHABET, character = 
# char at index i + shift 
# def caesar_shift(shift_amount: int): 
    # alphabet_length: int = len(ALPHABET) 
    # for index, character in enumerate(ALPHABET): 
        # # mod to account for wrapped index 
        # wrapped_index = index % alphabet_length 
        # # using standard index 
        # if(index + shift_amount < alphabet_length): 
            # character[index] = character[index + shift_amount] 
        # # otherwise, using wrapped index 
        # else:
            # character[wrapped_index] = character[wrapped_index + shift_amount] 
           

# determine which results are valid by comparing word amount to
# dictionary text file 


### MAIN ### 
take_input()
caesar_shift(1) 
print(ALPHABET)
   
