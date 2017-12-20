LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getLetterCount(message):
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    for letter in message.upper():
        if letter in LETTERS:
            letterCount[letter] += 1

    return letterCount

message = input('\n Message: ')
result = getLetterCount(message)

print('  \n +------------------+\n |')
print(' |  ' + message)
print(' |\n +------------------+')

print('   +--------------+')
for frequency in result:
    print('   |     ' + frequency + ':_' + str(result[frequency]) + '  \t  |')
    
print('   +--------------+')
print('')