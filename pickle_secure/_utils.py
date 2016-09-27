import pickle
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2

block_size = AES.block_size
key_size = AES.key_size[2]
mode = AES.MODE_CBC


class DecryptionError(Exception):
    pass


def pad(string, length):
    n = len(string)
    multiplicity = block_size - n % length
    padding_char = chr(multiplicity).encode()
    return string + multiplicity * padding_char


def unpad(string):
    multiplicity = string[-1]
    return string[:-multiplicity]


def encrypt(raw_data, key, protocol=None, fix_imports=True):
    salt = Random.new().read(block_size)
    key = PBKDF2(key, salt, key_size)
    iv = Random.new().read(block_size)
    cipher = AES.new(key, mode, iv)
    pickled_data = pickle.dumps(
        raw_data, protocol=protocol, fix_imports=fix_imports
    )
    padded_data = pad(pickled_data, block_size)
    encrypted_data = cipher.encrypt(padded_data)
    output_data = salt + iv + encrypted_data
    return output_data


def decrypt(input_data, key, fix_imports=True,
            encoding='ASCII', errors='strict'):
    salt = input_data[:block_size]
    iv = input_data[block_size:2*block_size]
    encrypted_data = input_data[2*block_size:]
    key = PBKDF2(key, salt, key_size)
    try:
        cipher = AES.new(key, mode, iv)
        padded_data = cipher.decrypt(encrypted_data)
        pickled_data = unpad(padded_data)
        raw_data = pickle.loads(
            pickled_data, fix_imports=fix_imports,
            encoding=encoding, errors=errors
        )
    except (EOFError, IndexError, ValueError):
        raise DecryptionError('Could not decrypt the data.')
    return raw_data
