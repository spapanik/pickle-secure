import pickle

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2

import settings


def pad(string):
    n = len(string)
    multiplicity = settings.block_size - n % settings.block_size
    padding_char = chr(multiplicity).encode()
    return string + multiplicity * padding_char


def unpad(string):
    multiplicity = string[-1]
    return string[:-multiplicity]


class Encrypt(object):
    def __init__(self, key, salt=None):
        if salt is None:
            salt = Random.new().read(settings.block_size)
        self.salt = salt
        self.key = PBKDF2(key, salt, settings.key_size)

    def encrypt(self, raw_data):
        iv = Random.new().read(settings.block_size)
        cipher = AES.new(self.key, settings.mode, iv)
        pickled_data = pickle.dumps(raw_data)
        padded_data = pad(pickled_data)
        encrypted_data = cipher.encrypt(padded_data)
        output_data = iv + encrypted_data
        return output_data

    def decrypt(self, input_data):
        iv = input_data[:settings.block_size]
        cipher = AES.new(self.key, settings.mode, iv)
        encrypted_data = input_data[settings.block_size:]
        padded_data = cipher.decrypt(encrypted_data)
        pickled_data = unpad(padded_data)
        raw_data = pickle.loads(pickled_data)
        return raw_data
