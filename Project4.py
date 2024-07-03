#Kelsey Nobles (Klnobles)
#COP2002 0M1
#7/2/2024
# This program creates a simple Ceaser cipher encryption.

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
           "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

encrypted_letters = ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                     "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                     "A", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                     "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a"]


def caesar_cipher_encrypt(message):
    encrypted_message = []
    for char in message:
        if char.isalpha(): 
            if char in letters:
                index = letters.index(char)
                encrypted_char = encrypted_letters[index]
                encrypted_message.append(encrypted_char)
            elif char in letters:
                index = letters.index(char)
                encrypted_char = encrypted_letters[index]
                encrypted_message.append(encrypted_char)
    return ''.join(encrypted_message)


message = input("Enter a message to encrypt: ")
encrypted_message = caesar_cipher_encrypt(message)
print(f"Encrypted message: {encrypted_message}")
