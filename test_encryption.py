from encryption import pad, unpad, Encrypt

import datetime


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
    encryptor = Encrypt('strong password')
    assert raw_data == encryptor.decrypt(encryptor.encrypt(raw_data))
