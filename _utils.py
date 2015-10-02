import pickle

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2

import settings


class DecryptionError(Exception):
    pass


def pad(string):
    n = len(string)
    multiplicity = settings.block_size - n % settings.block_size
    padding_char = chr(multiplicity).encode()
    return string + multiplicity * padding_char


def unpad(string):
    multiplicity = string[-1]
    return string[:-multiplicity]


def encrypt(raw_data, key, protocol=None, fix_imports=True):
    salt = Random.new().read(settings.block_size)
    key = PBKDF2(key, salt, settings.key_size)
    iv = Random.new().read(settings.block_size)
    cipher = AES.new(key, settings.mode, iv)
    pickled_data = pickle.dumps(
        raw_data, protocol=protocol, fix_imports=fix_imports
    )
    padded_data = pad(pickled_data)
    encrypted_data = cipher.encrypt(padded_data)
    output_data = salt + iv + encrypted_data
    return output_data


def decrypt(input_data, key, fix_imports=True,
            encoding='ASCII', errors='strict'):
    salt = input_data[:settings.block_size]
    iv = input_data[settings.block_size:2*settings.block_size]
    encrypted_data = input_data[2*settings.block_size:]
    key = PBKDF2(key, salt, settings.key_size)
    try:
        cipher = AES.new(key, settings.mode, iv)
        padded_data = cipher.decrypt(encrypted_data)
        pickled_data = unpad(padded_data)
        raw_data = pickle.loads(
            pickled_data, fix_imports=fix_imports,
            encoding=encoding, errors=errors
        )
    except (EOFError, IndexError, ValueError):
        raise DecryptionError('Could not decrypt the data.')
    return raw_data
