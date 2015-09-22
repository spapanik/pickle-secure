import pickle

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Protocol import KDF

block_size = AES.block_size
key_size = AES.key_size[2]
mode = AES.MODE_CBC
kdf = KDF.PBKDF2 


def pad(string):
    padding_char = chr(block_size - len(string) % block_size).encode()
    multiplicity = block_size - len(string) % block_size
    return string + multiplicity * padding_char


def unpad(string):
    multiplicity = string[-1]
    return string[:-multiplicity]


class Encrypt(object):
    def __init__(self, key, salt=None):
        if salt is None:
            salt = Random.new().read(block_size)
        self.salt = salt
        self.key = kdf(key, salt, key_size)

    def encrypt(self, raw_data):
        iv = Random.new().read(block_size)
        cipher = AES.new(self.key, mode, iv)
        pickled_data = pickle.dumps(raw_data)
        padded_data = pad(pickled_data)
        encrypted_data = cipher.encrypt(padded_data)
        output_data = iv + encrypted_data
        return output_data

    def decrypt(self, input_data):
        iv = input_data[:block_size]
        cipher = AES.new(self.key, mode, iv)
        encrypted_data = input_data[block_size:]
        padded_data = cipher.decrypt(encrypted_data)
        pickled_data = unpad(padded_data)
        raw_data = pickle.loads(pickled_data)
        return raw_data

