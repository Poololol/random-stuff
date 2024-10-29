alphabet = list('abcdefghijklmnopqrstuvwxyz')
shift = 1
message = 'This is a test of the caesar cipher!'
encrypedMessage = ''
for letter in message.lower():
    if letter not in alphabet:
        encrypedMessage += letter
    else:
        encrypedMessage += alphabet[alphabet.index(letter)+shift % len(alphabet)]
print(encrypedMessage)
