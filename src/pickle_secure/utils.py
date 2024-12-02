from __future__ import annotations

import base64
import pickle
import secrets

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

SALT_SIZE = 16


def derive_key(password: str, salt: bytes) -> bytes:
    encoded_password = password.encode()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
        backend=default_backend(),
    )
    return base64.urlsafe_b64encode(kdf.derive(encoded_password))


def encrypt(
    raw_data: object,
    password: str,
    protocol: int | None = None,
    *,
    fix_imports: bool = True,
) -> bytes:
    salt = secrets.token_bytes(SALT_SIZE)
    key = derive_key(password, salt)
    fernet = Fernet(key)
    pickled_data = pickle.dumps(raw_data, protocol=protocol, fix_imports=fix_imports)
    encrypted_data: bytes = fernet.encrypt(pickled_data)
    return salt + encrypted_data


def decrypt(
    input_data: bytes,
    password: str,
    *,
    fix_imports: bool = True,
    encoding: str = "ASCII",
    errors: str = "strict",
) -> object:
    salt = input_data[:SALT_SIZE]
    encrypted_data = input_data[SALT_SIZE:]
    key = derive_key(password, salt)
    fernet = Fernet(key)
    pickled_data = fernet.decrypt(encrypted_data)
    return pickle.loads(  # noqa: S301
        pickled_data, fix_imports=fix_imports, encoding=encoding, errors=errors
    )
