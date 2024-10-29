words = ['Slate', 'Earthy', 'Quick']
output = ''
for word in words:
    word = word.lower()
    tempWord = ''
    for letter in word:
        if letter != 'a' and letter != 'e' and letter != 'i' and letter != 'o' and letter != 'u' and letter != '':
            tempWord = tempWord.join([letter, ''])    
    output = output.join([tempWord, ''])
    output = output.join([' ', ''])
output = output[::-1]
print(output)
