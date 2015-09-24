import datetime

from _utils import pad, unpad, encrypt, decrypt


def test_pad_unpad():
    for length in range(17):
        string = b'x' * length
        assert string == unpad(pad(string))


def test_encrypt_decrypt():
    raw_data = [
        123,
        '£¿éά',
        {
            (2, 3, 5): datetime.datetime.now()
        }
    ]
    key = 'strong password'
    assert raw_data == decrypt(encrypt(raw_data, key), key)
