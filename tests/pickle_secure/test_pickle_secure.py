import datetime

from cryptography.fernet import InvalidToken
from pytest import raises

from pickle_secure import pickle_secure


def test_dump_load(tmpdir):
    file = tmpdir.join("secret.pickle")
    secret = [123, "£¿éά", {(2, 3, 5): datetime.datetime.now()}]
    password = "strong password"
    with open(file, "wb") as f:
        pickle_secure.dump(secret, f, key=password)
    with open(file, "rb") as f:
        decrypted_data = pickle_secure.load(f, key=password)
    assert secret == decrypted_data


def test_dumps_loads():
    secret = [123, "£¿éά", {(2, 3, 5): datetime.datetime.now()}]
    password = "strong password"
    encrypted_data = pickle_secure.dumps(secret, key=password)
    assert secret == pickle_secure.loads(encrypted_data, key=password)


def test_dumps_loads_wrong_password():
    secret = [123, "£¿éά", {(2, 3, 5): datetime.datetime.now()}]
    password = "strong password"
    wrong_password = "weak password"
    encrypted_data = pickle_secure.dumps(secret, key=password)
    assert raises(InvalidToken, pickle_secure.loads, encrypted_data, key=wrong_password)


def test_pickler_unpickler_classes(tmpdir):
    file = tmpdir.join("secret.pickle")
    password = "strong password"
    secret = {123, "£¿éά", None}
    with open(file, "wb") as f:
        pickler = pickle_secure.Pickler(f, key=password)
        pickler.dump(secret)
    with open(file, "rb") as f:
        unpickler = pickle_secure.Unpickler(f, key=password)
        decrypted_data = unpickler.load()
    assert secret == decrypted_data
