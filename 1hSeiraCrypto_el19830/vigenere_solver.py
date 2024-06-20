import math
import sys

letter_mappings = { 'A': 1,'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
                    'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16,
                    'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24,
                    'Y': 25, 'Z': 26 }

# split input_text to groups (list of lists) based on key. For example if key = 3 will have 3 groups and in the first group will be char 1, 4, 7, etc
def split(key, input_text):
    n = len(input_text)     
    groups = [[] for _ in range(key)]
    for i in range (0, n):
        groups[i % key].append(input_text[i])
    return groups

# returns the index_of_coincidence of a text, given as a list of characters (text_list)
def index_of_coincidence(text_list, n):
    letter_freqs = {}
    
    for letter in text_list:
        if letter in letter_freqs:
            letter_freqs[letter] += 1
        else:
            letter_freqs[letter] = 1

    ic = 0
    for letter in letter_freqs:
        ic += (letter_freqs[letter] / n) * ( (letter_freqs[letter] - 1) / (n - 1) )
    
    return ic  
    
# takes a list of decrypted character which is each group that was splitted, and decrypts it because each group has been encrypted with caesar
# Returns the shift which corresponds to a letter of the key.
def caesar_decrypt(group):
    letter_freqs = {}
    english_freqs =    {'A': 8.5,'B': 2.07, 'C': 4.54, 'D': 3.38, 'E': 11.16, 'F': 1.81, 'G': 2.47, 'H': 3,
                        'I': 7.54, 'J': 0.2, 'K': 1.1, 'L': 5.49, 'M': 3.01, 'N': 6.65, 'O': 7.16, 'P': 3.17,
                        'Q': 0.2, 'R': 7.58, 'S': 5.74, 'T': 6.95, 'U': 3.63, 'V': 1.01, 'W': 1.29, 'X': 0.29,
                        'Y': 1.78, 'Z': 0.27}
    
    for letter in group:
        if letter in letter_freqs:
            letter_freqs[letter] += 1
        else:
            letter_freqs[letter] = 1
    
    def shift(letter_freqs, n):
        shifted_freqs = {}
        for letter, frequency in letter_freqs.items():
            # Convert the letter to uppercase and calculate the shifted position
            shifted_letter = chr(((ord(letter) - ord('A') + n) % 26) + ord('A'))
            
            # Update the frequency in the shifted dictionary
            shifted_freqs[shifted_letter] = frequency
        
        return shifted_freqs
    
    min_entropy = 2**10
    n = 0
    for i in range (1, 26):
        shifted_by_n_freqs = shift(letter_freqs, i)
        current_entropy = 0
        for letter in shifted_by_n_freqs:
            current_entropy += (shifted_by_n_freqs[letter] / len(group)) * math.log10(english_freqs[letter])
        current_entropy *= -1
        if current_entropy < min_entropy:
            min_entropy = current_entropy
            n = i

    c = group[0]
    p = chr(((ord(group[0]) - ord('A') + n) % 26) + ord('A'))

    key_char_map = (letter_mappings[c] - letter_mappings[p]) % 26
    key_char = chr(ord('A') + key_char_map)
        
    return key_char

# receives an input_file and does the decryption. It outputs 5 possible plaintexts with keys and ics
def vigenere_decrypt(input_file):
    # whole input text. with commas etc
    input_text = []

    # input text but only letters
    input_text_letters = []

    try:
        file = open(input_file, 'r')
        input_text = list(file.read())
        # list of letters of input text
        input_text_letters = [char for char in input_text if char.isalpha()]
    finally:
        file.close()

    key = 2
    # length of input but only characters
    n = len(input_text_letters)
    groups = []
    ic_counter = 0
    while ic_counter < 10:
        decrypted_text = []
        mean_ic = 0

        # split text in groups based on candidate key length
        groups = split(key, input_text_letters)
        for group in groups:
            if len(group) > 1:
                mean_ic += index_of_coincidence(group, len(group))
        # find mean index of coincidence of all groups
        mean_ic /= key

        if mean_ic >= 0.06 and mean_ic <= 0.07:     
            vigenere_key = ""
            # decrypt each group seperately with caesar and find key, cause each group indicates a key character
            for group in groups:
                vigenere_key += caesar_decrypt(group)

            key_counter = 0
            # decrypt the text with key
            for i in range (0, len(input_text)):
                if key_counter == len(vigenere_key):
                    key_counter = 0
                if input_text[i].isalpha():
                    decrypted_text.append(chr ((letter_mappings[input_text[i]] - letter_mappings[vigenere_key[key_counter]]) % 26 + ord('A')))
                    key_counter += 1
                else:
                    decrypted_text.append(input_text[i])

            print()
            decrypted_text_str = ''.join(decrypted_text)
            print(vigenere_key + '\n\n' +  decrypted_text_str + '\n')
            print(mean_ic)
            print("-----------------------------------------------------------------------------------------")
            ic_counter += 1

        key += 1
        if (key == n):
            break

input_file = sys.argv[1]
vigenere_decrypt(input_file)