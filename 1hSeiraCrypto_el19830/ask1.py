from collections import defaultdict
import re

english_freqs = [ {'A': 8.5}, {'B': 2.07}, {'C': 4.54}, {'D': 3.38}, {'E': 11.16}, {'F': 1.81}, {'G': 2.47}, {'H': 3},
                  {'I': 7.54}, {'J': 0.2}, {'K': 1.1}, {'L': 5.49}, {'M': 3.01}, {'N': 6.65}, {'O': 7.16}, {'P': 3.17},
                  {'Q': 0.2}, {'R': 7.58}, {'S': 5.74}, {'T': 6.95}, {'U': 3.63}, {'V': 1.01}, {'W': 1.29}, {'X': 0.29},
                  {'Y': 1.78}, {'Z': 0.27} ]

english_freqs = [{'E': 11.16}, {'A': 8.5}, {'R': 7.58}, {'I': 7.54}, {'O': 7.16}, {'T': 6.95}, {'N': 6.65}, {'S': 5.74}, 
                 {'L': 5.49}, {'C': 4.54}, {'U': 3.63}, {'D': 3.38}, {'P': 3.17}, {'M': 3.01}, {'H': 3}, {'G': 2.47}, {'B': 2.07}, 
                 {'F': 1.81}, {'Y': 1.78}, {'W': 1.29}, {'K': 1.1}, {'V': 1.01}, {'X': 0.29}, {'Z': 0.27}, {'J': 0.2}, {'Q': 0.2}]

input = []
input_length = 0
input_freqs = [ {'A': 0}, {'B': 0}, {'C': 0}, {'D': 0}, {'E': 0}, {'F': 0}, {'G': 0}, {'H': 0},
                {'I': 0}, {'J': 0}, {'K': 0}, {'L': 0}, {'M': 0}, {'N': 0}, {'O': 0}, {'P': 0},
                {'Q': 0}, {'R': 0}, {'S': 0}, {'T': 0}, {'U': 0}, {'V': 0}, {'W': 0}, {'X': 0},
                {'Y': 0}, {'Z': 0} ]
letter_counter = 0


doubles = []
triples = []

def decrypt(input_file):
    global letter_counter
    global input_freqs
    with open(input_file, 'r') as file:
        input = list(file.read())

    for i in range (0, len(input)): 
        # check if current input character is letter
        if input[i].isalpha():
            current_letter = input[i]
            # iterate the frequencies to find the element with the current_letter
            for letter_freq in input_freqs:
                if current_letter in letter_freq:
                    # increase the frequency by 1
                    letter_freq[current_letter] += 1              
            letter_counter += 1

    # sort input_freqs on descending order
    input_freqs = sorted(input_freqs, key = lambda x:list(x.values())[0], reverse=True)
    print(input_freqs)

def collect_bigrams(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    input_text =''.join(lines)

    words = re.findall(r'\b[A-Za-z]+\b', input_text)
    bigram_freqs = defaultdict(int)

    for word in words:
        for i in range (0, len(word)):
            if (len(word) > 1 and (i + 1 < len(word))):
                bigram = word[i] + word[i + 1]
                bigram_freqs[bigram] += 1
    bigram_freqs = sorted(bigram_freqs.items(), key=lambda x: x[1], reverse=True)
    return bigram_freqs


def collect_trigrams(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    input_text =''.join(lines)

    words = re.findall(r'\b[A-Za-z]+\b', input_text)
    trigram_freqs = defaultdict(int)

    for word in words:
        for i in range (0, len(word)):
            if (len(word) > 2 and (i + 2 < len(word))):
                trigram = word[i] + word[i + 1] + word[i + 2]
                trigram_freqs[trigram] += 1
    trigram_freqs = sorted(trigram_freqs.items(), key=lambda x: x[1], reverse=True)
    return trigram_freqs

def find_words_with_p(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    input_text =''.join(lines)

    words = re.findall(r'\b[A-Za-z]+\b', input_text)
    res = []
    allowed_letters = set('UKVRQWLCGI')
    for word in words:
        for letter in word:
            #if 'U' in word or 'K' in word or 'V' in word or 'R' in word or 'Q' in word or 'W' in word or 'L' in word or 'C' in word or 'G' in word and word not in res and len(word) <= 3:
            if letter in allowed_letters and word not in res and len(word) < 6:
                res.append(word)
                break
    return res

def replace_letters(input_file, letter_mapping):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    input_text =''.join(lines)
    # Convert the list of dictionaries into a dictionary
    mapping_dict = {k: v for mapping in letter_mapping for k, v in mapping.items()}

    # Replace letters in the text using the mapping
    replaced_text = ''.join(mapping_dict.get(char, char) for char in  input_text)

    return replaced_text

    
input_file = "cipher.txt"

decrypt(input_file)
print("\n\n")
print(collect_bigrams(input_file))
print("\n\n")
print(collect_trigrams(input_file))
print("\n\n")
print(find_words_with_p(input_file))
print("\n\n")
# MEROS -> ZEROS αρα M->Z. To S δεν παει καπου γτ δεν εμφανιζεται πουθενα
letter_mapping = [{'U': 'E'}, {'K': 'T'}, {'V': 'H'}, {'R': 'R'}, {'Q': 'O'}, {'W': 'A'}, {'L': 'L'}, {'C': 'I'}, 
                  {'G': 'S'}, {'I': 'P'}, {'D': 'N'}, {'N': 'U'}, {'B': 'M'}, {'A': 'B'}, 
                  {'X': 'V'}, {'Z': 'W'}, {'H': 'C'}, {'T': 'X'}, {'J': 'G'}, {'O': 'Y'}, 
                  {'Y': 'D'}, {'P': 'F'}, {'E': 'J'}, {'F': 'Q'}, {'M': 'Z'}]

print(replace_letters(input_file, letter_mapping))



