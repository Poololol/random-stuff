alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
badLetters = ['c', 'h', 'z', 'g', 'n']
word = ''
middleWords = []
outputWords = []
for letter in word:
    if letter == '_':
        for replacementLetter in alphabet:
            if replacementLetter not in badLetters:
                middleWords.append(word.replace('_', replacementLetter, 1))
for wordy in middleWords:
    for lettery in wordy:
        if lettery == '_':
            for replacementLettery in alphabet:
                if replacementLettery not in badLetters:
                    outputWords.append(wordy.replace('_', replacementLettery, 1))
print(outputWords)