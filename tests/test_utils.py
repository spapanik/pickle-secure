import datetime
from pytest import raises, fixture

from pickle_secure._utils import pad, unpad, encrypt, decrypt, DecryptionError


@fixture(scope="module")
def data():
    key = "strong password"
    wrong_key = "weak password"
    secret = "secret"
    encrypted_data = encrypt(secret, key)
    return {
        "key": key,
        "wrong_key": wrong_key,
        "encrypted_data": encrypted_data,
    }


def test_pad_unpad():
    quantum_length = 16
    for length in range(quantum_length + 1):
        string = b"x" * length
        padded_string = pad(string, quantum_length)
        assert len(padded_string) % quantum_length == 0
        assert string == unpad(pad(string, quantum_length))


def test_encrypt_decrypt():
    raw_data = [123, "£¿éά", {(2, 3, 5): datetime.datetime.now()}]
    key = "strong password"
    assert raw_data == decrypt(encrypt(raw_data, key), key)


def test_empty_data():
    assert raises(DecryptionError, decrypt, b"", data()["key"])


def test_wrong_password():
    assert raises(
        DecryptionError, decrypt, data()["encrypted_data"], data()["wrong_key"]
    )


def test_too_short_for_iv():
    assert raises(
        DecryptionError, decrypt, data()["encrypted_data"][:10], data()["key"]
    )


def test_too_short_for_padding():
    assert raises(
        DecryptionError, decrypt, data()["encrypted_data"][:32], data()["key"]
    )


def test_too_short_for_decrypting():
    assert raises(
        DecryptionError, decrypt, data()["encrypted_data"][:33], data()["key"]
    )
