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
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\\|;:'\",<.>/? "

# ciphertext-3 alphabet 
#ALPHABET = " -,;:!?/.'\"()[]$&#%012345789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxyYzZ"


# debug for test printing 
DEBUG = False


# -- reading the contents of the dictionary file --
with open("dictionary.txt", "r") as dictionary:
    dictionary_content = dictionary.read()


# -- taking input from StdIn -- 
def take_input() ->str:
    userInput: str = sys.stdin.read()
    if(DEBUG):
        print(userInput)
    return userInput


# -- performing a caesar cipher shift --
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
def try_rotations(cipher_text: str) ->list[str]:
    candidate_ciphers: list = []
    for i in range(len(ALPHABET)):
        
        plain_text_attempt: str = caesar_shift(ALPHABET, cipher_text, i)
        candidate_ciphers.append(plain_text_attempt)
        if(DEBUG): 
            print(f"Shift of {i} \n", plain_text_attempt)
    return candidate_ciphers
        
    
# -- testing candidates against dictionary -- 
# helper function that tests one candidate against the dictionary giving an accuracy percentage 
def test_against_dictionary(candidate_cipher: str) ->float: 
    score: int = 0 
    # tokenize candidate 
    split_candidate = candidate_cipher.split()
    for word in split_candidate: 
        if word in dictionary_content: 
            score += 1
    
    return score / len(split_candidate)
    
    
# test all candidates, returns the final best plaintext candidate 
def get_best_candidate(candidate_ciphers: list[str]) ->str: 
    scores: dict[float, str] = {}
    for candidate in candidate_ciphers: 
        # scores.append(test_against_dictionary(candidate))
        scores[candidate] = test_against_dictionary(candidate)
        
    # get key associated with kv pair that has max score value 
    best_candidate = max(scores, key=scores.get)
    return best_candidate   


### MAIN ### 
user_input_ciphertext: str = take_input()
candidate_ciphers = try_rotations(user_input_ciphertext)
print(get_best_candidate(candidate_ciphers))


   
