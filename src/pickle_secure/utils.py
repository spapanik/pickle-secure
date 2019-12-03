import base64
import os
import pickle

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

SALT_SIZE = 16


def derive_key(password, salt):
    password = password.encode()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
        backend=default_backend(),
    )
    return base64.urlsafe_b64encode(kdf.derive(password))


def encrypt(raw_data, password, protocol=None, fix_imports=True):
    salt = os.urandom(SALT_SIZE)
    key = derive_key(password, salt)
    fernet = Fernet(key)
    pickled_data = pickle.dumps(raw_data, protocol=protocol, fix_imports=fix_imports)
    encrypted_data = fernet.encrypt(pickled_data)
    return salt + encrypted_data


def decrypt(input_data, password, fix_imports=True, encoding="ASCII", errors="strict"):
    salt = input_data[:SALT_SIZE]
    encrypted_data = input_data[SALT_SIZE:]
    key = derive_key(password, salt)
    fernet = Fernet(key)
    pickled_data = fernet.decrypt(encrypted_data)
    return pickle.loads(
        pickled_data, fix_imports=fix_imports, encoding=encoding, errors=errors
    )
