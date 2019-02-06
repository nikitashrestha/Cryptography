def encode(message,keys):
    cipher_text = ""
    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            cipher_text += chr((ord(char) + keys - 65) % 26 + 65)
        elif char.islower():
            cipher_text += chr((ord(char) + keys - 97) % 26 + 97)
        elif char.isspace():
            cipher_text += " "
    return cipher_text


def decode(encrypted_message,keys):
    plain_text = ""
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        if char.isupper():
            plain_text += chr((ord(char) - keys - 65) % 26 + 65)
        elif char.islower():
            plain_text += chr((ord(char) - keys - 97) % 26 + 97)
        elif char.isspace():
            plain_text += " "

    return plain_text

