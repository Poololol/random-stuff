alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
badLetters = ['', '', '', '', '']
word = '_ount'
middleWords = []
outputWords = []
for letter in word:
    if letter == '_':
        for replacementLetter in alphabet:
            if replacementLetter not in badLetters:
                middleWords.append(word.replace('_', replacementLetter, 1))
print(middleWords)