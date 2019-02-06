import pyperclip

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(keys,message):
    encrypted_message = []
    key_index = 0
    keys = keys.upper()

    for char in message:
        num = LETTERS.find(char.upper())
        if num != -1:
            num += LETTERS.find(keys[key_index])
            num %= len(LETTERS)
            if char.isupper():
                encrypted_message.append(LETTERS[num])
            elif char.islower():
                encrypted_message.append(LETTERS[num].lower())
            key_index += 1

            if key_index == len(keys):
                key_index = 0
    return ''.join(encrypted_message)


def decrypt(keys,encrypted_message):
    decrypted_message = []
    key_index = 0
    keys = keys.upper()

    for char in encrypted_message:
        num = LETTERS.find(char.upper())
        if num != -1:
            num -= LETTERS.find(keys[key_index])
            num %= len(LETTERS)
            if char.isupper():
                decrypted_message.append(LETTERS[num])
            elif char.islower():
                decrypted_message.append(LETTERS[num].lower())
            key_index += 1

            if key_index == len(keys):
                key_index = 0
    return ''.join(decrypted_message)

