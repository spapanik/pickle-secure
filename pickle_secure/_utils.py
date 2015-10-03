import pickle
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2

from . import _settings


class DecryptionError(Exception):
    pass


def pad(string):
    n = len(string)
    multiplicity = _settings.block_size - n % _settings.block_size
    padding_char = chr(multiplicity).encode()
    return string + multiplicity * padding_char


def unpad(string):
    multiplicity = string[-1]
    return string[:-multiplicity]


def encrypt(raw_data, key, protocol=None, fix_imports=True):
    salt = Random.new().read(_settings.block_size)
    key = PBKDF2(key, salt, _settings.key_size)
    iv = Random.new().read(_settings.block_size)
    cipher = AES.new(key, _settings.mode, iv)
    pickled_data = pickle.dumps(
        raw_data, protocol=protocol, fix_imports=fix_imports
    )
    padded_data = pad(pickled_data)
    encrypted_data = cipher.encrypt(padded_data)
    output_data = salt + iv + encrypted_data
    return output_data


def decrypt(input_data, key, fix_imports=True,
            encoding='ASCII', errors='strict'):
    salt = input_data[:_settings.block_size]
    iv = input_data[_settings.block_size:2*_settings.block_size]
    encrypted_data = input_data[2*_settings.block_size:]
    key = PBKDF2(key, salt, _settings.key_size)
    try:
        cipher = AES.new(key, _settings.mode, iv)
        padded_data = cipher.decrypt(encrypted_data)
        pickled_data = unpad(padded_data)
        raw_data = pickle.loads(
            pickled_data, fix_imports=fix_imports,
            encoding=encoding, errors=errors
        )
    except (EOFError, IndexError, ValueError):
        raise DecryptionError('Could not decrypt the data.')
    return raw_data
