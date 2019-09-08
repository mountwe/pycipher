# Reverse Cipher
# https://www.nostarch.com/crackingcodes/ (BSD License)

message = input("Type in a message to be printed out reversed: ")
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)
