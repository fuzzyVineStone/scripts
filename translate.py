#!/bin/python

# variables

COLOR = '\033[92m'
NORMAL = '\033[0;37m'

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

DELIMITER = '|'
GREP_DELIMTER = ' '


# letter frequency

def letterFrequency(message):
    def getLetterCount(message):
        letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    
        for letter in message:
            if letter in LETTERS:
                letterCount[letter] += 1
    
        return letterCount
    
    result = getLetterCount(message)
    
    print(COLOR + '\n   letter frequency' + NORMAL)
    print(' +------------------+')
    print('    ' + message)
    print('  ------------------')
    
    print('   +--------------+')
    
    for frequency in result:
        print('   |     ' + frequency + ':_' + str(result[frequency]) + '  \t  |')
        
    print('   +--------------+')


# reverse

def reverse(message):
    print(COLOR + '\n\t  reverse' + NORMAL)
    print(' +--------------------------+')
    print('    ' + message[::-1])
    print('  --------------------------\n')


# atbash

def atbash(message):
    print(COLOR + '\n\t   atbash' + NORMAL)
    print(' +--------------------------+')
    
    def decode(message):
        result = ""
        for i in message:
            index = LETTERS.index(i)
            result += LETTERS[abs(len(LETTERS) - index - 1) % len(LETTERS)]
    
        return result
    
    print('    ' + decode(message))
    print('  --------------------------\n')


# caesar shift

def caesar(message):
    print(COLOR + '\n\tcaesar shifts' + NORMAL)
    print(' +--------------------------+')
    
    def caesar(message, shift):
        for shift in list(range(26)):
            shifted_LETTERS = LETTERS[shift:] + LETTERS[:shift]
            table = message.maketrans(LETTERS, shifted_LETTERS)
            print('    ' + str(shift) + ':\t' + str(message.translate(table)))
            shift += 1
    
    caesar(message, shift = 1)
    print('  --------------------------\n')


# logic

init_string = input('\n Message: ').upper()
string_table = init_string.split(DELIMITER)

for i in range(len(string_table)):
    string_table[i] = string_table[i].strip()

message = string_table[0]

if len(string_table) > 1:
    grep_table = string_table[1].split(GREP_DELIMTER)

    if grep_table[0] == 'GREP':
        if grep_table[1] == 'LETTERFREQUENCY':
            letterFrequency(message)
        elif grep_table[1] == 'REVERSE':
            reverse(message)
        elif grep_table[1] == 'ATBASH':
            atbash(message)
        elif grep_table[1] == 'CAESAR':
            caesar(message)
        else:
            print('\n  No such option...\n') 
    else:
        print('\n  No such argument...\n')
else:
    letterFrequency(message)
    reverse(message)
    atbash(message)
    caesar(message)
