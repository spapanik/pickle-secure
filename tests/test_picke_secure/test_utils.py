import datetime

from cryptography.fernet import InvalidToken
from pytest import raises

from pickle_secure import utils


def test_encrypt_decrypt():
    secret = [123, "£¿éά", {(2, 3, 5): datetime.datetime.now()}]
    password = "strong password"
    encrypted_data = utils.encrypt(secret, password)
    assert secret == utils.decrypt(encrypted_data, password)


def test_empty_data():
    password = "strong password"
    assert raises(InvalidToken, utils.decrypt, b"", password)


def test_wrong_password():
    secret = "secret"
    password = "strong password"
    wrong_key = "weak password"
    encrypted_data = utils.encrypt(secret, password)
    assert raises(InvalidToken, utils.decrypt, encrypted_data, wrong_key)


def test_too_short_for_decrypting():
    secret = "secret"
    password = "strong password"
    encrypted_data = utils.encrypt(secret, password)
    short_size = utils.SALT_SIZE - 1
    assert raises(InvalidToken, utils.decrypt, encrypted_data[:short_size], password)
