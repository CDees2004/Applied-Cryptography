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
#ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\\|;:'\",<.>/? "
# alternate alphabet used on ciphertext3
ALPHABET = " -,;:!?/.'\"()[]$&#%012345789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxyYzZ" 
PUNCTUATION = ".,!?;:'\"()[]{}<>-_+=/\\|`~@#$%^&*"

# debug for test printing 
DEBUG = False 


# -- top level notes -- 
    
# we are getting the key from the dictionary and using 
# the key in combination with the ciphertext to get our 
# plaintext. We need to utilize dictionaries because 
# plaintext AND key must be included in output. 


# -- reading the contents of the dictionary file --
with open("dictionary-1.txt", "r") as dictionary:
    dictionary_content = dictionary.read()

# normalizing words in the dictionary 
#dictionary_words: str = dictionary_content.lower().split()
dictionary_words = set() # used to store normalized results in helper function


# -- taking input from StdIn -- 
def take_input() ->str:
    userInput: str = sys.stdin.read()
    if(DEBUG):
        print(userInput)
    return userInput
  
    
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
def create_key(input_key: str, cipher_text: str) -> str: 
    # take one string as input and the length of 
    # the plaintext and repeat each char until its equal 
    # to the length of the plaintext 
    key_result: list[str] = [] 
    key_index: int = 0
    
    # iterating through each char in the text 
    for char in cipher_text: 
        if char in ALPHABET: 
            # iterating through key characters with wrap around 
            key_result.append(input_key[key_index % len(input_key)])
            key_index += 1 
        else: 
            # account for new lines
            key_result.append(char)
    
    string_result: str = "".join(key_result) 
    return string_result


# -- making one plaintext -- 
# a single decryption attempt taking a key and the ciphertext 
# to generate a plaintext candidate 
def decrypt_text(cipher_text: str, key: str) -> str: 
    # take one char from key and look it up on left of table 
    # scroll to the right until you reach the corresponding char of the ciphertext (row headers)
    # scroll up until you reach the resulting plaintext character (column headers)
    
    # key: plaintext_index is cipher_index - key_index % alphabet_length for wrapping 
    result: list[str] = [] 
    alphabet_length = len(ALPHABET)
    cipher_length = len(cipher_text)
    
    for value in range(cipher_length): 
        c = cipher_text[value] 
        k = key[value]
        
        if c in ALPHABET: 
            # find positions within the alphabet 
            c_index = ALPHABET.index(c) 
            k_index = ALPHABET.index(k)
            
            # actual decryption bit, finding our result 
            # giving our plaintext index 
            p_index = (c_index - k_index) % alphabet_length
            result.append(ALPHABET[p_index])
            
        else: 
            # accouting for new lines 
            result.append(c) 
            
    string_result: str = "".join(result) 
    return string_result 
            


# normalizing our words 
def normalize(word: str) -> str: 
    # removing punctuation and converting to lowercase 
    # to improve matches
    return word.strip(PUNCTUATION).lower()


def normalize_dictionary(): 
    for word in dictionary_content.split(): 
        normalized = word.strip(PUNCTUATION).lower() 
        if normalized: 
            dictionary_words.add(normalized)


# -- trying all possible keys -- 
def try_keys(cipher_text: str) -> dict[str, str]: 
    # treat every word as a possible key 
    # attempt a decryption and store that result to be later filtered 
    candidates: dict[str, str] = {}
    
    # dictionary_content read the entire file
    # need to break it up to be meaningful 
    words = dictionary_content.split()
    
    for key in words: 
        # expanding it for our cipher_text 
        full_key = create_key(key, cipher_text) 
        
        # decrypt using the key grabbed 
        plaintext = decrypt_text(cipher_text, full_key) 
        
        candidates[key] = plaintext 
        
        if DEBUG: 
            print(f"Key={key}\n{plaintext}\n")
    
    return candidates
    
    
# -- comparing candidate plaintexts against dictionary to get best candidate     
def compare_against_dictionary(candidate: str) -> float: 
    # getting a percentage score to judge candidate plaintexts 
    # a lot reused from program 1 here also
    words = candidate.split()
    score: int = 0 
    
    for word in words: 
        # normalizing everything for best comparisons 
        cleaned_word = normalize(word)
        
        # referring to our normalized version of the dict
        if cleaned_word in dictionary_words: 
            score += 1
            
    # giving our score as a percentage 
    return score / len(words)
    

# -- finding the best key and plaintext based on the score from comparison -- 
def get_best_candidate(candidates: dict[str, str]) -> tuple[str, str]: 
    # also borrows a  lot from program 1 
    best_key: str = "" 
    best_plaintext: str = "" 
    best_score = 0 
    
    # iterating through to find the best score 
    for key, text in candidates.items(): 
        score = compare_against_dictionary(text) 
        
        if DEBUG: 
            print(f"Key: {key}, Score: {score}")
         
        # updating our best match 
        if score > best_score: 
            best_score = score 
            best_key = key 
            best_plaintext = text 
            
    return best_key, best_plaintext 
   
### MAIN ###
# initial normalization 
normalize_dictionary()

user_input: str = take_input()
candidates = try_keys(user_input) 
key, plaintext = get_best_candidate(candidates) 

print(f"KEY={key}") 
print(plaintext)
