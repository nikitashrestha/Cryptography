from string import ascii_letters,digits
from random import shuffle

def random_mono_alpha(pool = None):
    if pool is None:
        pool = ascii_letters + digits
    original_pool = list(pool)
    shuffled_pool = list(pool)
    shuffle(shuffled_pool)
    return dict(zip(original_pool, shuffled_pool))


def inverse_mono_alpha(monoalpha_cipher):
    inverse_monoalpha = {}
    for key, value in monoalpha_cipher.items():
        inverse_monoalpha[value] = key
    return inverse_monoalpha


def encrypt(message, monoalpha_cipher):
    encrypted_message = []
    for letter in message:
        encrypted_message.append(monoalpha_cipher.get(letter, letter))
    return ''.join(encrypted_message)


def decrypt(encrypted_message,monoalpha_cipher):
    return encrypt(encrypted_message, inverse_mono_alpha(monoalpha_cipher))


cipher = random_mono_alpha()
print(cipher)
en_msg = encrypt("Hello World", cipher)
print(en_msg)
print(decrypt(en_msg,cipher))