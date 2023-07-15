from datetime import datetime, timezone

import pytest
from cryptography.fernet import InvalidToken

from pickle_secure import utils


def test_encrypt_decrypt() -> None:
    secret = [123, "£¿éά", {(2, 3, 5): datetime.now(tz=timezone.utc)}]
    password = "strong password"
    encrypted_data = utils.encrypt(secret, password)
    assert secret == utils.decrypt(encrypted_data, password)


def test_empty_data() -> None:
    password = "strong password"
    assert pytest.raises(InvalidToken, utils.decrypt, b"", password)


def test_wrong_password() -> None:
    secret = "secret"
    password = "strong password"
    wrong_key = "weak password"
    encrypted_data = utils.encrypt(secret, password)
    assert pytest.raises(InvalidToken, utils.decrypt, encrypted_data, wrong_key)


def test_too_short_for_decrypting() -> None:
    secret = "secret"
    password = "strong password"
    encrypted_data = utils.encrypt(secret, password)
    short_size = utils.SALT_SIZE - 1
    assert pytest.raises(
        InvalidToken, utils.decrypt, encrypted_data[:short_size], password
    )
